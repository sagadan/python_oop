from models import Character, Warrior, Mage, Archer, CharacterCollection
from interfaces import Printable, Comparable, PowerRatable


# Универсальные функции через интерфейсы

def print_all(characters: list[Printable]):
    """Универсальная функция вывода через интерфейс Printable"""
    for char in characters:
        print(f"  • {char.to_string()}")


def show_power_rating(character: PowerRatable):
    """Функция для расчета рейтинга силы с проверкой типа"""
    if not isinstance(character, PowerRatable):
        raise TypeError(f"{character.game_name} не может иметь рейтинг силы!")
    print(f"  • {character.game_name}: рейтинг = {character.get_power_rating():.2f}")


# Сценарий 1: Создание персонажей
print("\nСценарий 1: Создание персонажей")

warrior = Warrior("Уолтер", 100, 35, 55, 15, "Двуручный меч", 45)
mage = Mage("Джесси", 70, 25, 10, 75, "Огненная магия", 100)
archer = Archer("Сол", 80, 40, 50, 30, "Длинный лук", 95)
basic = Character("Герой", 85, 30, 25, 40)

print("\nСозданные персонажи:")
print(f"  • {warrior}")
print(f"  • {mage}")
print(f"  • {archer}")
print(f"  • {basic}")

# Проверка интерфейсов через isinstance
print("\nПроверка интерфейсов:")
print(f"  Воин: Printable={isinstance(warrior, Printable)}, "
      f"Comparable={isinstance(warrior, Comparable)}, "
      f"PowerRatable={isinstance(warrior, PowerRatable)}")
print(f"  Маг: Printable={isinstance(mage, Printable)}, "
      f"Comparable={isinstance(mage, Comparable)}, "
      f"PowerRatable={isinstance(mage, PowerRatable)}")
print(f"  Лучник: Printable={isinstance(archer, Printable)}, "
      f"Comparable={isinstance(archer, Comparable)}, "
      f"PowerRatable={isinstance(archer, PowerRatable)}")

# Разные реализации to_string()
print("\nРазные реализации to_string():")
print(f"  {warrior.to_string()}")
print(f"  {mage.to_string()}")
print(f"  {archer.to_string()}")
print(f"  {basic.to_string()}")

# Сценарий 2: Универсальные функции
print("\nСценарий 2: Универсальные функции")

characters = [warrior, mage, archer, basic]
print("\nВывод через интерфейс Printable:")
print_all(characters)

print("\nРейтинг силы через интерфейс PowerRatable:")
show_power_rating(warrior)
show_power_rating(mage)

try:
    show_power_rating(archer)
except TypeError as e:
    print(f"  ✗ Ошибка: {e}")

# Сравнение через Comparable
print("\nСравнение персонажей:")
print(f"  {warrior.game_name} vs {mage.game_name}: {warrior.compare_to(mage)}")
print(f"  {archer.game_name} vs {basic.game_name}: {archer.compare_to(basic)}")

# Сценарий 3: Работа с коллекцией 
print("\nСценарий 3: Работа с коллекцией")

# Создаем доп. персонажей
warrior2 = Warrior("Хэнк", 95, 38, 60, 12, "Ледяная скорбь", 50)
mage2 = Mage("Густаво", 75, 30, 15, 80, "Белая магия", 120)

# Создание коллекции и добавление
collection = CharacterCollection()
for char in [warrior, mage, archer, basic, warrior2, mage2]:
    collection.add(char)

print(f"\nВсего персонажей: {len(collection)}")

# Фильтрация по типу
print("\nФильтрация по типу класса:")
warriors = collection.filter_by_interface(Warrior)
print(f"  Воины ({len(warriors)}): {', '.join([w.game_name for w in warriors])}")

mages = collection.filter_by_interface(Mage)
print(f"  Маги ({len(mages)}): {', '.join([m.game_name for m in mages])}")

# Фильтрация по интерфейсу
print("\nФильтрация по интерфейсу PowerRatable:")
power_chars = collection.get_power_ratable()
for char in power_chars:
    print(f"  • {char.game_name} - рейтинг: {char.get_power_rating():.2f}")

# Сортировка через Comparable
print("\nСортировка через Comparable:")
print("  До сортировки:", [c.game_name for c in collection.get_all()])
collection.sort_by_comparable()
print("  После сортировки:", [c.game_name for c in collection.get_all()])

# Итог
print("Итог:")
print(f"  Всего: {len(collection)}")
print(f"  Printable: {len(collection.get_printable())}")
print(f"  Comparable: {len(collection.get_comparable())}")
print(f"  PowerRatable: {len(collection.get_power_ratable())}")
