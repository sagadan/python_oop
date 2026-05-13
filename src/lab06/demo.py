from container import TypedCollection
from typing import List


# Классы с аннотациями типов (ЛР-1) 

class Character:
    "Базовый класс персонажа с аннотациями типов"
    
    def __init__(self, game_name: str, health: int, power: int) -> None:
        self._game_name: str = game_name
        self._health: int = health
        self._power: int = power
    
    @property
    def game_name(self) -> str:
        return self._game_name
    
    @property
    def health(self) -> int:
        return self._health
    
    @property
    def power(self) -> int:
        return self._power
    
    # Методы для протоколов (без наследования!)
    def display(self) -> str:
        "Для Displayable протокола"
        return f"{self._game_name} ({self._health})"
    
    def score(self) -> float:
        "Для Scorable протокола"
        return self._power * 0.7 + (self._health / 100) * 30
    
    def __str__(self) -> str:
        return f"{self._game_name}: {self._power}"


# Классы из ЛР-3 (иерархия, тоже имеют display и score)
class Warrior(Character):
    def __init__(self, game_name: str, health: int, power: int, weapon: str) -> None:
        super().__init__(game_name, health, power)
        self.weapon: str = weapon
    
    def display(self) -> str:
        return f"{self.game_name} (Воин) с {self.weapon}"
    
    def score(self) -> float:
        return self.power * 0.9 + 10


class Mage(Character):
    def __init__(self, game_name: str, health: int, power: int, mana: int) -> None:
        super().__init__(game_name, health, power)
        self.mana: int = mana
    
    def display(self) -> str:
        return f"{self.game_name} (Маг) мана:{self.mana}"
    
    def score(self) -> float:
        return self.power * 0.6 + self.mana * 0.2


# Демонстрация

def main() -> None:
    
    coll: TypedCollection[Character] = TypedCollection()
    
    # Создаем персонажей
    char1 = Character("Артур", 100, 50)
    char2 = Character("Мерлин", 80, 30)
    char3 = Character("Ланселот", 95, 55)
    
    # Добавляем персонажей
    coll.add(char1)
    coll.add(char2)
    coll.add(char3)
    print(f"Добавлено {len(coll)} персонажей")
    
    # Демонстрация проверки типов - создаем отдельную коллекцию для теста
    print("\nПроверка типов (демонстрация работы TypeVar):")
    test_coll: TypedCollection[Character] = TypedCollection()
    try:
        # Пытаемся добавить строку
        test_coll.add("Не персонаж")  # type: ignore
        print("Ошибка: строка добавилась (это баг в runtime проверке)")
    except TypeError as e:
        print(f"TypeError: {e}")
    except AttributeError:
        print("Ошибка: нет метода add с проверкой типа")
    
    # Показываем, что основная коллекция не пострадала
    print(f"\nВсе персонажи в основной коллекции: {[c.game_name for c in coll.get_all()]}")
    
    
    # find - найден
    found = coll.find(lambda c: c.game_name == "Мерлин")
    print(f"find('Мерлин'): {found.game_name if found else None}")
    
    # find - не найден
    not_found = coll.find(lambda c: c.game_name == "Гендальф")
    print(f"find('Гендальф'): {not_found}")
    
    # filter
    strong = coll.filter(lambda c: c.power > 40)
    print(f"filter(сила > 40): {[c.game_name for c in strong]}")
    
    # map - демонстрация изменения типа результата
    names: List[str] = coll.map(lambda c: c.game_name)
    powers: List[int] = coll.map(lambda c: c.power)
    ratings: List[float] = coll.map(lambda c: c.score())
    
    print(f"\nmap -> имена: {names} (тип {type(names[0]).__name__})")
    print(f"map -> сила: {powers} (тип {type(powers[0]).__name__})")
    print(f"map -> рейтинг: {[round(r,1) for r in ratings]} (тип {type(ratings[0]).__name__})")
    print("\nВторой TypeVar R позволяет менять тип результата")
    

    
    # Сценарий 1: TypedCollection с Displayable
    print("\nСценарий 1: Displayable коллекция")
    display_coll = TypedCollection()
    
    # Объекты разных типов - не наследуются от Displayable, но имеют метод display()
    warrior = Warrior("Тор", 120, 70, "Мьёльнир")
    mage = Mage("Гэндальф", 90, 40, 150)
    
    display_coll.add(char1)
    display_coll.add(warrior)
    display_coll.add(mage)
    
    print("Объекты добавлены (без наследования от Displayable):")
    for item in display_coll.get_all():
        print(f"   - {type(item).__name__}: {item.display()}")
    
    # Сценарий 2: TypedCollection с Scorable
    print("\nСценарий 2: Scorable коллекция")
    score_coll = TypedCollection()
    
    score_coll.add(char2)
    score_coll.add(warrior)
    score_coll.add(mage)
    
    print("Объекты добавлены (без наследования от Scorable):")
    for item in score_coll.get_all():
        print(f"   - {type(item).__name__}: рейтинг = {item.score():.1f}")
    
    # Демонстрация работы методов с протоколами
    print("\nРабота методов с протоколами:")
    
    try:
        # filter на Displayable коллекции
        result = display_coll.filter(lambda d: "Воин" in d.display())
        if result:
            print(f"   filter(содержит 'Воин'): найдено {len(result)} -> {result[0].display()}")
        
        # map на Scorable коллекции
        all_scores = score_coll.map(lambda s: s.score())
        print(f"   map(score): {[round(s,1) for s in all_scores]}")
    except Exception as e:
        print(f"   Ошибка: {e}")
   

if __name__ == "__main__":
    main()