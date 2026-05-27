from abc import ABC, abstractmethod
from typing import List, Any, Protocol, Union
from datetime import datetime


class Displayable(Protocol):
    
    def display(self) -> str:
        """Возвращает строковое представление объекта"""
        ...


class Scorable(Protocol):
    """Протокол для объектов, которые имеют оценку/рейтинг"""
    def score(self) -> float:
        """Возвращает числовую оценку объекта"""
        ...


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


class Character(Printable, Comparable):
    """Базовый класс персонажа"""
    
    min_health: int = 0
    max_health: int = 100
    min_stamina: int = 0
    max_stamina: int = 40
    min_power: int = 1
    max_power: int = 60
    min_intelligence: int = 1
    max_intelligence: int = 80

    def __init__(self, game_name: str, health: Union[int, float], stamina: Union[int, float], 
                 power: Union[int, float], intelligence: Union[int, float]):
        # Валидация имени
        if isinstance(game_name, str):
            if game_name.strip():
                self._game_name: str = game_name.strip()
            else:
                raise ValueError('Ошибка! Имя не может быть пустым.')
        else:
            raise TypeError('Ошибка! Имя должно быть строкой.')
        
        # Валидация характеристик
        self._validate_health(health)
        self._validate_stamina(stamina)
        self._validate_power(power)
        self._validate_intelligence(intelligence)
        
        # Дата создания
        self._created_at: datetime = datetime.now()
    
    def _validate_health(self, value: Union[int, float]) -> None:
        """Валидация здоровья"""
        if isinstance(value, (int, float)):
            if self.min_health <= value <= self.max_health:
                self._health: Union[int, float] = value
            else:
                raise ValueError(f'Ошибка! Здоровье должно быть от {self.min_health} до {self.max_health}.')
        else:
            raise TypeError('Ошибка! Здоровье должно быть числом.')
    
    def _validate_stamina(self, value: Union[int, float]) -> None:
        """Валидация выносливости"""
        if isinstance(value, (int, float)):
            if self.min_stamina <= value <= self.max_stamina:
                self._stamina: Union[int, float] = value
            else:
                raise ValueError(f'Ошибка! Выносливость должна быть от {self.min_stamina} до {self.max_stamina}.')
        else:
            raise TypeError('Ошибка! Выносливость должна быть числом.')
    
    def _validate_power(self, value: Union[int, float]) -> None:
        """Валидация силы"""
        if isinstance(value, (int, float)):
            if self.min_power <= value <= self.max_power:
                self._power: Union[int, float] = value
            else:
                raise ValueError(f'Ошибка! Сила должна быть от {self.min_power} до {self.max_power}.')
        else:
            raise TypeError('Ошибка! Сила должна быть числом.')
    
    def _validate_intelligence(self, value: Union[int, float]) -> None:
        """Валидация интеллекта"""
        if isinstance(value, (int, float)):
            if self.min_intelligence <= value <= self.max_intelligence:
                self._intelligence: Union[int, float] = value
            else:
                raise ValueError(f'Ошибка! Интеллект должен быть от {self.min_intelligence} до {self.max_intelligence}.')
        else:
            raise TypeError('Ошибка! Интеллект должен быть числом.')
    
    @property
    def game_name(self) -> str:
        return self._game_name
    
    @property 
    def health(self) -> Union[int, float]:
        return self._health
    
    @property 
    def stamina(self) -> Union[int, float]:
        return self._stamina
    
    @property
    def power(self) -> Union[int, float]:
        return self._power
    
    @property 
    def intelligence(self) -> Union[int, float]:
        return self._intelligence
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    @game_name.setter
    def game_name(self, value: str) -> None:
        if isinstance(value, str):
            if value.strip():
                self._game_name = value.strip()
            else:
                raise ValueError('Ошибка! Имя персонажа не может быть пустым.')
        else:
            raise TypeError('Ошибка! Имя персонажа должно быть строкой.')
    
    @health.setter
    def health(self, value: Union[int, float]) -> None:
        self._validate_health(value)
    
    @stamina.setter
    def stamina(self, value: Union[int, float]) -> None:
        self._validate_stamina(value)
    
    @power.setter
    def power(self, value: Union[int, float]) -> None:
        self._validate_power(value)
    
    @intelligence.setter
    def intelligence(self, value: Union[int, float]) -> None:
        self._validate_intelligence(value)
    
    def attack(self, target: 'Character') -> str:
        """Атака персонажа"""
        if not isinstance(target, Character):
            raise TypeError('Ошибка! Можно атаковать только другого персонажа.')
        if self._stamina < 5:
            return f"{self._game_name} слишком устал для атаки"
        
        damage = self._power * 2
        target.health = max(0, target.health - damage)
        self._stamina -= 5

        return (f"{self._game_name} атакует {target.game_name} "
                f"и наносит {damage} урона.")

    def magic_attack(self, target: 'Character') -> str:
        """Магическая атака персонажа"""
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
    
    def get_class_type(self) -> str:
        """Возвращает тип класса"""
        return "Обычный персонаж"
    
    def calculate_power_rating(self) -> float:
        """Расчет рейтинга силы персонажа"""
        return (self._power * 0.5 + self._intelligence * 0.3 + (self._health / 100) * 20)
    
    def is_available_for_fight(self) -> bool:
        """Проверка, готов ли персонаж к бою"""
        return self._health > 20 and self._stamina > 10
    
    def to_string(self) -> str:
        """Реализация интерфейса Printable"""
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
    
    def compare_to(self, other: 'Character') -> int:
        """Реализация интерфейса Comparable"""
        if not isinstance(other, Character):
            raise TypeError(f"Невозможно сравнить Character с {type(other)}")
        if self._game_name < other._game_name:
            return -1
        elif self._game_name > other._game_name:
            return 1
        return 0
    
    def __str__(self) -> str:
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

    def __repr__(self) -> str:
        return (f"Character(game_name='{self._game_name}', "
                f"health={self._health}, stamina={self._stamina}, "
                f"power={self._power}, intelligence={self._intelligence})")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Character):
            return NotImplemented
        return self._game_name == other._game_name


class Warrior(Character, PowerRatable):
    """Класс Воин - наследник Character"""
    
    def __init__(self, game_name: str, health: Union[int, float], stamina: Union[int, float], 
                 power: Union[int, float], intelligence: Union[int, float], 
                 weapon: str, armor_rating: int):
        super().__init__(game_name, health, stamina, power, intelligence)
        self.weapon: str = weapon
        self.armor_rating: int = armor_rating
        self.rage: int = 0
    
    def berserker_rage(self) -> str:
        """Ярость берсерка"""
        if self.stamina < 15:
            return f"{self.game_name} слишком устал для ярости!"
        self.rage += 25
        self.stamina -= 15
        return f"{self.game_name} впадает в ярость!"
    
    def attack(self, target: Character) -> str:
        """Переопределенный метод атаки воина"""
        if not isinstance(target, Character):
            raise TypeError('Ошибка!')
        if self.stamina < 5:
            return f"{self.game_name} слишком устал"
        
        damage = (self.power * 2) + 10
        target.health = max(0, target.health - damage)
        self.stamina -= 5
        
        return f"{self.game_name} атакует {target.game_name} и наносит {damage} урона!"
    
    def get_power_rating(self) -> float:
        """Реализация интерфейса PowerRatable"""
        return self.power * 0.7 + self.armor_rating * 0.3
    
    def get_class_type(self) -> str:
        return "Воин"
    
    def __str__(self) -> str:
        return (f"{self.game_name} (Воин)\n"
                f"  Здоровье: {self.health}\n"
                f"  Сила: {self.power}\n"
                f"  Оружие: {self.weapon}\n"
                f"  Броня: {self.armor_rating}")


class Mage(Character, PowerRatable):
    """Класс Маг - наследник Character"""
    
    def __init__(self, game_name: str, health: Union[int, float], stamina: Union[int, float], 
                 power: Union[int, float], intelligence: Union[int, float], 
                 magic_school: str, mana: int):
        super().__init__(game_name, health, stamina, power, intelligence)
        self.magic_school: str = magic_school
        self.mana: int = mana
        self.spells: List[str] = []
    
    def learn_spell(self, spell_name: str) -> str:
        """Изучить заклинание"""
        self.spells.append(spell_name)
        return f"{self.game_name} выучил {spell_name}!"
    
    def magic_attack(self, target: Character) -> str:
        """Переопределенный метод магической атаки мага"""
        if self.mana < 20:
            return f"{self.game_name} не хватает маны!"
        damage = self.intelligence * 2
        target.health = max(0, target.health - damage)
        self.mana -= 20
        return f"{self.game_name} наносит {damage} магического урона!"
    
    def get_power_rating(self) -> float:
        """Реализация интерфейса PowerRatable"""
        return self.intelligence * 0.8 + len(self.spells) * 5
    
    def get_class_type(self) -> str:
        return "Маг"
    
    def __str__(self) -> str:
        return f"{self.game_name} (Маг)\n  Интеллект: {self.intelligence}\n  Мана: {self.mana}"


class Archer(Character):
    """Класс Лучник - наследник Character"""
    
    def __init__(self, game_name: str, health: Union[int, float], stamina: Union[int, float], 
                 power: Union[int, float], intelligence: Union[int, float], 
                 bow_type: str, accuracy: int):
        super().__init__(game_name, health, stamina, power, intelligence)
        self.bow_type: str = bow_type
        self.accuracy: int = accuracy
        self.arrows: int = 20
    
    def aimed_shot(self, target: Character) -> str:
        """Прицельный выстрел"""
        if self.arrows < 1:
            return "Нет стрел!"
        damage = self.power * 4
        self.arrows -= 1
        target.health = max(0, target.health - damage)
        return f"{self.game_name} наносит {damage} урона прицельным выстрелом!"
    
    def get_class_type(self) -> str:
        return "Лучник"
    
    def __str__(self) -> str:
        return f"{self.game_name} (Лучник)\n  Сила: {self.power}\n  Точность: {self.accuracy}%"


class CharacterCollection:
    """Коллекция для хранения и управления объектами Character"""
    
    def __init__(self, characters: List[Character] = None):
        if characters is None:
            self._characters: List[Character] = []
        else:
            self._characters = characters.copy()
    
    def _check_type(self, character: Character) -> None:
        """Проверка типа добавляемого объекта"""
        if not isinstance(character, Character):
            raise TypeError(f"Ошибка! Ожидается объект Character, получен {type(character).__name__}")
    
    def add(self, character: Character) -> None:
        """Добавить персонажа в коллекцию"""
        self._check_type(character)
        if character in self._characters:
            raise ValueError('Персонаж уже был добавлен')
        self._characters.append(character)
    
    def remove(self, character: Character) -> None:
        """Удалить персонажа"""
        self._check_type(character)
        self._characters.remove(character)
    
    def remove_at(self, index: int) -> Character:
        """Удалить по индексу"""
        if 0 <= index < len(self._characters):
            return self._characters.pop(index)
        raise IndexError(f"Индекс не попадает в диапазон от 0 до {len(self._characters)}")
    
    def get_all(self) -> List[Character]:
        """Вернуть всех персонажей"""
        return self._characters.copy()
    
    def clear(self) -> None:
        """Очистить коллекцию"""
        self._characters.clear()
    
    def copy(self) -> 'CharacterCollection':
        """Создать копию коллекции"""
        return CharacterCollection(self._characters)
    
    def find_by_name(self, name: str) -> Character:
        """Поиск персонажа по имени"""
        for character in self._characters:
            if character.game_name.lower() == name.lower():
                return character
        return None
    
    def find_by_health_range(self, min_health: int = 0, max_health: int = 100) -> List[Character]:
        """Поиск персонажей в заданном диапазоне здоровья"""
        result = []
        for character in self._characters:
            if min_health <= character.health <= max_health:
                result.append(character)
        return result
    
    def find_by_power_range(self, min_power: int = 1, max_power: int = 60) -> List[Character]:
        """Поиск персонажей в заданном диапазоне силы"""
        result = []
        for character in self._characters:
            if min_power <= character.power <= max_power:
                result.append(character)
        return result
    
    def filter_warriors(self) -> List[Character]:
        """Фильтрация воинов"""
        return [c for c in self._characters if isinstance(c, Warrior)]
    
    def filter_mages(self) -> List[Character]:
        """Фильтрация магов"""
        return [c for c in self._characters if isinstance(c, Mage)]
    
    def filter_archers(self) -> List[Character]:
        """Фильтрация лучников"""
        return [c for c in self._characters if isinstance(c, Archer)]
    
    def filter_healthy(self, threshold: int = 50) -> List[Character]:
        """Фильтрация здоровых персонажей"""
        return [c for c in self._characters if c.health > threshold]
    
    def filter_powerful(self, threshold: int = 30) -> List[Character]:
        """Фильтрация сильных персонажей"""
        return [c for c in self._characters if c.power > threshold]
    
    def sort_by_name(self, reverse: bool = False) -> 'CharacterCollection':
        """Сортировка по имени"""
        self._characters.sort(key=lambda c: c.game_name.lower(), reverse=reverse)
        return self
    
    def sort_by_health(self, reverse: bool = False) -> 'CharacterCollection':
        """Сортировка по здоровью"""
        self._characters.sort(key=lambda c: c.health, reverse=reverse)
        return self
    
    def sort_by_power(self, reverse: bool = False) -> 'CharacterCollection':
        """Сортировка по силе"""
        self._characters.sort(key=lambda c: c.power, reverse=reverse)
        return self
    
    def sort_by_intelligence(self, reverse: bool = False) -> 'CharacterCollection':
        """Сортировка по интеллекту"""
        self._characters.sort(key=lambda c: c.intelligence, reverse=reverse)
        return self
    
    def sort_by_stamina(self, reverse: bool = False) -> 'CharacterCollection':
        """Сортировка по выносливости"""
        self._characters.sort(key=lambda c: c.stamina, reverse=reverse)
        return self
    
    def sort_by_class(self, reverse: bool = False) -> 'CharacterCollection':
        """Сортировка по классу"""
        class_order = {"Воин": 1, "Маг": 2, "Лучник": 3}
        self._characters.sort(key=lambda c: class_order.get(c.get_class_type(), 4), reverse=reverse)
        return self
    
    def sort_by_power_rating(self, reverse: bool = False) -> 'CharacterCollection':
        """Сортировка по рейтингу силы"""
        self._characters.sort(key=lambda c: c.calculate_power_rating(), reverse=reverse)
        return self
    
    def sort_by_created_at(self, reverse: bool = False) -> 'CharacterCollection':
        """Сортировка по дате создания"""
        self._characters.sort(key=lambda c: c.created_at, reverse=reverse)
        return self
    
    def __len__(self) -> int:
        return len(self._characters)
    
    def __iter__(self):
        return iter(self._characters)
    
    def __getitem__(self, index: int) -> Character:
        return self._characters[index]
    
    def __str__(self) -> str:
        if not self._characters:
            return "Коллекция пуста"
        result = f"┌{'=' * 68}┐\n"
        result += f"│{' ' * 25}КОЛЛЕКЦИЯ ПЕРСОНАЖЕЙ{' ' * 25}│\n"
        result += f"├{'=' * 68}┤\n"
        for i, char in enumerate(self._characters, 1):
            result += f"│ {i:2}. {char.game_name:<20} [{char.get_class_type():^10}] "
            result += f"HP:{char.health:3} PWR:{char.power:2} INT:{char.intelligence:2} │\n"
        result += f"└{'=' * 68}┘"
        result += f"\nВсего персонажей: {len(self._characters)}"
        return result


# Точка входа для тестирования
if __name__ == '__main__':
    # Создаем несколько персонажей для тестирования
    char1 = Character("Тестовый", 80, 30, 40, 50)
    warrior = Warrior("Громобой", 95, 35, 55, 20, "Двуручный меч", 8)
    mage = Mage("Мерлин", 60, 25, 15, 75, "Огня", 150)
    archer = Archer("Леголас", 75, 30, 45, 40, "Длинный лук", 90)
    
    # Создаем коллекцию и добавляем персонажей
    collection = CharacterCollection()
    collection.add(char1)
    collection.add(warrior)
    collection.add(mage)
    collection.add(archer)
    
    print("Тестовый вывод коллекции:")
    print(collection)