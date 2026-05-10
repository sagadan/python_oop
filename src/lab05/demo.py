from collection import CharacterCollection
from model import Character, Warrior, Mage, Archer
from strategies import *


char1 = Warrior("Сайто", 90, 30, 55, 15, "Двуручный меч", 25)
char2 = Mage("Коб", 65, 20, 20, 75, "Белая магия", 100)
char3 = Archer("Эрик", 80, 35, 42, 30, "Длинный лук", 95)
char4 = Warrior("Саймон", 75, 25, 48, 18, "Одноручный меч", 20)
char5 = Mage("Генри", 70, 15, 18, 65, "Природная магия", 85)
char6 = Archer("Брэд", 68, 28, 35, 25, "Короткий лук", 85)


character_collection = CharacterCollection()
character_collection.add(char1)
character_collection.add(char2)
character_collection.add(char3)
character_collection.add(char4)
character_collection.add(char5)
character_collection.add(char6)


def print_list_characters(characters):
    if not characters:
        print("  Список пуст")
        return
    for i, char in enumerate(characters, 1):
        print(f"  {i}. {char.game_name} ({char.get_class_type()}) - {char.health} {char.power}")


print("\nСценарий 1: сортировка коллекции")

print("\n1) Сортировка по имени (алфавитный порядок)")
sort_name = character_collection.copy().sort_by_name()
print(sort_name)

print("\n2) Сортировка по силе (от слабого к сильному)")
sort_power = character_collection.copy().sort_by_power()
print(sort_power)

print("\n3) Сортировка по здоровью (от здоровых к больным)")
sort_health = character_collection.copy().sort_by_health(reverse=True)
print(sort_health)

print("\n4) Сортировка по классу (Воин -> Маг -> Лучник)")
sort_class = character_collection.copy().sort_by_class()
print(sort_class)


print("\nСценарий 2: фильтрация коллекции предикатами")

print("\n1) Только воины (фильтр filter_warrior)")
warriors = list(filter(filter_warrior, character_collection.get_all()))
print_list_characters(warriors)

print("\n2) Только маги (фильтр filter_mage)")
mages = list(filter(filter_mage, character_collection.get_all()))
print_list_characters(mages)

print("\n3) Здоровые персонажи (здоровье > 50) через lambda")
healthy = character_collection.copy().filter_by(lambda c: c.health > 50)
print(healthy)

print("\n4) Сильные персонажи (сила > 30) через функцию filter_powerful")
powerful = character_collection.copy().filter_by(filter_powerful)
print(powerful)


print("\nСценарий 3: map, lambda и фабрика функций")

print("\n1) Список имён персонажей (через map и lambda)")
names_list = list(map(lambda c: c.game_name, character_collection.get_all()))
print(f"> Имена: {names_list}")

print("\n2) Список силы персонажей (через map)")
power_list = list(map(lambda c: c.power, character_collection.get_all()))
print(f"> Сила: {power_list}")

print("\n3) Сильные персонажи (сила > 40) через фабрику функций")
power_filter = make_power_filter(40)
strong_characters = list(filter(power_filter, character_collection.get_all()))
print_list_characters(strong_characters)

print("\n4) Здоровые персонажи (здоровье > 70) через фабрику функций")
health_filter = make_health_filter(70)
very_healthy = list(filter(health_filter, character_collection.get_all()))
print_list_characters(very_healthy)


print("\nСценарий 4: паттерн стратегия через callable-объекты")
print("   Цепочки операций над коллекцией\n")

print("\nСтратегия 1")
print("- Цепочка: фильтр(воины) → сортировка(по силе) → стратегия(по классу)")
result1 = (character_collection.copy()
           .filter_by(filter_warrior)
           .sort_by_power(reverse=True)
           .apply(StrategyByClass()))
for char in result1.get_all():
    print(f"  {char}")

print("\nСтратегия 2")
print("- Цепочка с другой стратегией (StrategyByName)")
result2 = (character_collection.copy()
           .filter_by(filter_warrior)
           .sort_by_power(reverse=True)
           .apply(StrategyByName()))
for char in result2.get_all():
    print(f"  {char}")

print("\nСтратегия 3")
print("- Цепочка: фильтр(маги) → сортировка(по интеллекту) → стратегия(по здоровью)")
result3 = (character_collection.copy()
           .filter_by(filter_mage)
           .sort_by_intelligence(reverse=True)
           .apply(StrategyByHealth()))
for char in result3.get_all():
    print(f"  {char}")

