from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Product.name must be a non-empty string")
        if not isinstance(self.description, str):
            raise TypeError("Product.description must be a string")
        if not isinstance(self.price, (int, float)):
            raise TypeError("Product.price must be a number")
        if float(self.price) < 0:
            raise ValueError("Product.price must be >= 0")
        if not isinstance(self.quantity, int):
            raise TypeError("Product.quantity must be an int")
        if self.quantity < 0:
            raise ValueError("Product.quantity must be >= 0")
