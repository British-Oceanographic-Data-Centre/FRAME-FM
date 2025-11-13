import mlflow.pytorch
import logging
import os
import time
import hydra
from omegaconf import DictConfig, OmegaConf
import pytorch_lightning as pl
import submitit
from configs import * 

from omegaconf import DictConfig

log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="configs",)
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    if not cfg.local:
        # running on cluster
        pass
    
    env = submitit.JobEnvironment()
    log.info(f"Process ID {os.getpid()} executing task {cfg.task}, with {env}")
    time.sleep(1)


if __name__ == "__main__":
    my_app()