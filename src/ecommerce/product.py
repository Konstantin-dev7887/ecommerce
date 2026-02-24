from __future__ import annotations

from .base_product import BaseProduct
from .creation_mixin import CreationMixin


class Product(CreationMixin, BaseProduct):
    name: str
    description: str
    quantity: int
    _price: float

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
    ) -> None:

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product.name must be a non-empty string")

        if not isinstance(description, str):
            raise TypeError("Product.description must be a string")

        if not isinstance(price, (int, float)):
            raise TypeError("Product.price must be a number")

        if price <= 0:
            raise ValueError("Product.price must be > 0")

        if not isinstance(quantity, int):
            raise TypeError("Product.quantity must be an int")

        if quantity < 0:
            raise ValueError("Product.quantity must be >= 0")

        self.name = name
        self.description = description
        self._price = float(price)
        self.quantity = quantity

        self._print_creation_info()

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self._price = float(new_price)
        else:
            print("Price should be more then 0")

    def __str__(self) -> str:
        return (f"{self.name}, "
                f"{int(self.price)} руб. "
                f"Остаток: {self.quantity} шт.")

    def __add__(self, other: object) -> float:
        if type(self) is not type(other):
            raise TypeError("Only equals classes")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
