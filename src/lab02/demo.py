from collection import CharacterCollection
from model import Character

# Создание персонажей
character1 = Character("Арагорн", 95, 35, 55, 45)
character2 = Character("Гэндальф", 80, 25, 40, 75)
character3 = Character("Леголас", 75, 38, 50, 60)
character4 = Character("Фродо", 60, 20, 15, 40)
character5 = Character("Гимли", 90, 30, 58, 30)
character6 = Character("Саруман", 85, 28, 35, 78)

print("> Добавление персонажей в коллекцию")
character_collection = CharacterCollection()
character_collection.add(character1)
character_collection.add(character2)
character_collection.add(character3)
character_collection.add(character4)
character_collection.add(character5)
character_collection.add(character6)

for char in character_collection:
    print(f"   {char.game_name}, здоровье: {char.health}, сила: {char.power}")
print(f"Добавлено {len(character_collection)} персонажей")


print("\n> Коллекция после удаления персонажа")
print(f"Удаляем: {character2.game_name}")
character_collection.remove(character2)
for char in character_collection:
    print(f"   {char.game_name}, здоровье: {char.health}, сила: {char.power}")
print(f"В коллекции осталось {len(character_collection)} персонажей")

print("\n> Поиск персонажа по имени 'Гимли'")
find_gimli = character_collection.find_by_name("Гимли")
if find_gimli:
    print(f"   {find_gimli.game_name}, здоровье: {find_gimli.health}, сила: {find_gimli.power}")

print("\n> Поиск персонажей по силе (> 50)")
find_strong = character_collection.find_by_power_range(min_power=51)
for strong in find_strong:
    print(f"   {strong.game_name}, сила: {strong.power}")


print("\n> Обход коллекции с помощью iterator")
print(f"Всего персонажей: {len(character_collection)}")
for i, character in enumerate(character_collection, 1):
    print(f"  {i}. {character.game_name}, здоровье: {character.health}, сила: {character.power}, интеллект: {character.intelligence}")

print("\n> Проверка ошибки на добавление дубликата")
try:
    character_collection.add(character1)
    print("Ошибка: дубликат был добавлен!")
except ValueError as e:
    print(f"Дубликат не добавлен так как: {e}")

print("\n---Сценарий 1: фильтрация здоровых персонажей (здоровье >= 80)")
healthy_characters = character_collection.get_healthy(min_health=80)

print(f"\n1) Здоровых персонажей: {len(healthy_characters)} из {len(character_collection)}")

print("\n2) Список здоровых персонажей:")
for character in healthy_characters:
    print(f"   {character.game_name}, здоровье: {character.health}")


print("\n> Сортировка по имени (А-Я):")
character_collection.sort_by_name()
for i, char in enumerate(character_collection, 1):
    print(f"   {i}. {char.game_name}")

print("\n> Сортировка по силе (от сильного к слабому):")
character_collection.sort_by_power(reverse=True)
for i, char in enumerate(character_collection, 1):
    print(f"   {i}. {char.game_name} (сила: {char.power})")