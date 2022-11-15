from .galaxy_model_object import Galaxy_Model
import torch
import numpy as np

__all__ = ["SuperEllipse_Galaxy"]

class SuperEllipse_Galaxy(Galaxy_Model):
    """Expanded galaxy model which includes a superellipse transformation
    in its radius metric. This allows for the expression of "boxy" and
    "disky" isophotes instead of pure ellipses. This is a common
    extension of the standard elliptical representation, especially
    for early-type galaxies.

    """
    model_type = f"superellipse {Galaxy_Model.model_type}"
    parameter_specs = {
        "C0": {"units": "C-2", "value": 0.},
    }
    
    def radius_metric(self, X, Y):
        return torch.pow(torch.pow(torch.abs(X)+1e-6, self["C0"].value + 2.) + torch.pow(torch.abs(Y)+1e-6, self["C0"].value + 2.), 1. / (self["C0"].value + 2.)) # epsilon added for numerical stability of gradient
    
    