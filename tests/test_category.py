import pytest

from src.ecommerce import Category
from src.ecommerce import Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    Category.category_count = 0
    Category.product_count = 0


def test_category_initialization_success_with_products() -> None:
    product_1 = Product(
        name="Phone",
        description="Smartphone",
        price=499.99,
        quantity=5,
    )
    product_2 = Product(
        name="Tablet",
        description="10-inch tablet",
        price=299.00,
        quantity=2,
    )

    category = Category(
        name="Electronics",
        description="Devices",
        products=[product_1, product_2],
    )

    assert category.name == "Electronics"
    assert category.description == "Devices"

    expected = (
        "Phone, 499 руб. Остаток: 5 шт.\n"
        "Tablet, 299 руб. Остаток: 2 шт.\n"
    )

    assert category.products == expected


def test_category_initialization_success_empty_products() -> None:
    category = Category(
        name="Books",
        description="All kinds of books",
        products=[],
    )

    assert category.name == "Books"
    assert category.description == "All kinds of books"
    assert category.products == ""


def test_category_empty_name_raises() -> None:
    with pytest.raises(ValueError):
        Category(
            name=" ",
            description="desc",
            products=[],
        )


def test_category_products_type_check_raises() -> None:
    with pytest.raises(TypeError):
        Category(
            name="Invalid",
            description="desc",
            products=["not a product"],  # type: ignore[list-item]
        )


def test_category_count_increments() -> None:
    assert Category.category_count == 0

    Category(name="A", description="desc", products=[])
    Category(name="B", description="desc", products=[])

    assert Category.category_count == 2


def test_product_count_increments_by_products_length() -> None:
    p1 = Product(name="P1", description="d", price=1.0, quantity=1)
    p2 = Product(name="P2", description="d", price=2.0, quantity=2)
    p3 = Product(name="P3", description="d", price=3.0, quantity=3)

    assert Category.product_count == 0

    Category(name="C1", description="desc", products=[p1, p2])
    assert Category.product_count == 2

    Category(name="C2", description="desc", products=[p3])
    assert Category.product_count == 3

    Category(name="C3", description="desc", products=[])
    assert Category.product_count == 3
