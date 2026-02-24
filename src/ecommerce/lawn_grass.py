from __future__ import annotations

from .product import Product


class LawnGrass(Product):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: int,
            color: str,
    ) -> None:
        super().__init__(name=name,
                         description=description,
                         price=price,
                         quantity=quantity)

        self.country = country
        self.germination_period = germination_period
        self.color = color
