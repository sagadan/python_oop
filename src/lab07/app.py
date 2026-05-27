"""
Модуль бизнес-логики приложения
Управляет коллекцией персонажей и операциями над ней
"""

from typing import List, Optional, Callable
from models import Character, CharacterCollection, Warrior, Mage, Archer
from exceptions import CharacterNotFoundError, DuplicateCharacterError, InvalidCharacterDataError, InvalidClassTypeError


class CharacterApp:
    """Главный класс приложения для управления персонажами"""
    
    def __init__(self, collection: CharacterCollection = None):
        """
        Инициализация приложения
        
        Args:
            collection: Объект коллекции персонажей (опционально)
        """
        self._collection = collection if collection else CharacterCollection()
    
    @property
    def collection(self) -> CharacterCollection:
        """Получить коллекцию персонажей"""
        return self._collection
    
    def get_all_characters(self) -> List[Character]:
        """
        Получить список всех персонажей
        
        Returns:
            Список всех персонажей
        """
        return self._collection.get_all()
    
    def add_character(self, character: Character) -> None:
        """
        Добавить персонажа в коллекцию
        
        Args:
            character: Объект персонажа
        
        Raises:
            DuplicateCharacterError: Если персонаж с таким именем уже существует
        """
        existing = self._collection.find_by_name(character.game_name)
        if existing:
            raise DuplicateCharacterError(character.game_name)
        self._collection.add(character)
    
    def remove_character(self, name: str) -> Character:
        """
        Удалить персонажа по имени
        
        Args:
            name: Имя персонажа
        
        Returns:
            Удаленный персонаж
        
        Raises:
            CharacterNotFoundError: Если персонаж не найден
        """
        character = self._collection.find_by_name(name)
        if not character:
            raise CharacterNotFoundError(name)
        
        # Находим индекс и удаляем
        for i, c in enumerate(self._collection.get_all()):
            if c.game_name.lower() == name.lower():
                return self._collection.remove_at(i)
        
        raise CharacterNotFoundError(name)
    
    def find_character_by_name(self, name: str) -> Optional[Character]:
        """
        Найти персонажа по имени
        
        Args:
            name: Имя персонажа
        
        Returns:
            Найденный персонаж или None
        """
        return self._collection.find_by_name(name)
    
    def find_characters_by_health_range(self, min_health: int, max_health: int) -> List[Character]:
        """
        Найти персонажей в диапазоне здоровья
        
        Args:
            min_health: Минимальное здоровье
            max_health: Максимальное здоровье
        
        Returns:
            Список найденных персонажей
        """
        return self._collection.find_by_health_range(min_health, max_health)
    
    def find_characters_by_power_range(self, min_power: int, max_power: int) -> List[Character]:
        """
        Найти персонажей в диапазоне силы
        
        Args:
            min_power: Минимальная сила
            max_power: Максимальная сила
        
        Returns:
            Список найденных персонажей
        """
        return self._collection.find_by_power_range(min_power, max_power)
    
    def filter_by_class(self, class_type: str) -> List[Character]:
        """
        Фильтрация персонажей по классу
        
        Args:
            class_type: Тип класса ('Воин', 'Маг', 'Лучник')
        
        Returns:
            Список отфильтрованных персонажей
        
        Raises:
            InvalidClassTypeError: Если указан неверный тип класса
        """
        if class_type == 'Воин':
            return self._collection.filter_warriors()
        elif class_type == 'Маг':
            return self._collection.filter_mages()
        elif class_type == 'Лучник':
            return self._collection.filter_archers()
        else:
            raise InvalidClassTypeError(class_type)
    
    def filter_by_health(self, min_health: int = 50) -> List[Character]:
        """
        Фильтрация по здоровью
        
        Args:
            min_health: Минимальное здоровье для фильтрации
        
        Returns:
            Список персонажей со здоровьем выше порога
        """
        return self._collection.filter_healthy(min_health)
    
    def filter_by_power(self, min_power: int = 30) -> List[Character]:
        """
        Фильтрация по силе
        
        Args:
            min_power: Минимальная сила для фильтрации
        
        Returns:
            Список персонажей с силой выше порога
        """
        return self._collection.filter_powerful(min_power)
    
    def sort_characters(self, sort_by: str, reverse: bool = False) -> None:
        """
        Сортировка персонажей
        
        Args:
            sort_by: Поле для сортировки ('name', 'health', 'power', 'intelligence', 'stamina', 'class', 'power_rating', 'created_at')
            reverse: Сортировка в обратном порядке
        
        Raises:
            ValueError: Если указано неверное поле для сортировки
        """
        sort_methods = {
            'name': self._collection.sort_by_name,
            'health': self._collection.sort_by_health,
            'power': self._collection.sort_by_power,
            'intelligence': self._collection.sort_by_intelligence,
            'stamina': self._collection.sort_by_stamina,
            'class': self._collection.sort_by_class,
            'power_rating': self._collection.sort_by_power_rating,
            'created_at': self._collection.sort_by_created_at
        }
        
        if sort_by not in sort_methods:
            raise ValueError(f"Неверное поле для сортировки: {sort_by}. "
                           f"Доступные: {', '.join(sort_methods.keys())}")
        
        sort_methods[sort_by](reverse)
    
    def get_stats(self) -> dict:
        """
        Получить статистику по коллекции
        
        Returns:
            Словарь со статистикой
        """
        characters = self._collection.get_all()
        
        if not characters:
            return {
                'total': 0,
                'avg_health': 0,
                'avg_power': 0,
                'avg_intelligence': 0,
                'warriors': 0,
                'mages': 0,
                'archers': 0
            }
        
        total_health = sum(c.health for c in characters)
        total_power = sum(c.power for c in characters)
        total_intelligence = sum(c.intelligence for c in characters)
        
        warriors = len(self._collection.filter_warriors())
        mages = len(self._collection.filter_mages())
        archers = len(self._collection.filter_archers())
        
        return {
            'total': len(characters),
            'avg_health': total_health / len(characters),
            'avg_power': total_power / len(characters),
            'avg_intelligence': total_intelligence / len(characters),
            'warriors': warriors,
            'mages': mages,
            'archers': archers
        }
    
    def clear_collection(self) -> None:
        """Очистить коллекцию"""
        self._collection.clear()