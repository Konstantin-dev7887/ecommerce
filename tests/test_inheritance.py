import pytest

from src.ecommerce import Category, LawnGrass, Product, Smartphone


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    Category.category_count = 0
    Category.product_count = 0


def test_smartphone_inheritance_and_attributes() -> None:
    phone = Smartphone(
        name="iPhone",
        description="Phone",
        price=1000.0,
        quantity=2,
        efficiency=9.5,
        model="15 Pro",
        memory=256,
        color="Gray",
    )

    assert isinstance(phone, Product)
    assert phone.efficiency == 9.5
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Gray"


def test_lawn_grass_inheritance_and_attributes() -> None:
    grass = LawnGrass(
        name="Green grass",
        description="Lawn",
        price=10.0,
        quantity=5,
        country="Netherlands",
        germination_period=14,
        color="Green",
    )

    assert isinstance(grass, Product)
    assert grass.country == "Netherlands"
    assert grass.germination_period == 14
    assert grass.color == "Green"


def test_add_only_same_class_allowed() -> None:
    p1 = Product(name="A", description="d", price=100, quantity=10)
    p2 = Product(name="B", description="d", price=200, quantity=2)

    assert p1 + p2 == 1400


def test_add_different_classes_raises_type_error() -> None:
    phone = Smartphone(
        name="Phone",
        description="d",
        price=100,
        quantity=10,
        efficiency=10,
        model="X",
        memory=128,
        color="Black",
    )

    grass = LawnGrass(
        name="Grass",
        description="d",
        price=200,
        quantity=2,
        country="RU",
        germination_period=7,
        color="Green",
    )

    with pytest.raises(TypeError):
        _ = phone + grass


def test_category_add_product_allows_subclasses() -> None:
    category = Category(name="Mixed", description="desc", products=[])

    phone = Smartphone(
        name="Phone",
        description="d",
        price=100,
        quantity=1,
        efficiency=10,
        model="X",
        memory=128,
        color="Black",
    )

    grass = LawnGrass(
        name="Grass",
        description="d",
        price=10,
        quantity=2,
        country="RU",
        germination_period=7,
        color="Green",
    )

    category.add_product(phone)
    category.add_product(grass)

    assert Category.product_count == 2


def test_category_add_product_rejects_non_product() -> None:
    category = Category(name="Mixed", description="desc", products=[])

    with pytest.raises(TypeError):
        category.add_product("not a product")