from __future__ import annotations

from dataclasses import dataclass

from .base_product import BaseProduct
from .creation_info_mixin import CreationInfoMixin


@dataclass(slots=True)
class Product(CreationInfoMixin, BaseProduct):
    name: str
    description: str
    quantity: int
    _price: float

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name=name, description=description, price=price, quantity=quantity)

    def __str__(self) -> str:
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."