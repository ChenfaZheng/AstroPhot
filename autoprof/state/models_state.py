from .substate_object import SubState
from autoprof.models import Model
from autoprof.pipeline.class_discovery import all_subclasses

class Models_State(SubState):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.models = {}
        self.model_list = []
        
    def add_model(self, name, model, **kwargs):
        MODELS = all_subclasses(Model)
        if isinstance(model, str):
            for m in MODELS:
                if m.name == model:
                    self.models[name] = m(name, self.state, self.state.data.image, **kwargs)
                    break
        elif isinstance(model, Model):
            self.models[name] = model(name, self.state, self.state.data.image, **kwargs)
        else:
            raise ValueError('model should be a string or AutoProf Model object, not: {type(model)}')
        self.model_list.append(name)
            
    def initialize(self):

        for m in self.model_list:
            self.models[m].initialize()

    def compute_loss(self):
        
        for m in self.model_list:
            self.models[m].compute_loss()

    def sample_models(self):

        for m in self.model_list:
            self.models[m].sample_model()
        
