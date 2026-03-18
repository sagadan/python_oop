from model import Character  

def demo():
    """Компактная демонстрация работы класса Character."""
    
    print("=" * 60)
    print("Демонстрация касса персонажа")
    print("=" * 60)
    
    # 1. Создание объектов
    print("\n1. Создание персонажей:")
    warrior = Character("Фродо", 100, 35, 55, 20) 
    mage = Character("Гэндальф", 80, 25, 15, 75)        
    print("   Воин и Маг созданы")
    
    # 2. Вывод через print
    print("\n2. Вывод информации (__str__):")
    print(warrior)
    
    # 3. Сравнение объектов
    print("\n3. Сравнение (__eq__):")
    warrior2 = Character("Гэндальф", 100, 35, 55, 20)
    print(f"   warrior == warrior2: {warrior == warrior2}")
    print(f"   warrior == mage: {warrior == mage}")
    
    # 4. Демонстрация __repr__
    print("\n4. Представление (__repr__):")
    print(f"   {repr(warrior)}")
    
    # 5. Некорректное создание
    print("\n5. Примеры ошибок:")
    try:
        bad = Character("", 100, 35, 55, 20)
    except ValueError as e:
        print(f"   Пустое имя: {e}")
    
    try:
        bad = Character("Bad", -10, 35, 55, 20)
    except ValueError as e:
        print(f"   Отрицательное здоровье: {e}")
    
    # 6. Доступ к атрибутам
    print("\n6. Доступ к атрибутам:")
    print(f"   Имя: {warrior.game_name}")
    print(f"   Здоровье: {warrior.health}/100")
    print(f"   Выносливость: {warrior.stamina}/40")
    
    # 7. Изменение через сеттер
    print("\n7. Изменение свойств:")
    old_health = warrior.health
    warrior.health = 90
    print(f"   Здоровье изменено: {old_health} -> {warrior.health}")
    
    try:
        warrior.health = 200
    except ValueError as e:
        print(f"   Ошибка: {e}")
    
    # 8. Бизнес-методы
    print("\n8. Бизнес-методы:")
    
    # Атаки
    print(f"   {warrior.attack(mage)}")
    print(f"   {mage.magic_attack(warrior)}")
    
    # 9. Финальное состояние
    print("\n9. Итоговое состояние:")
    print(warrior)
    print(mage)
    
    print("\n" + "=" * 60)
    print("Демонстрация завершена")
    print("=" * 60)


if __name__ == "__main__":
    demo()