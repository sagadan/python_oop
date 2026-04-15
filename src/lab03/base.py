class Character:
    """Базовый класс персонажа"""
    
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
            if self.min_intelligence <= intelligence <= self.max_intelligence:
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
    def name(self):
        """Алиас для game_name (удобство использования)"""
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
    
    # Полиморфизм
    
    def get_class_type(self):
        """Возвращает тип класса"""
        return "Обычный персонаж"
    
    def calculate_power_rating(self):
        """Расчет рейтинга силы персонажа"""
        return (self._power * 0.5 + self._intelligence * 0.3 + (self._health / 100) * 20)
    
    def is_available_for_fight(self):
        """Проверка, готов ли персонаж к бою"""
        return self._health > 20 and self._stamina > 10
    
    def get_special_bonus(self):
        """Возвращает специальный бонус класса"""
        return 0
    
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
        
        return (f" {self._game_name} [{health_status}]\n"
                f"   Здоровье: {self._health}/100 ({health_percent:.1f}%)\n"
                f"   Выносливость: {self._stamina}/40\n"
                f"   Сила: {self._power}/60\n"
                f"   Интеллект: {self._intelligence}/80")

    def __repr__(self):
        return (f"Character(game_name='{self._game_name}', "
                f"health={self._health}, stamina={self._stamina}, "
                f"power={self._power}, intelligence={self._intelligence})")

    def __eq__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        return self._game_name == other._game_name










