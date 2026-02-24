from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
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

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self._price = float(new_price)
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict) -> "BaseProduct":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __add__(self, other: object) -> float:
        # Требование из ДЗ4: складывать можно только объекты одного класса; использовать type()
        if type(other) is not type(self):
            raise TypeError("Можно складывать только продукты одного класса")

        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self) -> str:
        price_value: float = self.price
        price_part = int(price_value) if float(price_value).is_integer() else price_value

        return f"{self.__class__.__name__}({self.name!r}, {self.description!r}, {price_part}, {self.quantity})"

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError