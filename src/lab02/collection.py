from model import Character 

class CharacterCollection:
    def __init__(self):
        "Инициализация пустой коллекции"
        self._characters = []


    def _check_type(self, character):
        "проверка типа добавляемого объекта"
        if not isinstance (character, Character):
            raise TypeError (f"Ошибка! Ожидается объект Chararacter, получен {type(character)._name_}")
        
    # Основные методы 

    def add(self, character):
        "добавить персонажа в коллекцию"
        self._check_type(character)
        if character in self._characters:
            raise ValueError('Персонаж уже был добавлен')
        self._characters.append(character)

    def remove(self, character):
        "удалить персонажа"
        self._check_type(character)
        self._characters.remove(character)

    def remove_at(self, index):
        "удалить по индексу"
        if 0 <= index <= len(self._characters):
            return self._chaarcters.pop(index)
        raise IndexError (f"Индекс не попадает в диапазон от 0 до {len(self._characters)}")
    
    def get_all(self):
        return self._characters 
    

    # Методы поиска
    
    def find_by_name (self, name: str):
        "поиск персонажа по имени"
        for character in self._characters:
            if character.game_name.lower() == name.lower():
                return character
        return None
    
    def find_by_health_range(self, min_health: int = 0, max_health: int = 100):
        "поиск персонажей в заданном диапазоне здоровья"
        result = []
        for character in self._characters:
            if min_health <= character.health <= max_health:
                result.append(character)
        return result 
    
    def find_by_power_range (self, min_power: int = 1, max_power: int = 60):
        "поиск персонажей в заданном диапазоне силы"
        result = []
        for character in self._characters:
            if min_power <= character.power <= max_power:
                result.append(character)
        return result 
    
    # Фильтрация

    def get_healthy (self, min_health: int = 50):
        "возвращает новую коллекцию с здоровыми песронажами"
        new_collection = CharacterCollection()
        for character in self._characters:
            if character.health >= min_health:
                new_collection.add(character)
        return new_collection 
    
    def get_strong (self, min_power: int = 30):
        "возвращает новую коллекцию с сильными персонажами"
        new_collection = CharacterCollection()
        for character in self._characters:
            if character.power >= min_power:
                new_collection.add(character)
        return new_collection 
    

    # Сортировка

    def sort_by_name(self, reverse=False):
        "Сортировка по имени"
        self._characters.sort(key=lambda c: c.game_name.lower(), reverse=reverse)
    
    def sort_by_power(self, reverse=False):
        """Сортировка по силе"""
        self._characters.sort(key=lambda c: c.power, reverse=reverse)

    # Магические методы

    def __str__(self):
        "строковое представение коллекции для пользователей"
        result = ""
        for char in self._characters:
            result += str(char) + "\n"
        return result
        
    def __len__(self):
        "возвращает количсетво персонажей в коллекции"
        return len(self._characters)
    
    def __iter__(self):
        "возвращает итератор по коллекции"
        return iter(self._characters)
    
    def __getitem__(self, index):
        "доступ к перонажу по индексу"
        return self._characters[index]
    

            



    

        


