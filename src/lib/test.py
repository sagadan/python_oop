# class Character:
#     def __init__(self, name: str, max_health: int, level: int = 1, experience: int = 0):
#         name_clean = name.strip()
#         if not name_clean:
#             raise ValueError("имя пустое")
#         self._name = name_clean
        
#         if max_health <= 0:
#             raise ValueError("max_health > 0")
#         self._max_health = max_health
#         self._health = max_health  
        
#         if not (1 <= level <= 100):
#             raise ValueError("level должен быть от 1 до 100")
#         self._level = level
        
#         if experience < 0:
#             raise ValueError("experience не может быть отрицательным")
#         self._experience = experience
        
#         # Проверяем, не нужно ли сразу повысить уровень
#         self._check_level_up()
    
#     # Свойства 
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def health(self):
#         return self._health
    
#     @property
#     def max_health(self):
#         return self._max_health
    
#     @property
#     def level(self):
#         return self._level
    
#     @property
#     def experience(self):
#         return self._experience
    
#     # Внутренний метод для проверки повышения уровня
#     def _check_level_up(self):
#         "Повышает уровень, если опыта достаточно"
#         while self._experience >= self._level * 100 and self._level < 100:
#             self._experience -= self._level * 100
#             self._level += 1
#         # Если уровень стал 100, лишний опыт просто отбрасывается
#         if self._level == 100:
#             self._experience = 0
    
#     # Основные методы
#     def take_damage(self, amount: int):
#         if amount <= 0:
#             raise ValueError("amount > 0")
#         self._health = max(0, self._health - amount)
    
#     def heal(self, amount: int):
#         if amount <= 0:
#             raise ValueError("amount > 0")
#         self._health = min(self._max_health, self._health + amount)
    
#     def gain_xp(self, amount: int):
#         if amount <= 0:
#             raise ValueError("amount > 0")
#         self._experience += amount
#         self._check_level_up()
    
#     def is_alive(self) -> bool:
#         return self._health > 0
    
#     def __str__(self) -> str:
#         return f"{self._name} (уровень {self._level}): {self._health}/{self._max_health} HP, XP {self._experience}"
    
#     def __eq__(self, other) -> bool:
#         if not isinstance(other, Character):
#             return False
#         return self._name == other._name




# # Создание персонажа
# hero = Character('  Воин  ', 100, 1, 0)  
# print(hero.name)        

# # Бой и лечение
# hero.take_damage(30)
# print(hero.health)      
# hero.heal(20)
# print(hero.health)    

# # Получение опыта и повышение уровня
# hero.gain_xp(150)
# print(hero.level)       
# print(hero.experience)  

# # Проверка жизни
# print(hero.is_alive())  

# # Строковое представление
# print(hero)             

# # Сравнение по имени
# hero2 = Character('Воин', 200)
# print(hero == hero2)   

# # Проверка граничных условий
# try:
#     Character('', 100)   
# except ValueError as e:
#     print(e)

# try:
#     Character('Воин', 0) 
# except ValueError as e:
#     print(e)

# try:
#     hero.take_damage(-5) 
# except ValueError as e:
#     print(e)





# import random
# from abc import ABC, abstractmethod
# from typing import List, Optional

# # 1. Исключение
# class InsufficientManaError(Exception):
#     pass

# # 2. Интерфейс стратегии 
# class AttackStrategy(ABC):
#     @abstractmethod
#     def attack(self, attacker, target):
#         pass
#     def __call__(self, attacker, target):
#         return self.attack(attacker, target)

# # 3. Конкретные стратегии 
# class SwordAttack(AttackStrategy):
#     def __init__(self, damage: int):
#         if damage <= 0: raise ValueError("damage > 0")
#         self.damage = damage
#     def attack(self, attacker, target):
#         target.take_damage(self.damage)

# class BowAttack(AttackStrategy):
#     def __init__(self, damage: int, accuracy: float):
#         if damage <= 0: raise ValueError("damage > 0")
#         if not (0 <= accuracy <= 1): raise ValueError("accuracy от 0 до 1")
#         self.damage, self.accuracy = damage, accuracy
#     def attack(self, attacker, target):
#         if random.random() < self.accuracy:
#             target.take_damage(self.damage)

# class MagicAttack(AttackStrategy):
#     def __init__(self, damage: int, mana_cost: int):
#         if damage <= 0 or mana_cost <= 0: raise ValueError("damage > 0, mana_cost > 0")
#         self.damage, self.mana_cost = damage, mana_cost
#     def attack(self, attacker, target):
#         if attacker.experience < self.mana_cost:
#             raise InsufficientManaError(f"Нужно {self.mana_cost}, есть {attacker.experience}")
#         attacker._experience -= self.mana_cost
#         target.take_damage(self.damage)

# class CriticalAttack(AttackStrategy):
#     def __init__(self, base_damage: int, crit_multiplier: float):
#         if base_damage <= 0 or crit_multiplier <= 1: raise ValueError("base_damage > 0, crit_multiplier > 1")
#         self.base_damage, self.crit_multiplier = base_damage, crit_multiplier
#     def attack(self, attacker, target):
#         damage = self.base_damage if attacker.level % 2 else int(self.base_damage * self.crit_multiplier)
#         target.take_damage(damage)

# # 4. Новая стратегия 
# class FireAttack(AttackStrategy):
#     def __init__(self, damage: int, burn_damage: int, burn_duration: int = 3):
#         if damage <= 0 or burn_damage <= 0 or burn_duration <= 0: raise ValueError("все параметры > 0")
#         self.damage, self.burn_damage, self.burn_duration = damage, burn_damage, burn_duration
#     def attack(self, attacker, target):
#         target.take_damage(self.damage)
#         if not hasattr(target, '_burn_turns'):
#             target._burn_turns = 0
#         target._burn_turns = max(target._burn_turns, self.burn_duration)

# # 5. Класс Character 
# class Character:
#     def __init__(self, name: str, max_health: int, level: int = 1, experience: int = 0):
#         name_clean = name.strip()
#         if not name_clean: raise ValueError("имя пустое")
#         self._name = name_clean
#         if max_health <= 0: raise ValueError("max_health > 0")
#         self._max_health = max_health
#         self._health = max_health
#         if not (1 <= level <= 100): raise ValueError("level от 1 до 100")
#         self._level = level
#         if experience < 0: raise ValueError("experience >= 0")
#         self._experience = experience
#         self._attack_strategy = None
#         self._burn_turns = 0
#         self._check_level_up()
    
#     # Свойства
#     @property
#     def name(self): return self._name
#     @property
#     def health(self): return self._health
#     @property
#     def max_health(self): return self._max_health
#     @property
#     def level(self): return self._level
#     @property
#     def experience(self): return self._experience
    
#     def _check_level_up(self):
#         while self._experience >= self._level * 100 and self._level < 100:
#             self._experience -= self._level * 100
#             self._level += 1
#         if self._level == 100:
#             self._experience = 0
    
#     def take_damage(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._health = max(0, self._health - amount)
    
#     def heal(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._health = min(self._max_health, self._health + amount)
    
#     def gain_xp(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._experience += amount
#         self._check_level_up()
    
#     def is_alive(self) -> bool:
#         return self._health > 0
    
#     def set_attack_strategy(self, strategy: AttackStrategy):
#         self._attack_strategy = strategy
    
#     def attack(self, target):
#         if self._attack_strategy is None:
#             raise ValueError("Стратегия атаки не установлена")
#         self._attack_strategy.attack(self, target)
#         # Применяем эффект горения (FireAttack)
#         if self._burn_turns > 0:
#             self.take_damage(10)  # упрощённый урон от горения
#             self._burn_turns -= 1
    
#     def __str__(self):
#         return f"{self._name} (ур.{self._level}): {self._health}/{self._max_health} HP, XP {self._experience}"
    
#     def __eq__(self, other):
#         return isinstance(other, Character) and self._name == other._name

# # 6. Класс Party и битва 
# class Party:
#     def __init__(self, characters: Optional[List[Character]] = None):
#         self._characters = characters if characters else []
    
#     def add(self, character: Character):
#         self._characters.append(character)
    
#     def alive_members(self) -> List[Character]:
#         return [c for c in self._characters if c.is_alive()]
    
#     def battle(self, other_party):
#         attackers = self.alive_members()
#         defenders = other_party.alive_members()
#         while attackers and defenders:
#             for attacker in attackers[:]:
#                 if not attacker.is_alive():
#                     continue
#                 defenders = other_party.alive_members()
#                 if not defenders:
#                     break
#                 target = random.choice(defenders)
#                 try:
#                     attacker.attack(target)
#                 except InsufficientManaError as e:
#                     print(f"Мана ошибка: {e}")
#             attackers = self.alive_members()
#             defenders = other_party.alive_members()

# # 7. Демонстрация 
# if __name__ == "__main__":
#     # Тест 1: базовый Character
#     hero = Character('  Воин  ', 100, 100, 350)
#     hero.take_damage(10)
#     hero.heal(20)
#     hero.gain_xp(100)
#     print(hero)  # Воин (ур.2): 90/100 HP, XP 50
    
#     # Тест 2: стратегии
#     orc = Character('Орк', 120, 4, 350)
#     hero.set_attack_strategy(SwordAttack(20))
#     hero.attack(orc)
#     print(f"Орк HP: {orc.health}")  # 100
    
#     mage = Character('Маг', 80, 3, 350)  
#     mage.set_attack_strategy(MagicAttack(100, 100))
#     mage.attack(orc)
#     print(f"Орк HP: {orc.health}")  # 50
#     print(f"Маг XP: {mage.experience}")  # 250
    
#     # Тест 3: новая стратегия FireAttack
#     pyro = Character('Пиро', 100, 5, 200)
#     pyro.set_attack_strategy(FireAttack(40, 15))
#     dummy = Character('Цель', 100, 1, 0)
#     pyro.attack(dummy)
#     print(f"Цель HP: {dummy.health}")  # 60 (100-40)
    
#     # Тест 4: командная битва
#     good = Party([hero, mage, pyro])
#     evil = Party([orc, dummy])
#     good.battle(evil)
#     print(f"Орк жив: {orc.is_alive()}, Цель жива: {dummy.is_alive()}")






# import random
# from abc import ABC, abstractmethod
# from typing import List, Optional

# class InsufficientManaError(Exception):
#     pass

# class AttackStrategy(ABC):
#     @abstractmethod
#     def attack(self, attacker, target):
#         pass
#     def __call__(self, attacker, target):
#         return self.attack(attacker, target)

# class SwordAttack(AttackStrategy):
#     def __init__(self, damage: int):
#         if damage <= 0: raise ValueError("damage > 0")
#         self.damage = damage
#     def attack(self, attacker, target):
#         target.take_damage(self.damage)

# class BowAttack(AttackStrategy):
#     def __init__(self, damage: int, accuracy: float):
#         if damage <= 0: raise ValueError("damage > 0")
#         if not (0 <= accuracy <= 1): raise ValueError("accuracy от 0 до 1")
#         self.damage, self.accuracy = damage, accuracy
#     def attack(self, attacker, target):
#         if random.random() < self.accuracy:
#             target.take_damage(self.damage)

# class MagicAttack(AttackStrategy):
#     def __init__(self, damage: int, mana_cost: int):
#         if damage <= 0 or mana_cost <= 0: raise ValueError("damage > 0, mana_cost > 0")
#         self.damage, self.mana_cost = damage, mana_cost
#     def attack(self, attacker, target):
#         if attacker.experience < self.mana_cost:
#             raise InsufficientManaError(f"Нужно {self.mana_cost}, есть {attacker.experience}")
#         attacker._experience -= self.mana_cost
#         target.take_damage(self.damage)

# class CriticalAttack(AttackStrategy):
#     def __init__(self, base_damage: int, crit_multiplier: float):
#         if base_damage <= 0 or crit_multiplier <= 1: raise ValueError("base_damage > 0, crit_multiplier > 1")
#         self.base_damage, self.crit_multiplier = base_damage, crit_multiplier
#     def attack(self, attacker, target):
#         damage = self.base_damage if attacker.level % 2 else int(self.base_damage * self.crit_multiplier)
#         target.take_damage(damage)

# class FireAttack(AttackStrategy):
#     def __init__(self, damage: int, burn_damage: int, burn_duration: int = 3):
#         if damage <= 0 or burn_damage <= 0 or burn_duration <= 0: raise ValueError("все параметры > 0")
#         self.damage, self.burn_damage, self.burn_duration = damage, burn_damage, burn_duration
#     def attack(self, attacker, target):
#         target.take_damage(self.damage)
#         if not hasattr(target, '_burn_turns'):
#             target._burn_turns = 0
#         target._burn_turns = max(target._burn_turns, self.burn_duration)

# class Character:
#     def __init__(self, name: str, max_health: int, level: int = 1, experience: int = 0):
#         name_clean = name.strip()
#         if not name_clean: raise ValueError("имя пустое")
#         self._name = name_clean
#         if max_health <= 0: raise ValueError("max_health > 0")
#         self._max_health = max_health
#         self._health = max_health
#         if not (1 <= level <= 100): raise ValueError("level от 1 до 100")
#         self._level = level
#         if experience < 0: raise ValueError("experience >= 0")
#         self._experience = experience
#         self._attack_strategy = None
#         self._burn_turns = 0
#         self._check_level_up()
    
#     @property
#     def name(self): return self._name
#     @property
#     def health(self): return self._health
#     @property
#     def max_health(self): return self._max_health
#     @property
#     def level(self): return self._level
#     @property
#     def experience(self): return self._experience
    
#     def _check_level_up(self):
#         while self._experience >= self._level * 100 and self._level < 100:
#             self._experience -= self._level * 100
#             self._level += 1
#         if self._level == 100:
#             self._experience = 0
    
#     def take_damage(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._health = max(0, self._health - amount)
    
#     def heal(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._health = min(self._max_health, self._health + amount)
    
#     def gain_xp(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._experience += amount
#         self._check_level_up()
    
#     def is_alive(self) -> bool:
#         return self._health > 0
    
#     def set_attack_strategy(self, strategy: AttackStrategy):
#         self._attack_strategy = strategy
    
#     def attack(self, target):
#         if self._attack_strategy is None:
#             raise ValueError("Стратегия атаки не установлена")
#         self._attack_strategy.attack(self, target)
#         if self._burn_turns > 0:
#             self.take_damage(10)
#             self._burn_turns -= 1
    
#     def __str__(self):
#         return f"{self._name} (ур.{self._level}): {self._health}/{self._max_health} HP, XP {self._experience}"
    
#     def __eq__(self, other):
#         return isinstance(other, Character) and self._name == other._name

# class Party:
#     def __init__(self, characters: Optional[List[Character]] = None):
#         self._characters = characters if characters else []
    
#     def add(self, character: Character):
#         self._characters.append(character)
    
#     def alive_members(self) -> List[Character]:
#         return [c for c in self._characters if c.is_alive()]
    
#     def battle(self, other_party):
#         attackers = self.alive_members()
#         defenders = other_party.alive_members()
#         while attackers and defenders:
#             for attacker in attackers[:]:
#                 if not attacker.is_alive():
#                     continue
#                 defenders = other_party.alive_members()
#                 if not defenders:
#                     break
#                 target = random.choice(defenders)
#                 try:
#                     attacker.attack(target)
#                 except InsufficientManaError as e:
#                     print(f"Ошибка маны: {e}")
#             attackers = self.alive_members()
#             defenders = other_party.alive_members()

# # ========== ГЛАВНОЕ - ЗДЕСЬ ВСЁ ИСПРАВЛЕНО ==========
# if __name__ == "__main__":
#     hero = Character('Воин', 100, 1, 0)
#     hero.take_damage(30)
#     hero.heal(20)
#     hero.gain_xp(150)
#     print(hero)
    
#     orc = Character('Орк', 120, 4, 100)
#     hero.set_attack_strategy(SwordAttack(20))
#     hero.attack(orc)
#     print(f"Орк HP: {orc.health}")
    
#     # ВНИМАНИЕ: ЗДЕСЬ 350 ОПЫТА, А НЕ 50!
#     mage = Character('Маг', 80, 3, 350)
#     mage.set_attack_strategy(MagicAttack(50, 100))
#     mage.attack(orc)
#     print(f"Орк HP: {orc.health}")
#     print(f"Маг XP: {mage.experience}")






# import random
# from abc import ABC, abstractmethod
# from typing import List, Optional

# class InsufficientManaError(Exception):
#     pass

# class AttackStrategy(ABC):
#     @abstractmethod
#     def attack(self, attacker, target):
#         pass
#     def __call__(self, attacker, target):
#         return self.attack(attacker, target)

# class SwordAttack(AttackStrategy):
#     def __init__(self, damage: int):
#         if damage <= 0: raise ValueError("damage > 0")
#         self.damage = damage
#     def attack(self, attacker, target):
#         target.take_damage(self.damage)

# class BowAttack(AttackStrategy):
#     def __init__(self, damage: int, accuracy: float):
#         if damage <= 0: raise ValueError("damage > 0")
#         if not (0 <= accuracy <= 1): raise ValueError("accuracy от 0 до 1")
#         self.damage, self.accuracy = damage, accuracy
#     def attack(self, attacker, target):
#         if random.random() < self.accuracy:
#             target.take_damage(self.damage)

# class MagicAttack(AttackStrategy):
#     def __init__(self, damage: int, mana_cost: int):
#         if damage <= 0 or mana_cost <= 0: raise ValueError("damage > 0, mana_cost > 0")
#         self.damage, self.mana_cost = damage, mana_cost
#     def attack(self, attacker, target):
#         if attacker.experience < self.mana_cost:
#             raise InsufficientManaError(f"Нужно {self.mana_cost}, есть {attacker.experience}")
#         attacker._experience -= self.mana_cost
#         target.take_damage(self.damage)

# class CriticalAttack(AttackStrategy):
#     def __init__(self, base_damage: int, crit_multiplier: float):
#         if base_damage <= 0 or crit_multiplier <= 1: raise ValueError("base_damage > 0, crit_multiplier > 1")
#         self.base_damage, self.crit_multiplier = base_damage, crit_multiplier
#     def attack(self, attacker, target):
#         damage = self.base_damage if attacker.level % 2 else int(self.base_damage * self.crit_multiplier)
#         target.take_damage(damage)

# class FireAttack(AttackStrategy):
#     def __init__(self, damage: int, burn_damage: int, burn_duration: int = 3):
#         if damage <= 0 or burn_damage <= 0 or burn_duration <= 0: raise ValueError("все параметры > 0")
#         self.damage, self.burn_damage, self.burn_duration = damage, burn_damage, burn_duration
#     def attack(self, attacker, target):
#         target.take_damage(self.damage)
#         if not hasattr(target, '_burn_turns'):
#             target._burn_turns = 0
#         target._burn_turns = max(target._burn_turns, self.burn_duration)

# class Character:
#     def __init__(self, name: str, max_health: int, level: int = 1, experience: int = 0):
#         name_clean = name.strip()
#         if not name_clean: raise ValueError("имя пустое")
#         self._name = name_clean
#         if max_health <= 0: raise ValueError("max_health > 0")
#         self._max_health = max_health
#         self._health = max_health
#         if not (1 <= level <= 100): raise ValueError("level от 1 до 100")
#         self._level = level
#         if experience < 0: raise ValueError("experience >= 0")
#         self._experience = experience
#         self._attack_strategy = None
#         self._burn_turns = 0
#         self._check_level_up()
    
#     @property
#     def name(self): return self._name
#     @property
#     def health(self): return self._health
#     @property
#     def max_health(self): return self._max_health
#     @property
#     def level(self): return self._level
#     @property
#     def experience(self): return self._experience
    
#     def _check_level_up(self):
#         while self._experience >= self._level * 100 and self._level < 100:
#             self._experience -= self._level * 100
#             self._level += 1
#         if self._level == 100:
#             self._experience = 0
    
#     def take_damage(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._health = max(0, self._health - amount)
    
#     def heal(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._health = min(self._max_health, self._health + amount)
    
#     def gain_xp(self, amount: int):
#         if amount <= 0: raise ValueError("amount > 0")
#         self._experience += amount
#         self._check_level_up()
    
#     def is_alive(self) -> bool:
#         return self._health > 0
    
#     def set_attack_strategy(self, strategy: AttackStrategy):
#         self._attack_strategy = strategy
    
#     def attack(self, target):
#         if self._attack_strategy is None:
#             raise ValueError("Стратегия атаки не установлена")
#         self._attack_strategy.attack(self, target)
#         if self._burn_turns > 0:
#             self.take_damage(10)
#             self._burn_turns -= 1
    
#     def __str__(self):
#         return f"{self._name} (ур.{self._level}): {self._health}/{self._max_health} HP, XP {self._experience}"
    
#     def __eq__(self, other):
#         return isinstance(other, Character) and self._name == other._name

# class Party:
#     def __init__(self, characters: Optional[List[Character]] = None):
#         self._characters = characters if characters else []
    
#     def add(self, character: Character):
#         self._characters.append(character)
    
#     def alive_members(self) -> List[Character]:
#         return [c for c in self._characters if c.is_alive()]
    
#     def battle(self, other_party):
#         attackers = self.alive_members()
#         defenders = other_party.alive_members()
#         while attackers and defenders:
#             for attacker in attackers[:]:
#                 if not attacker.is_alive():
#                     continue
#                 defenders = other_party.alive_members()
#                 if not defenders:
#                     break
#                 target = random.choice(defenders)
#                 try:
#                     attacker.attack(target)
#                 except InsufficientManaError as e:
#                     print(f"Ошибка маны: {e}")
#             attackers = self.alive_members()
#             defenders = other_party.alive_members()


# if __name__ == "__main__":
#     hero = Character('Воин', 100, 1, 0)
#     hero.take_damage(30)
#     hero.heal(20)
#     hero.gain_xp(150)
#     print(hero)
    
#     orc = Character('Орк', 120, 4, 100)
#     hero.set_attack_strategy(SwordAttack(20))
#     hero.attack(orc)
#     print(f"Орк HP: {orc.health}")
    
#     mage = Character('Маг', 80, 3, 50)
#     mage.set_attack_strategy(MagicAttack(50, 100))
    
#     try:
#         mage.attack(orc)
#         print(f"Орк HP: {orc.health}")
#         print(f"Маг XP: {mage.experience}")
#     except InsufficientManaError as e:
#         print(f"Атака не удалась: {e}")
#         print("Маг не смог атаковать - недостаточно опыта!")
#         print(f"У мага осталось: {mage.experience} XP, орк здоров: {orc.health}")









class Character:
    def __init__(self, name: str, max_health: int, level: int = 1, experience: int = 0):
        # Обработка name
        name_clean = name.strip()
        if not name_clean:
            raise ValueError("имя пустое")
        self._name = name_clean
        
        # Обработка max_health
        if max_health <= 0:
            raise ValueError("max_health > 0")
        self._max_health = max_health
        self._health = max_health  # начальное здоровье = максимальному
        
        # Обработка level
        if not (1 <= level <= 100):
            raise ValueError("level должен быть от 1 до 100")
        self._level = level
        
        # Обработка experience
        if experience < 0:
            raise ValueError("experience не может быть отрицательным")
        self._experience = experience
        
        # Проверяем, не нужно ли сразу повысить уровень
        self._check_level_up()
    
    # === Свойства (только чтение) ===
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @property
    def max_health(self):
        return self._max_health
    
    @property
    def level(self):
        return self._level
    
    @property
    def experience(self):
        return self._experience
    
    # === Внутренний метод для проверки повышения уровня ===
    def _check_level_up(self):
        """Повышает уровень, если опыта достаточно"""
        while self._experience >= self._level * 100 and self._level < 100:
            self._experience -= self._level * 100
            self._level += 1
        # Если уровень стал 100, лишний опыт просто отбрасывается
        if self._level == 100:
            self._experience = 0
    
    # === Основные методы ===
    def take_damage(self, amount: int):
        if amount <= 0:
            raise ValueError("amount > 0")
        self._health = max(0, self._health - amount)
    
    def heal(self, amount: int):
        if amount <= 0:
            raise ValueError("amount > 0")
        self._health = min(self._max_health, self._health + amount)
    
    def gain_xp(self, amount: int):
        if amount <= 0:
            raise ValueError("amount > 0")
        self._experience += amount
        self._check_level_up()
    
    def is_alive(self) -> bool:
        return self._health > 0
    
    # === Специальные методы ===
    def __str__(self) -> str:
        return f"{self._name} (уровень {self._level}): {self._health}/{self._max_health} HP, XP {self._experience}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Character):
            return False
        return self._name == other._name
    





    # Создание персонажа
hero = Character('  Воин  ', 100, 1, 0)  # пробелы обрезаются
print(hero.name)        # "Воин"

# Бой и лечение
hero.take_damage(30)
print(hero.health)      # 70
hero.heal(20)
print(hero.health)      # 90

# Получение опыта и повышение уровня
hero.gain_xp(150)
print(hero.level)       # 2 (было 1, порог 100 → повысился)
print(hero.experience)  # 50 (150 - 100 = 50)

# Проверка жизни
print(hero.is_alive())  # True

# Строковое представление
print(hero)             # "Воин (уровень 2): 90/100 HP, XP 50"

# Сравнение по имени
hero2 = Character('Воин', 200)
print(hero == hero2)    # True (имена совпадают)

# Проверка граничных условий
try:
    Character('', 100)   # ValueError: имя пустое
except ValueError as e:
    print(e)

try:
    Character('Воин', 0) # ValueError: max_health > 0
except ValueError as e:
    print(e)

try:
    hero.take_damage(-5) # ValueError: amount > 0
except ValueError as e:
    print(e)