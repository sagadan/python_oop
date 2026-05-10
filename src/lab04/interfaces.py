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
        """Сравнивает текущий объект с другим"""
        pass


class PowerRatable(ABC):
    """Интерфейс для объектов, имеющих рейтинг силы"""
    
    @abstractmethod
    def get_power_rating(self) -> float:  
        """Возвращает рейтинг силы объекта"""
        pass

    