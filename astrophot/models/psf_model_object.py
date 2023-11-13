from typing import Optional

import torch

from .core_model import AstroPhot_Model
from ..image import (
    Model_Image,
    Window,
    PSF_Image,
    Image_List,
)
from ._shared_methods import select_target
from ..utils.decorators import default_internal, ignore_numpy_warnings
from ..param import Param_Unlock, Param_SoftLimits, Parameter_Node


__all__ = ["PSF_Model"]


class PSF_Model(AstroPhot_Model):
    """Prototype point source (typically a star) model, to be subclassed
    by other point source models which define specific behavior.

    PSF_Models behave differently than component models. For starters,
    their target image must be a PSF_Image object instead of a
    Target_Image object. PSF_Models also don't define a "center"
    variable since their center is always (0,0) just like a
    PSF_Image. A PSF_Model will never be convolved with a PSF_Model
    (that's it's job!), so a lot of the sampling method is simpler.

    """

    # Specifications for the model parameters including units, value, uncertainty, limits, locked, and cyclic
    parameter_specs = {}
    # Fixed order of parameters for all methods that interact with the list of parameters
    _parameter_order = ()
    model_type = f"psf {AstroPhot_Model.model_type}"
    useable = False
    # Method for initial sampling of model
    sampling_mode = "midpoint"  # midpoint, trapezoid, simpson

    # Level to which each pixel should be evaluated
    sampling_tolerance = 1e-2

    # Integration scope for model
    integrate_mode = "threshold"  # none, threshold, full*

    # Maximum recursion depth when performing sub pixel integration
    integrate_max_depth = 3

    # Amount by which to subdivide pixels when doing recursive pixel integration
    integrate_gridding = 5

    # The initial quadrature level for sub pixel integration. Please always choose an odd number 3 or higher
    integrate_quad_level = 3

    # Maximum size of parameter list before jacobian will be broken into smaller chunks, this is helpful for limiting the memory requirements to build a model, lower jacobian_chunksize is slower but uses less memory
    jacobian_chunksize = 10

    # Softening length used for numerical stability and/or integration stability to avoid discontinuities (near R=0)
    softening = 1e-3

    # Parameters which are treated specially by the model object and should not be updated directly when initializing
    special_kwargs = ["parameters", "filename", "model_type"]
    track_attrs = [
        "psf_mode",
        "psf_convolve_mode",
        "sampling_mode",
        "sampling_tolerance",
        "integrate_mode",
        "integrate_max_depth",
        "integrate_gridding",
        "integrate_quad_level",
        "jacobian_chunksize",
        "softening",
    ]

    def __init__(self, *, name=None, **kwargs):
        self._target_identity = None
        super().__init__(name=name,**kwargs)

        # Set any user defined attributes for the model
        for kwarg in kwargs:  # fixme move to core model?
            # Skip parameters with special behaviour
            if kwarg in self.special_kwargs:
                continue
            # Set the model parameter
            setattr(self, kwarg, kwargs[kwarg])

        # If loading from a file, get model configuration then exit __init__
        if "filename" in kwargs:
            self.load(kwargs["filename"], new_name = name)
            return

        self.parameter_specs = self.build_parameter_specs(
            kwargs.get("parameters", None)
        )
        with torch.no_grad():
            self.build_parameters()
            if isinstance(kwargs.get("parameters", None), torch.Tensor):
                self.parameters.value = kwargs["parameters"]
        assert torch.allclose(self.window.center, torch.zeros_like(self.window.center)), "PSF models must always be centered at (0,0)"

    # Initialization functions
    ######################################################################
    @torch.no_grad()
    @ignore_numpy_warnings
    @select_target
    @default_internal
    def initialize(
        self,
        target: Optional["PSF_Image"] = None,
        parameters: Optional[Parameter_Node] = None,
        **kwargs,
    ):
        """Determine initial values for the center coordinates. This is done
        with a local center of mass search which iterates by finding
        the center of light in a window, then iteratively updates
        until the iterations move by less than a pixel.

        Args:
          target (Optional[Target_Image]): A target image object to use as a reference when setting parameter values

        """
        super().initialize(target=target, parameters=parameters)
    
    # Fit loop functions
    ######################################################################
    def evaluate_model(
        self,
        X: Optional[torch.Tensor] = None,
        Y: Optional[torch.Tensor] = None,
        image: Optional["Image"] = None,
        parameters: "Parameter_Node" = None,
        **kwargs,
    ):
        """Evaluate the model on every pixel in the given image. The
        basemodel object simply returns zeros, this function should be
        overloaded by subclasses.

        Args:
          image (Image): The image defining the set of pixels on which to evaluate the model

        """
        if X is None or Y is None:
            X, Y = image.get_coordinate_meshgrid()
        return torch.zeros_like(X)  # do nothing in base model

    def sample(
        self,
        image: Optional["Image"] = None,
        window: Optional[Window] = None,
        parameters: Optional[Parameter_Node] = None,
    ):
        """Evaluate the model on the space covered by an image object. This
        function properly calls integration methods. This should not
        be overloaded except in special cases.

        This function is designed to compute the model on a given
        image or within a specified window. It takes care of sub-pixel
        sampling, recursive integration for high curvature regions,
        and proper alignment of the computed model with the original
        pixel grid. The final model is then added to the requested
        image.

        Args:
          image (Optional[Image]): An AstroPhot Image object (likely a Model_Image)
                                     on which to evaluate the model values. If not
                                     provided, a new Model_Image object will be created.
          window (Optional[Window]): A window within which to evaluate the model.
                                   Should only be used if a subset of the full image
                                   is needed. If not provided, the entire image will
                                   be used.

        Returns:
          Image: The image with the computed model values.

        """
        # Image on which to evaluate model
        if image is None:
            image = self.make_model_image(window=window)

        # Window within which to evaluate model
        if window is None:
            working_window = image.window.copy()
        else:
            working_window = window.copy()

        # Parameters with which to evaluate the model
        if parameters is None:
            parameters = self.parameters

        if "window" in self.psf_mode:
            raise NotImplementedError("PSF convolution in sub-window not available yet")

        # Create an image to store pixel samples
        working_image = Model_Image(
            pixelscale=image.pixelscale, window=working_window
        )
        # Evaluate the model on the image
        reference, deep = self._sample_init(
            image=working_image,
            parameters=parameters,
            center=torch.zeros_like(working_image.center),
        )
        # Super-resolve and integrate where needed
        deep = self._sample_integrate(
            deep,
            reference,
            working_image,
            parameters,
            center=torch.zeros_like(working_image.center),
        )
        # Add the sampled/integrated pixels to the requested image
        working_image.data += deep

        if self.mask is not None:
            working_image.data = working_image.data * torch.logical_not(self.mask)

        image += working_image

        return image

    @property
    def target(self):
        try:
            return self._target
        except AttributeError:
            return None

    @target.setter
    def target(self, tar):
        assert tar is None or isinstance(tar, PSF_Image)

        # If a target image list is assigned, pick out the target appropriate for this model
        if isinstance(tar, Image_List) and self._target_identity is not None:
            for subtar in tar:
                if subtar.identity == self._target_identity:
                    usetar = subtar
                    break
            else:
                raise KeyError(
                    f"Could not find target in Target_Image_List with matching identity to {self.name}: {self._target_identity}"
                )
        else:
            usetar = tar

        self._target = usetar

        # Remember the target identity to use
        try:
            self._target_identity = self._target.identity
        except AttributeError:
            pass


    # Extra background methods for the basemodel
    ######################################################################
    from ._model_methods import radius_metric
    from ._model_methods import angular_metric
    from ._model_methods import _sample_init
    from ._model_methods import _sample_integrate
    from ._model_methods import _integrate_reference
    from ._model_methods import build_parameter_specs
    from ._model_methods import build_parameters
    from ._model_methods import jacobian
    from ._model_methods import _chunk_jacobian
    from ._model_methods import get_state
    from ._model_methods import load