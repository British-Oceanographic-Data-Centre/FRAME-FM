
import pytorch_lightning as pl

class Model(pl.LightningModule):
    def log(self, *args, **kwargs):
        super().log(*args, **kwargs)

    def summary(self):
        # summary is not a direct method, but you can print model architecture
        print(self)
