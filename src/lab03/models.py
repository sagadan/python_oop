from base import Character


class Warrior(Character):
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
    
    # Переопределение метода
    def attack(self, target):
        if not isinstance(target, Character):
            raise TypeError('Ошибка!')
        if self.stamina < 5:
            return f"{self.game_name} слишком устал"
        
        damage = (self.power * 2) + 10
        target.health = max(0, target.health - damage)
        self.stamina -= 5
        
        return f"{self.game_name} атакует {target.game_name} и наносит {damage} урона!"
    
    def calculate_power_rating(self):
        return self.power * 0.7 + self.armor_rating * 0.3
    
    def get_class_type(self):
        return "Воин"
    
    def __str__(self):
        return (f"{self.game_name} (Воин)\n"
                f"  Здоровье: {self.health}\n"
                f"  Сила: {self.power}\n"
                f"  Оружие: {self.weapon}\n"
                f"  Броня: {self.armor_rating}")


class Mage(Character):
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
    
    def calculate_power_rating(self):
        return self.intelligence * 0.8 + len(self.spells) * 5
    
    def get_class_type(self):
        return "Маг"
    
    def __str__(self):
        return f"{self.game_name} (Маг)\n  Интеллект: {self.intelligence}\n  Мана: {self.mana}"


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
    
    def calculate_power_rating(self):
        return self.power * 0.6 + self.accuracy * 0.4
    
    def get_class_type(self):
        return "Лучник"
    
    def __str__(self):
        return f"{self.game_name} (Лучник)\n  Сила: {self.power}\n  Точность: {self.accuracy}%"