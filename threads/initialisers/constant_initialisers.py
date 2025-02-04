import numpy as np

from threads.initialisers.initialiser import Initialiser
from threads.tensor import Tensor


class Constant(Initialiser):
    def __init__(self, value: float) -> None:
        self.value = value

    @property
    def name(self) -> str:
        return "constant_initialiser"

    def __call__(self, shape, dtype, **kwargs) -> Tensor:
        dtype = Tensor.standardise_dtype(dtype)
        return Tensor(
            self.value * np.ones(shape), dtype=dtype
        )  # TODO: change from np calls to generate tensor data

    def get_config(self):
        return {"value": self.value}

    @classmethod
    def from_config(cls, config):
        return cls(**config)


class Zeros(Initialiser):
    def __call__(self, shape, dtype, **kwargs) -> Tensor:
        dtype = Tensor.standardise_dtype(dtype)
        return Tensor(np.zeros(shape), dtype=dtype)

    @property
    def name(self) -> str:
        return "zeros_initialiser"


class Ones(Initialiser):
    def __call__(self, shape, dtype, **kwargs) -> Tensor:
        dtype = Tensor.standardise_dtype(dtype)
        return Tensor(np.ones(shape), dtype=dtype)

    @property
    def name(self) -> str:
        return "ones_initialiser"
