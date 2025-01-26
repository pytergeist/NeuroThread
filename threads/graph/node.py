import numpy as np
from typing import Optional

from threads.operations.operation import Operation


class Node:
    def __init__(
        self,
        value: np.ndarray,
        operation: Optional[Operation],
        parents: tuple = (),
        requires_grad: bool = False,
    ):
        self.value = value
        self.operation = operation
        self.parents = parents
        self.requires_grad = requires_grad
        self.grad = None
        self.name = None

    def __repr__(self):
        return f"""Node(name={self.name}, value={self.value}, 
        operation={self.operation}, parents={self.parents},
        requires_grad={self.requires_grad})"""
