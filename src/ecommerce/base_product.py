from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: object) -> float:
        pass
