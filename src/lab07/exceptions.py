class CharacterNotFoundError(Exception):
    """Исключение: персонаж не найден в коллекции"""
    
    def __init__(self, name: str = ""):
        self.name = name
        if name:
            super().__init__(f"Персонаж '{name}' не найден в коллекции.")
        else:
            super().__init__("Персонаж не найден в коллекции.")


class DuplicateCharacterError(Exception):
    """Исключение: персонаж с таким именем уже существует"""
    
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Персонаж с именем '{name}' уже существует в коллекции.")


class InvalidCharacterDataError(Exception):
    """Исключение: неверные данные персонажа"""
    
    def __init__(self, message: str):
        super().__init__(f"Неверные данные персонажа: {message}")


class InvalidClassTypeError(Exception):
    """Исключение: неверный тип класса персонажа"""
    
    def __init__(self, class_type: str):
        self.class_type = class_type
        super().__init__(f"Неверный тип класса персонажа: '{class_type}'. "
                        f"Доступные типы: Воин, Маг, Лучник")