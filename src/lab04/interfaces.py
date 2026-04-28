from abc import ABC, abstractmethod
from typing import Any

class Printable(ABC):
    """Интерфейс для объектов, которые могут быть представлены в виде строки"""
    
    @abstractmethod
    def to_string(self) -> str:
        """Возвращает строковое представление объекта"""
        pass


class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать"""
    
    @abstractmethod
    def compare_to(self, other: Any) -> int:
        """
        Сравнивает текущий объект с другим.
        Возвращает:
        - отрицательное число, если self < other
        - 0, если self == other
        - положительное число, если self > other
        """
        pass


class PowerRatable(ABC):
    """Интерфейс для объектов, имеющих рейтинг силы"""
    
    @abstractmethod
    def get_power_rating(self) -> float:  # ← ИСПРАВЛЕНО: rating, а не raiting
        """Возвращает рейтинг силы объекта"""
        pass

    