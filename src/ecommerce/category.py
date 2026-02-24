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

        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products

        Category.category_count += 1
        Category.product_count += len(products)
