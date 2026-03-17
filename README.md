# Лабораторная работа №1

### Атрибуты класса

<img width="291" height="240" alt="атрибуты класса" src="https://github.com/user-attachments/assets/32790221-7d1f-4c0c-9886-c1627725d146" />

### Закрытые атрибуты экземпляра

<img width="842" height="679" alt="Снимок экрана 2026-03-17 в 23 34 38" src="https://github.com/user-attachments/assets/03e9c947-be72-4c0a-b03c-35233c55c9bf" />



## Декоратор @property
<img width="883" height="350" alt="image" src="https://github.com/user-attachments/assets/42440939-5052-4151-95d4-e11ca6c29ca9" />


## Метод-сеттер (setter)
<img width="875" height="740" alt="Снимок экрана 2026-03-17 в 23 12 32" src="https://github.com/user-attachments/assets/4c7467fd-5551-4ac0-a972-4f10ed14f54e" />

### Бизес-методы

- **`attack`** - Атака другого персонажа
- **`magic_attack`** - Магическая атака другого персонажа

<img width="829" height="518" alt="Снимок экрана 2026-03-17 в 23 26 43" src="https://github.com/user-attachments/assets/76e61fa3-bbe1-4d1a-9f28-e6e82d7b8de0" />

### Магические методы

- **`__str__`** — неформальное строковое представление объекта для пользователей (например, для `print()`)
- **`__repr__`** — официальное строковое представление для разработчиков (отладочная информация)
- **`__eq__`** — переопределяет оператор равенства `==`, задает логику сравнения объектов

<img width="572" height="478" alt="Снимок экрана 2026-03-17 в 23 40 05" src="https://github.com/user-attachments/assets/9761d0fd-b47f-43f4-a31b-c86e8327c2a5" />


## Model.py

```
class Character: 

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
        
        # Здоровье
        if isinstance(health, (int, float)):
            if self.min_health <= health <= self.max_health:  
                self._health = health 
            else:
                raise ValueError(f'Ошибка! Здоровье должно быть от {self.min_health} до {self.max_health}.')
        else:
            raise TypeError('Ошибка! Здоровье должно быть числом.')
        
        # Выносливость
        if isinstance(stamina, (int, float)):
            if self.min_stamina <= stamina <= self.max_stamina:  
                self._stamina = stamina
            else:
                raise ValueError(f'Ошибка! Выносливость должна быть от {self.min_stamina} до {self.max_stamina}.')
        else:
            raise TypeError('Ошибка! Выносливость должна быть числом.')
        
        # Сила
        if isinstance(power, (int, float)):
            if self.min_power <= power <= self.max_power:  
                self._power = power
            else:
                raise ValueError(f'Ошибка! Сила должна быть от {self.min_power} до {self.max_power}.')
        else:
            raise TypeError('Ошибка! Сила должна быть числом.')
        
        # Интеллект
        if isinstance(intelligence, (int, float)):
            if self.min_intelligence <= intelligence <= self.max_intelligence:  #
                self._intelligence = intelligence
            else:
                raise ValueError(f'Ошибка! Интеллект должен быть от {self.min_intelligence} до {self.max_intelligence}.')
        else:
            raise TypeError('Ошибка! Интеллект должен быть числом.')
    
    # Геттеры
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
    
    # Сеттеры
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
    
    # Бизнес-методы
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
    
    # Магические методы 
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
        
        return (f"⚔️ {self._game_name} [{health_status}]\n"
                f"   Здоровье: {self._health}/100 ({health_percent:.1f}%)\n"
                f"   Выносливость: {self._stamina}/40\n"
                f"   Сила: {self._power}/60\n"
                f"   Интеллект: {self._intelligence}/80")
    

    def __repr__(self):
        """Официальное строковое представление персонажа"""
        return (f"Character(game_name='{self._game_name}', "
                f"health={self._health}, stamina={self._stamina}, "
                f"power={self._power}, intelligence={self._intelligence})")

    def __eq__(self, other):
        """Сравнение персонажей по имени (игровой никнейм уникален)"""
        if not isinstance(other, Character):
            return NotImplemented
        return self._game_name == other._game_name
```


## demo.py

```
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
    print("   ✅ Воин и Маг созданы")
    
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
    print("\n9. Бизнес-методы:")
    
    # Атаки
    print(f"   {warrior.attack(mage)}")
    print(f"   {mage.magic_attack(warrior)}")
    
    # 9. ФИНАЛЬНОЕ СОСТОЯНИЕ
    print("\n10. Итоговое состояние:")
    print(warrior)
    print(mage)
    
    print("\n" + "=" * 60)
    print("Демонстрация завершена")
    print("=" * 60)


if __name__ == "__main__":
    demo()
```
