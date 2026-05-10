from model import Warrior, Mage, Archer

class StrategyByName:
    "Стратегия: вывод по имени"
    def __call__(self, character):
        return f"Персонаж {character.game_name}"

class StrategyByClass:
    "Стратегия: вывод по классу"
    def __call__(self, character):
        return f"{character.game_name} - {character.get_class_type()}"

class StrategyByHealth:
    "Стратегия: вывод по здоровью"
    def __call__(self, character):
        status = "здоров" if character.health > 50 else "ранен"
        return f"{character.game_name}: {status} ({character.health})"


def filter_warrior(character):
    "Только воины"
    return isinstance(character, Warrior)

def filter_mage(character):
    "Только маги"
    return isinstance(character, Mage)

def filter_healthy(character):
    "Здоровые (>50 здоровья)"
    return character.health > 50

def filter_powerful(character):
    "Сильные (>30 силы)"
    return character.power > 30



def make_health_filter(min_health):
    "Создаёт фильтр по минимальному здоровью"
    return lambda c: c.health >= min_health

def make_power_filter(min_power):
    "Создаёт фильтр по минимальной силе"
    return lambda c: c.power >= min_power


