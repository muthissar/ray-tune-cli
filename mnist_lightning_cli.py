#!/usr/bin/env python3

from mnist_model import LightningMNISTClassifier
from lightning.pytorch.cli import LightningCLI


def lightning_cli():
    LightningCLI(LightningMNISTClassifier)


if __name__ == "__main__":
    lightning_cli()
