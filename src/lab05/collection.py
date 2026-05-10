from typing import Callable, List, Optional, Any
from copy import deepcopy
from model import Character, Warrior, Mage, Archer

class CharacterCollection:
    
    def __init__(self, characters=None):
        if characters is None:
            self._characters = []
        else:
            self._characters = characters.copy()
    
    def _check_type(self, character):
        if not isinstance(character, Character):
            raise TypeError(f"Ошибка! Ожидается объект Character, получен {type(character).__name__}")
    
    # Основные методы
    
    def add(self, character):
        self._check_type(character)
        if character in self._characters:
            raise ValueError('Персонаж уже был добавлен')
        self._characters.append(character)
    
    def remove(self, character):
        self._check_type(character)
        self._characters.remove(character)
    
    def remove_at(self, index):
        if 0 <= index < len(self._characters):
            return self._characters.pop(index)
        raise IndexError(f"Индекс не попадает в диапазон от 0 до {len(self._characters)}")
    
    def get_all(self):
        "Вернуть всех персонажей."
        return self._characters.copy()
    
    def clear(self):
        "Очистить коллекцию."
        self._characters.clear()
    
    def copy(self):
        "Создать копию коллекции."
        return CharacterCollection(self._characters)
    
    # Методы поиска
    
    def find_by_name(self, name):
        for character in self._characters:
            if character.game_name.lower() == name.lower():
                return character
        return None
    
    def find_by_health_range(self, min_health=0, max_health=100):
        result = []
        for character in self._characters:
            if min_health <= character.health <= max_health:
                result.append(character)
        return result
    
    def find_by_power_range(self, min_power=1, max_power=60):
        result = []
        for character in self._characters:
            if min_power <= character.power <= max_power:
                result.append(character)
        return result
    
    # Фильтрация
    
    def get_healthy(self, min_health=50):
        new_collection = CharacterCollection()
        for character in self._characters:
            if character.health >= min_health:
                new_collection.add(character)
        return new_collection
    
    def get_strong(self, min_power=30):
        new_collection = CharacterCollection()
        for character in self._characters:
            if character.power >= min_power:
                new_collection.add(character)
        return new_collection
    
    # Методы сортировки
    
    def sort_by_name(self, reverse=False):
        self._characters.sort(key=lambda c: c.game_name.lower(), reverse=reverse)
        return self
    
    def sort_by_health(self, reverse=False):
        self._characters.sort(key=lambda c: c.health, reverse=reverse)
        return self
    
    def sort_by_power(self, reverse=False):
        self._characters.sort(key=lambda c: c.power, reverse=reverse)
        return self
    
    def sort_by_intelligence(self, reverse=False):
        self._characters.sort(key=lambda c: c.intelligence, reverse=reverse)
        return self
    
    def sort_by_stamina(self, reverse=False):
        self._characters.sort(key=lambda c: c.stamina, reverse=reverse)
        return self
    
    def sort_by_class(self, reverse=False):
        class_order = {"Воин": 1, "Маг": 2, "Лучник": 3}
        self._characters.sort(key=lambda c: class_order.get(c.get_class_type(), 4), reverse=reverse)
        return self
    
    def sort_by_power_rating(self, reverse=False):
        """Сортировка по рейтингу силы"""
        self._characters.sort(key=lambda c: c.calculate_power_rating(), reverse=reverse)
        return self
    
    def sort_by(self, key_func, reverse=False):
        "Универсальная сортировка"
        self._characters.sort(key=key_func, reverse=reverse)
        return self
    
    # Методы фильтрации
    
    def filter_by(self, predicate):
        "Фильтрация с переданным предикатом"
        self._characters = [c for c in self._characters if predicate(c)]
        return self
    
    def filter_warriors(self):
        self._characters = [c for c in self._characters if isinstance(c, Warrior)]
        return self
    
    def filter_mages(self):
        self._characters = [c for c in self._characters if isinstance(c, Mage)]
        return self
    
    def filter_archers(self):
        self._characters = [c for c in self._characters if isinstance(c, Archer)]
        return self
    
    def filter_healthy(self, threshold=50):
        self._characters = [c for c in self._characters if c.health > threshold]
        return self
    
    def filter_powerful(self, threshold=30):
        self._characters = [c for c in self._characters if c.power > threshold]
        return self
    
    
    def apply(self, func):
        "Применить функцию ко всем элементам"
        for character in self._characters:
            func(character)
        return self
    
    def map(self, func):
        "Преобразовать коллекцию с помощью функции"
        return list(map(func, self._characters))
    
    def get_names(self):
        return self.map(lambda c: c.game_name)
    
    def get_powers(self):
        return self.map(lambda c: c.power)
    
    
    def chain(self, *operations):
        """Выполнить цепочку операций"""
        result = self.copy()
        for operation in operations:
            result = operation(result)
        return result
    
    
    def __str__(self):
        if not self._characters:
            return "Коллекция пуста"
        result = f"Всего персонажей: {len(self._characters)}\n"
        result += "=" * 50 + "\n"
        for i, char in enumerate(self._characters, 1):
            result += f"{i}. {char.game_name} ({char.get_class_type()}) - "
            result += f"{char.health} {char.power} {char.intelligence}\n"
        return result
    
    def __len__(self):
        return len(self._characters)
    
    def __iter__(self):
        return iter(self._characters)
    
    def __getitem__(self, index):
        return self._characters[index]
    
    def __repr__(self):
        return f"CharacterCollection({self._characters})"