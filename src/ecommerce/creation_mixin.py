from __future__ import annotations


class CreationMixin:
    def _print_creation_info(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        price_value = self.price

        if float(price_value).is_integer():
            price_value = int(price_value)

        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, "
            f"{self.description!r}, "
            f"{price_value}, "
            f"{self.quantity})"
        )
