import pytest

from src.ecommerce import BaseProduct, LawnGrass, Product, Smartphone


def test_base_product_is_abstract() -> None:
    with pytest.raises(TypeError):
        BaseProduct("A", "D", 10, 1)  # type: ignore[abstract]


def test_mixin_prints_creation_info_for_product(capsys) -> None:
    product = Product("Продукт1", "Описание продукта", 1200, 10)

    captured = capsys.readouterr()
    assert captured.out.strip() == "Product('Продукт1', 'Описание продукта', 1200, 10)"
    assert product.name == "Продукт1"


def test_mixin_prints_creation_info_for_subclass(capsys) -> None:
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


def test_add_only_same_class_allowed() -> None:
    p1 = Product("A", "D", 100, 10)
    p2 = Product("B", "D", 200, 2)

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
        price=10,
        quantity=2,
        country="RU",
        germination_period=7,
        color="Green",
    )

    with pytest.raises(TypeError):
        _ = phone + grass