from __future__ import annotations

from .product import Product


class Smartphone(Product):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ) -> None:
        super().__init__(name=name,
                         description=description,
                         price=price,
                         quantity=quantity)

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
