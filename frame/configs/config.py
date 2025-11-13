
from dataclasses import dataclass
from hydra import initialize, compose

@dataclass
class sweepConfig:
    method: str = "random"
    num_samples: int = 10
    metric: str = "accuracy"
    direction: str = "maximize"

@dataclass
class hydraConfig:
    config_path: str = "../../configs/yaml/"
    config_name: str = "config"
    sweep: sweepConfig = sweepConfig()

@dataclass
class config:
    
    experiment_name: str = "default_experiment"
    run_name: str = "default_run"
    local: bool = True
    hyrda: hydraConfig = hydraConfig()
    


    def __init__(self):
        with initialize(config_path="../../configs/yaml/"):
            cfg = compose(config_name="config")
        self.cfg = cfg
