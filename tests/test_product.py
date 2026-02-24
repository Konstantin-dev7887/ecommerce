from decimal import Decimal

import pytest

from src.ecommerce import Product


def test_product_initialization_success() -> None:
    product = Product(
        name="Coffee",
        description="Ground coffee 250g",
        price=7.5,
        quantity=25,
    )

    assert product.name == "Coffee"
    assert product.description == "Ground coffee 250g"
    assert product.price == Decimal("7.50")
    assert product.quantity == 25


def test_product_empty_name_raises() -> None:
    with pytest.raises(ValueError):
        Product(
            name="   ",
            description="Some desc",
            price=1.0,
            quantity=1,
        )


def test_product_negative_price_raises() -> None:
    with pytest.raises(ValueError):
        Product(
            name="Tea",
            description="Black tea",
            price=-1.0,
            quantity=1,
        )


def test_product_negative_quantity_raises() -> None:
    with pytest.raises(ValueError):
        Product(
            name="Tea",
            description="Black tea",
            price=1.0,
            quantity=-1,
        )
