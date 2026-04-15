import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base import Character
from models import Warrior, Mage, Archer
from model import CharacterCollection


def main():
    print("=" * 60)
    print("Лабораторная работа №3 - Наследование и Полиморфизм")
    print("=" * 60)
    
    # СЦЕНАРИЙ 1: Создание объектов разных типов 
    print("\n[Сценарий 1] Создание объектов разных типов")
    
    w = Warrior("Торин", 100, 35, 55, 30, "Меч", 25)
    m = Mage("Гэндальф", 80, 28, 25, 75, "Огонь", 100)
    a = Archer("Леголас", 85, 32, 45, 40, "Длинный лук", 85)
    basic = Character("Обычный Герой", 80, 30, 40, 50)
    
    print("Созданы объекты:")
    print(f"  {w}")
    print(f"  {m}")
    print(f"  {a}")
    print(f"  {basic}")
    
    # СЦЕНАРИЙ 2: Новые методы дочерних классов
    print("\n[Сценарий 2] Уникальные методы дочерних классов")
    print(f"  Ярость берсерка: {w.berserker_rage()}")
    print(f"  Изучение заклинания: {m.learn_spell('Огненный шар')}")
    print(f"  Прицельный выстрел: {a.aimed_shot(basic)}")
    print(f"  Здоровье мишени после атаки: {basic.health}")
    
    # СЦЕНАРИЙ 3: Переопределенные методы 
    print("\n[Сценарий 3] Переопределенные методы attack() и magic_attack()")
    
    target = Character("Мишень", 100, 40, 30, 40)
    print(f"  Воин атакует: {w.attack(target)}")
    print(f"  Здоровье мишени: {target.health}")
    
    target2 = Character("Цель", 100, 40, 30, 40)
    print(f"  Маг атакует магией: {m.magic_attack(target2)}")
    print(f"  Здоровье цели: {target2.health}")
    
    target3 = Character("Манекен", 100, 40, 30, 40)
    print(f"  Лучник атакует: {a.attack(target3)}")
    print(f"  Здоровье манекена: {target3.health}")
    
    # СЦЕНАРИЙ 4: Полиморфизм (один метод - разное поведение) 
    print("\n[Сценарий 4] Полиморфизм (calculate_power_rating - разное поведение)")
    
    for p in [w, m, a, basic]:
        print(f"  {p.name:12} | Тип: {p.get_class_type():12} | Рейтинг силы: {p.calculate_power_rating():.2f}")
    
    # СЦЕНАРИЙ 5: Проверка типов через isinstance() 
    print("\n[Сценарий 5] Проверка типов через isinstance()")
    print(f"  Торин - Warrior: {isinstance(w, Warrior)}")
    print(f"  Торин - Character: {isinstance(w, Character)}")
    print(f"  Торин - Mage: {isinstance(w, Mage)}")
    print(f"  Гэндальф - Mage: {isinstance(m, Mage)}")
    print(f"  Гэндальф - Character: {isinstance(m, Character)}")
    print(f"  Леголас - Archer: {isinstance(a, Archer)}")
    print(f"  Обычный Герой - Character: {isinstance(basic, Character)}")
    
    # СЦЕНАРИЙ 6: Интеграция с коллекцией из ЛР-2 
    print("\n[Сценарий 6] Интеграция с коллекцией CharacterCollection")
    
    col = CharacterCollection()
    col.add(w)
    col.add(m)
    col.add(a)
    col.add(Warrior("Артас", 95, 32, 58, 25, "Топор", 20))
    col.add(Mage("Мерлин", 75, 25, 20, 60, "Молния", 60))
    col.add(Character("Странник", 90, 30, 35, 45))
    
    print(f"Коллекция содержит {len(col)} персонажей")
    for p in col.get_all():
        print(f"  - {p.name} ({p.get_class_type()})")
    
    # СЦЕНАРИЙ 7: Фильтрация коллекции по типу 
    print("\n[Сценарий 7] Фильтрация коллекции по типу")
    
    warriors = [p for p in col.get_all() if isinstance(p, Warrior)]
    mages = [p for p in col.get_all() if isinstance(p, Mage)]
    archers = [p for p in col.get_all() if isinstance(p, Archer)]
    basics = [p for p in col.get_all() if not isinstance(p, (Warrior, Mage, Archer))]
    
    print(f"  Воины ({len(warriors)}): {[p.name for p in warriors]}")
    print(f"  Маги ({len(mages)}): {[p.name for p in mages]}")
    print(f"  Лучники ({len(archers)}): {[p.name for p in archers]}")
    print(f"  Обычные персонажи ({len(basics)}): {[p.name for p in basics]}")
    
    # СЦЕНАРИЙ 8: Полиморфный вызов метода для всей коллекции 
    print("\n[Сценарий 8] calculate_power_rating() для всех персонажей коллекции")
    
    for p in col.get_all():
        print(f"  {p.name:15} | {p.get_class_type():12} | Рейтинг силы: {p.calculate_power_rating():6.2f}")
        
        

if __name__ == "__main__":
    main()