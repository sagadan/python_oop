from interfaces import Printable, Comparable, PowerRatable
from typing import List, Any
import functools


class Character(Printable, Comparable):
    """Базовый класс персонажа, реализующий интерфейсы Printable и Comparable"""
    
    min_health = 0
    max_health = 100
    min_stamina = 0
    max_stamina = 40
    min_power = 1
    max_power = 60
    min_intelligence = 1
    max_intelligence = 80

    def __init__(self, game_name: str, health: int, stamina: int, power: int, intelligence: int):
        if isinstance(game_name, str): 
            if game_name.strip():
                self._game_name = game_name.strip()
            else:
                raise ValueError('Ошибка! Имя не может быть пустым.')
        else:
            raise TypeError('Ошибка! Имя должно быть строкой.')
        
        if isinstance(health, (int, float)):
            if self.min_health <= health <= self.max_health:  
                self._health = health 
            else:
                raise ValueError(f'Ошибка! Здоровье должно быть от {self.min_health} до {self.max_health}.')
        else:
            raise TypeError('Ошибка! Здоровье должно быть числом.')
        
        if isinstance(stamina, (int, float)):
            if self.min_stamina <= stamina <= self.max_stamina:  
                self._stamina = stamina
            else:
                raise ValueError(f'Ошибка! Выносливость должна быть от {self.min_stamina} до {self.max_stamina}.')
        else:
            raise TypeError('Ошибка! Выносливость должна быть числом.')
        
        if isinstance(power, (int, float)):
            if self.min_power <= power <= self.max_power:  
                self._power = power
            else:
                raise ValueError(f'Ошибка! Сила должна быть от {self.min_power} до {self.max_power}.')
        else:
            raise TypeError('Ошибка! Сила должна быть числом.')
        
        if isinstance(intelligence, (int, float)):
            if self.min_intelligence <= intelligence <= self.max_intelligence:  
                self._intelligence = intelligence
            else:
                raise ValueError(f'Ошибка! Интеллект должен быть от {self.min_intelligence} до {self.max_intelligence}.')
    
    @property
    def game_name(self):
        return self._game_name
    
    @property 
    def health(self):
        return self._health
    
    @property 
    def stamina(self):
        return self._stamina
    
    @property
    def power(self):
        return self._power
    
    @property 
    def intelligence(self):
        return self._intelligence
    
    @game_name.setter
    def game_name(self, value):
        if isinstance(value, str):
            if value.strip():
                self._game_name = value.strip()
            else:
                raise ValueError('Ошибка! Имя персонажа не может быть пустым.')
        else:
            raise TypeError('Ошибка! Имя персонажа должно быть строкой.')
    
    @health.setter
    def health(self, value):
        if isinstance(value, (int, float)):
            if self.min_health <= value <= self.max_health:  
                self._health = value
            else:
                raise ValueError(f'Ошибка! Здоровье должно быть от {self.min_health} до {self.max_health}.')
        else:
            raise TypeError('Ошибка! Здоровье должно быть числом.')
    
    @stamina.setter
    def stamina(self, value):
        if isinstance(value, (int, float)):
            if self.min_stamina <= value <= self.max_stamina:  
                self._stamina = value
            else:
                raise ValueError(f'Ошибка! Выносливость должна быть от {self.min_stamina} до {self.max_stamina}.')
        else:
            raise TypeError('Ошибка! Выносливость должна быть числом.')
    
    @power.setter
    def power(self, value):
        if isinstance(value, (int, float)):
            if self.min_power <= value <= self.max_power:  
                self._power = value
            else:
                raise ValueError(f'Ошибка! Сила должна быть от {self.min_power} до {self.max_power}.')
        else:
            raise TypeError('Ошибка! Сила должна быть числом.')
    
    @intelligence.setter
    def intelligence(self, value):
        if isinstance(value, (int, float)):
            if self.min_intelligence <= value <= self.max_intelligence:  
                self._intelligence = value
            else:
                raise ValueError(f'Ошибка! Интеллект должен быть от {self.min_intelligence} до {self.max_intelligence}.')
        else:
            raise TypeError('Ошибка! Интеллект должен быть числом.')
    
    def attack(self, target):
        if not isinstance(target, Character):  
            raise TypeError('Ошибка! Можно атаковать только другого персонажа.')
        if self._stamina < 5:
            return f"{self._game_name} слишком устал для атаки"
        
        damage = self._power * 2
        target.health = max(0, target.health - damage)
        self._stamina -= 5

        return (f"{self._game_name} атакует {target.game_name} "
                f"и наносит {damage} урона.")

    def magic_attack(self, target):
        if not isinstance(target, Character):  
            raise TypeError('Ошибка! Можно атаковать только другого персонажа.')
        if self._stamina < 8:
            return f"{self._game_name} слишком устал для магии."
        if self._intelligence < 10:
            return f"{self._game_name} недостаточно умен для магии."
        
        magic_damage = self._intelligence * 2
        target.health = max(0, target.health - magic_damage)
        self._stamina -= 8
        
        return (f"{self._game_name} произносит заклинание на {target.game_name} "
                f"и наносит {magic_damage} магического урона!")
    
    # Реализация интерфейса Printable
    def to_string(self) -> str:
        health_percent = (self._health / 100) * 100 

        if self._health > 80:
            health_status = 'Здоров'
        elif self._health > 50:
            health_status = 'Слегка ранен' 
        elif self._health > 20:  
            health_status = 'Сильно ранен'
        else:
            health_status = 'Почти мертв'
        
        return (f"{self._game_name} [{health_status}] | "
                f"HP: {self._health}/100 | STA: {self._stamina}/40 | "
                f"PWR: {self._power}/60 | INT: {self._intelligence}/80")
    
    # Реализация интерфейса Comparable
    def compare_to(self, other: 'Character') -> int:
        if not isinstance(other, Character):
            raise TypeError(f"Невозможно сравнить Character с {type(other)}")
        if self._game_name < other._game_name:
            return -1
        elif self._game_name > other._game_name:
            return 1
        return 0
    
    def __str__(self):
        health_percent = (self._health / 100) * 100 

        if self._health > 80:
            health_status = 'Здоров'
        elif self._health > 50:
            health_status = 'Слегка ранен' 
        elif self._health > 20:  
            health_status = 'Сильно ранен'
        else:
            health_status = 'Почти мертв'
        
        return (f" {self._game_name} [{health_status}]\n"
                f"   Здоровье: {self._health}/100 ({health_percent:.1f}%)\n"
                f"   Выносливость: {self._stamina}/40\n"
                f"   Сила: {self._power}/60\n"
                f"   Интеллект: {self._intelligence}/80")
    
    def __repr__(self):
        return (f"Character(game_name='{self._game_name}', "
                f"health={self._health}, stamina={self._stamina}, "
                f"power={self._power}, intelligence={self._intelligence})")

    def __eq__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        return self._game_name == other._game_name


# Класс воин

class Warrior(Character, PowerRatable):
    
    def __init__(self, game_name, health, stamina, power, intelligence, weapon, armor_rating):
        super().__init__(game_name, health, stamina, power, intelligence)
        self.weapon = weapon
        self.armor_rating = armor_rating
        self.rage = 0
    
    def berserker_rage(self):
        if self.stamina < 15:
            return f"{self.game_name} слишком устал для ярости!"
        self.rage += 25
        self.stamina -= 15
        return f"{self.game_name} впадает в ярость!"
    
    def attack(self, target):
        if not isinstance(target, Character):
            raise TypeError('Ошибка!')
        if self.stamina < 5:
            return f"{self.game_name} слишком устал"
        
        damage = (self.power * 2) + 10
        target.health = max(0, target.health - damage)
        self.stamina -= 5
        
        return f"{self.game_name} атакует {target.game_name} и наносит {damage} урона!"
    
    def get_power_rating(self) -> float:
        return self.power * 0.7 + self.armor_rating * 0.3
    
    def to_string(self) -> str:
        return f" {self.game_name} [Воин] | Оружие: {self.weapon} | Броня: {self.armor_rating} | Рейтинг силы: {self.get_power_rating():.1f}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Character):
            raise TypeError(f"Невозможно сравнить Warrior с {type(other)}")
        if hasattr(other, 'get_power_rating'):
            rating1 = self.get_power_rating()
            rating2 = other.get_power_rating()
            if rating1 < rating2:
                return -1
            elif rating1 > rating2:
                return 1
            return 0
        return super().compare_to(other)
    
    def get_class_type(self):
        return "Воин"
    
    def __str__(self):
        return (f"{self.game_name} (Воин)\n"
                f"  Здоровье: {self.health}\n"
                f"  Сила: {self.power}\n"
                f"  Оружие: {self.weapon}\n"
                f"  Броня: {self.armor_rating}")


# Класс маг

class Mage(Character, PowerRatable):
    
    def __init__(self, game_name, health, stamina, power, intelligence, magic_school, mana):
        super().__init__(game_name, health, stamina, power, intelligence)
        self.magic_school = magic_school
        self.mana = mana
        self.spells = []
    
    def learn_spell(self, spell_name):
        self.spells.append(spell_name)
        return f"{self.game_name} выучил {spell_name}!"
    
    def magic_attack(self, target):
        if self.mana < 20:
            return f"{self.game_name} не хватает маны!"
        damage = self.intelligence * 2
        target.health = max(0, target.health - damage)
        self.mana -= 20
        return f"{self.game_name} наносит {damage} магического урона!"
    
    def get_power_rating(self) -> float:
        return self.intelligence * 0.8 + len(self.spells) * 5
    
    def to_string(self) -> str:
        return f" {self.game_name} [Маг] | Школа: {self.magic_school} | Мана: {self.mana} | Заклинаний: {len(self.spells)} | Рейтинг: {self.get_power_rating():.1f}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Character):
            raise TypeError(f"Невозможно сравнить Mage с {type(other)}")
        if self.intelligence < other.intelligence:
            return -1
        elif self.intelligence > other.intelligence:
            return 1
        return 0
    
    def get_class_type(self):
        return "Маг"
    
    def __str__(self):
        return f"{self.game_name} (Маг)\n  Интеллект: {self.intelligence}\n  Мана: {self.mana}"


# Класс лучник

class Archer(Character):
    
    def __init__(self, game_name, health, stamina, power, intelligence, bow_type, accuracy):
        super().__init__(game_name, health, stamina, power, intelligence)
        self.bow_type = bow_type
        self.accuracy = accuracy
        self.arrows = 20
    
    def aimed_shot(self, target):
        if self.arrows < 1:
            return "Нет стрел!"
        damage = self.power * 4
        self.arrows -= 1
        target.health = max(0, target.health - damage)
        return f"{self.game_name} наносит {damage} урона прицельным выстрелом!"
    
    def to_string(self) -> str:
        return f" {self.game_name} [Лучник] | Лук: {self.bow_type} | Точность: {self.accuracy}% | Стрелы: {self.arrows}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Character):
            raise TypeError(f"Невозможно сравнить Archer с {type(other)}")
        if hasattr(other, 'accuracy'):
            if self.accuracy < other.accuracy:
                return -1
            elif self.accuracy > other.accuracy:
                return 1
            return 0
        return super().compare_to(other)
    
    def calculate_power_rating(self):
        return self.power * 0.6 + self.accuracy * 0.4
    
    def get_class_type(self):
        return "Лучник"
    
    def __str__(self):
        return f"{self.game_name} (Лучник)\n  Сила: {self.power}\n  Точность: {self.accuracy}%"


# Коллекция персонажей

class CharacterCollection:
    "Коллекция для хранения и управления объектами Character"
    
    def __init__(self):
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
        return self._characters.copy()
    
    # Фильтрация по интерфейсам
    def get_printable(self) -> List[Printable]:
        """Возвращает список объектов, реализующих интерфейс Printable"""
        return [char for char in self._characters if isinstance(char, Printable)]
    
    def get_comparable(self) -> List[Comparable]:
        """Возвращает список объектов, реализующих интерфейс Comparable"""
        return [char for char in self._characters if isinstance(char, Comparable)]
    
    def get_power_ratable(self) -> List[PowerRatable]:
        """Возвращает список объектов, реализующих интерфейс PowerRatable"""
        return [char for char in self._characters if isinstance(char, PowerRatable)]
    
    def filter_by_interface(self, interface_type) -> List:
        """Универсальная фильтрация по интерфейсу"""
        return [char for char in self._characters if isinstance(char, interface_type)]
    
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
    
    def find_by_power_range(self, min_power: int = 1, max_power: int = 60):
        """поиск персонажей в заданном диапазоне силы"""
        result = []
        for character in self._characters:
            if min_power <= character.power <= max_power:
                result.append(character)
        return result 
    
    # Фильтрация
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
    
    # Сортировка
    def sort_by_name(self, reverse=False):
        """Сортировка по имени"""
        self._characters.sort(key=lambda c: c.game_name.lower(), reverse=reverse)
    
    def sort_by_power(self, reverse=False):
        """Сортировка по силе"""
        self._characters.sort(key=lambda c: c.power, reverse=reverse)
    
    def sort_by_comparable(self, reverse: bool = False):
        """Сортировка коллекции с использованием метода compare_to"""
        def compare_func(a, b):
            if isinstance(a, Comparable) and isinstance(b, Comparable):
                return a.compare_to(b)
            return 0
        
        self._characters.sort(key=functools.cmp_to_key(compare_func), reverse=reverse)
    
    # Магические методы
    def __str__(self):
        """строковое представление коллекции для пользователей"""
        result = ""
        for char in self._characters:
            result += str(char) + "\n"
        return result
        
    def __len__(self):
        """возвращает количество персонажей в коллекции"""
        return len(self._characters)
    
    def __iter__(self):
        """возвращает итератор по коллекции"""
        return iter(self._characters)
    
    def __getitem__(self, index):
        """доступ к персонажу по индексу"""
        return self._characters[index]