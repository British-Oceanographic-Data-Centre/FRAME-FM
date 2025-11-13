
from .model import Model

class NeutalNet(Model):
    def __init__(self, layers: int):
        super().__init__()
        self.layers = layers
