from typing import TypeVar, Generic, Callable, Optional, List, Protocol
from abc import ABC, abstractmethod

# Протоколы

class Displayable(Protocol):
    "Протокол для объектов, которые могут отображаться"
    def display(self) -> str:
        "Возвращает строковое представление объекта"
        ...


class Scorable(Protocol):
    "Протокол для объектов, которые имеют оценку/рейтинг"
    def score(self) -> float:
        "Возвращает числовую оценку объекта"
        ...


# Type var

D = TypeVar('D', bound=Displayable)  
S = TypeVar('S', bound=Scorable)     
T = TypeVar('T')                      
R = TypeVar('R')                      


class TypedCollection(Generic[T]):
   
    
    def __init__(self) -> None:
        "Инициализация пустой типизированной коллекции"
        self._items: List[T] = []
    
    # Основные методы
    
    def add(self, item: T) -> None:
        "Добавить элемент в коллекцию"
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        "Удалить элемент из коллекции"
        self._items.remove(item)
    
    def remove_at(self, index: int) -> T:
        "Удалить элемент по индексу"
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        raise IndexError(f"Индекс {index} вне диапазона (0-{len(self._items) - 1})")
    
    def get_all(self) -> List[T]:
        "Получить все элементы коллекции"
        return list(self._items)
    
    def __len__(self) -> int:
        "Количество элементов в коллекции"
        return len(self._items)
    
    def __getitem__(self, index: int) -> T:
        "Доступ по индексу"
        return self._items[index]
    
    def __iter__(self):
        "Итератор по коллекции"
        return iter(self._items)
    
    # Методы высшего порядка 
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
       
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
      
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        
        return [transform(item) for item in self._items]
    
    # Доп. методы
    
    def sort(self, key: Optional[Callable[[T], any]] = None, reverse: bool = False) -> None:
        "Отсортировать коллекцию"
        if key:
            self._items.sort(key=key, reverse=reverse)
        else:
            self._items.sort(reverse=reverse)
    
    def __str__(self) -> str:
        "Строковое представление коллекции"
        if not self._items:
            return "TypedCollection[]"
        
        result = f"TypedCollection[{type(self._items[0]).__name__}]:\n"
        for i, item in enumerate(self._items):
            result += f"  [{i}] {item}\n"
        return result


# Классы-адаптеры для демонстрации протоколов 

class DisplayAdapter:
    
    
    def __init__(self, name: str, description: str) -> None:
        self._name = name
        self._description = description
    
    def display(self) -> str:
        """Реализация метода display() - требуется протоколом Displayable"""
        return f"{self._name}: {self._description}"
    
    def __str__(self) -> str:
        return self.display()


class ScoreAdapter:
    
    
    def __init__(self, name: str, value: float) -> None:
        self._name = name
        self._value = value
    
    def score(self) -> float:
        "Реализация метода score() - требуется протоколом Scorable"
        return self._value
    
    def display(self) -> str:
        "Дополнительно реализуем display для удобства"
        return f"{self._name}: {self._value}"
    
    def __str__(self) -> str:
        return f"{self._name} (score: {self._value})"