import pytest

from src.ecommerce import Category, Product


def test_product_zero_quantity_raises() -> None:
    with pytest.raises(ValueError) as exc:
        Product("Bad", "Desc", 1000, 0)

    assert (str(exc.value) ==
            "Товар с нулевым количеством не может быть добавлен")


def test_category_middle_price() -> None:
    p1 = Product("A", "D", 100, 5)
    p2 = Product("B", "D", 200, 3)

    category = Category("Test", "Desc", [p1, p2])

    assert category.middle_price() == 150


def test_category_middle_price_empty() -> None:
    category = Category("Empty", "Desc", [])

    assert category.middle_price() == 0
