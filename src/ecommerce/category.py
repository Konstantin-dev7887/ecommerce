from __future__ import annotations

from typing import List

from .product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str,
                 description: str,
                 products: List[Product]) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Category.name must be a non-empty string")

        if not isinstance(description, str):
            raise TypeError("Category.description must be a string")

        if not isinstance(products, list):
            raise TypeError("Category.products must be a list")

        for product in products:
            if not isinstance(product, Product):
                raise TypeError(
                    "Category.products must contain only Product objects")

        self.name = name
        self.description = description
        self._products: List[Product] = products.copy()

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Can only add Product instance")

        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "".join(f"{str(product)}\n" for product in self._products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."