from base import Character

from models import Warrior, Mage, Archer


class CharacterCollection:
    def __init__(self):
        """Инициализация пустой коллекции"""
        self._characters = []

    def _check_type(self, character):
        """проверка типа добавляемого объекта"""
        if not isinstance(character, Character):
            raise TypeError(f"Ошибка! Ожидается объект Character, получен {type(character).__name__}")
    
    # Основные методы
    def add(self, character):
        """добавить персонажа в коллекцию"""
        self._check_type(character)
        if character in self._characters:
            raise ValueError('Персонаж уже был добавлен')
        self._characters.append(character)

    def remove(self, character):
        """удалить персонажа"""
        self._check_type(character)
        self._characters.remove(character)

    def remove_at(self, index):
        """удалить по индексу"""
        if 0 <= index < len(self._characters):
            return self._characters.pop(index)
        raise IndexError(f"Индекс не попадает в диапазон от 0 до {len(self._characters)}")
    
    def get_all(self):
        """получить всех персонажей"""
        return self._characters.copy()
    
    # Методы поиска
    def find_by_name(self, name: str):
        """поиск персонажа по имени"""
        for character in self._characters:
            if character.game_name.lower() == name.lower():
                return character
        return None
    
    def find_by_health_range(self, min_health: int = 0, max_health: int = 100):
        """поиск персонажей в заданном диапазоне здоровья"""
        result = []
        for character in self._characters:
            if min_health <= character.health <= max_health:
                result.append(character)
        return result
    



    # Фильтрация по типу (isinstance)
    def get_warriors(self):
        """Получить только воинов"""
        result = CharacterCollection()
        for character in self._characters:
            if isinstance(character, Warrior):
                result.add(character)
        return result
    
    def get_mages(self):
        """Получить только магов"""
        result = CharacterCollection()
        for character in self._characters:
            if isinstance(character, Mage):
                result.add(character)
        return result
    
    def get_archers(self):
        """Получить только лучников"""
        result = CharacterCollection()
        for character in self._characters:
            if isinstance(character, Archer):
                result.add(character)
        return result
    
    def get_by_type(self, class_type):
        """Фильтрация по типу класса"""
        result = CharacterCollection()
        for character in self._characters:
            if character.get_class_type() == class_type:
                result.add(character)
        return result
    
    # Фильтрация по состоянию
    def get_active_for_fight(self):
        """Получить персонажей, готовых к бою (полиморфизм)"""
        result = CharacterCollection()
        for character in self._characters:
            if character.is_available_for_fight():
                result.add(character)
        return result
    
    def get_healthy(self, min_health: int = 50):
        """возвращает новую коллекцию с здоровыми персонажами"""
        new_collection = CharacterCollection()
        for character in self._characters:
            if character.health >= min_health:
                new_collection.add(character)
        return new_collection
    
    def get_strong(self, min_power: int = 30):
        """возвращает новую коллекцию с сильными персонажами"""
        new_collection = CharacterCollection()
        for character in self._characters:
            if character.power >= min_power:
                new_collection.add(character)
        return new_collection
    
    # Сортировка с использованием полиморфного метода
    def sort_by_power_rating(self, reverse=True):
        """Сортировка по рейтингу силы (полиморфное поведение)"""
        self._characters.sort(key=lambda c: c.calculate_power_rating(), reverse=reverse)
    
    def sort_by_name(self, reverse=False):
        """Сортировка по имени"""
        self._characters.sort(key=lambda c: c.game_name.lower(), reverse=reverse)
    
    def sort_by_power(self, reverse=False):
        """Сортировка по силе"""
        self._characters.sort(key=lambda c: c.power, reverse=reverse)
    
    # Статистика
    def get_average_power_rating(self):
        """Средний рейтинг силы (полиморфизм)"""
        if not self._characters:
            return 0
        total = sum(c.calculate_power_rating() for c in self._characters)
        return total / len(self._characters)
    
    def get_total_special_bonus(self):
        """Суммарный специальный бонус всех персонажей"""
        return sum(c.get_special_bonus() for c in self._characters)
    
    # Магические методы
    def __str__(self):
        """строковое представление коллекции для пользователей"""
        if not self._characters:
            return "Коллекция пуста"
        result = f"Всего персонажей: {len(self._characters)}\n"
        result += "=" * 50 + "\n"
        for char in self._characters:
            result += str(char) + "\n"
            result += "-" * 30 + "\n"
        return result
    
    def __len__(self):
        return len(self._characters)
    
    def __iter__(self):
        return iter(self._characters)
    
    def __getitem__(self, index):
        return self._characters[index]