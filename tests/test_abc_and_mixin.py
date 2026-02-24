import pytest

from src.ecommerce import BaseProduct, Product, Smartphone, LawnGrass


def test_base_product_is_abstract() -> None:
    with pytest.raises(TypeError):
        BaseProduct()


def test_creation_mixin_prints_for_product(capsys) -> None:
    product = Product("Test", "Desc", 100, 5)

    captured = capsys.readouterr()
    assert captured.out.strip() == "Product('Test', 'Desc', 100, 5)"

    assert product.name == "Test"
    assert product.quantity == 5


def test_creation_mixin_prints_for_smartphone(capsys) -> None:
    phone = Smartphone(
        name="Phone",
        description="Desc",
        price=1000,
        quantity=2,
        efficiency=10,
        model="X",
        memory=128,
        color="Black",
    )

    captured = capsys.readouterr()
    assert captured.out.strip() == "Smartphone('Phone', 'Desc', 1000, 2)"

    assert phone.model == "X"
    assert phone.memory == 128


def test_add_same_class_products() -> None:
    p1 = Product("A", "D", 100, 10)
    p2 = Product("B", "D", 200, 2)

    result = p1 + p2
    assert result == 1400


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
        price=10,
        quantity=2,
        country="RU",
        germination_period=7,
        color="Green",
    )

    with pytest.raises(TypeError):
        _ = phone + grass
