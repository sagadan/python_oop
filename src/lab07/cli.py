"""
Модуль интерфейса командной строки (CLI)
"""

from typing import Optional, List
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import CharacterApp
from models import Character, CharacterCollection, Warrior, Mage, Archer
from exceptions import CharacterNotFoundError, DuplicateCharacterError, InvalidClassTypeError
from storage import save_collection, load_collection


class CliInterface:
    
    def __init__(self, app: CharacterApp, data_file: str = "characters.json"):
        self._app = app
        self._data_file = data_file
        self._running = True
    
    def _print_menu(self) -> None:
        print("\n" + "=" * 60)
        print(" " * 20 + "Управление персонажами")
        print("=" * 60)
        print(" 1. Добавить персонажа")
        print(" 2. Показать всех персонажей")
        print(" 3. Найти персонажа по имени")
        print(" 4. Фильтрация персонажей")
        print(" 5. Сортировка персонажей")
        print(" 6. Удалить персонажа")
        print(" 7. Показать статистику")
        print(" 8. Очистить коллекцию")
        print(" 0. Выход")
        print("=" * 60)
    
    def _get_int_input(self, prompt: str, min_val: int = None, max_val: int = None) -> Optional[int]:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Ошибка: значение должно быть не меньше {min_val}")
                return None
            if max_val is not None and value > max_val:
                print(f"Ошибка: значение должно быть не больше {max_val}")
                return None
            return value
        except ValueError:
            print("Ошибка: введите целое число")
            return None
    
    def _print_characters_table(self, characters: List[Character], title: str = "ПЕРСОНАЖИ") -> None:
        """Вывод списка персонажей в виде таблицы"""
        if not characters:
            print("\nНет персонажей для отображения.")
            return
        
        # Функция для получения короткого названия класса
        def get_class_short(c):
            t = c.get_class_type()
            if t == "Воин":
                return "Воин"
            elif t == "Маг":
                return "Маг"
            elif t == "Лучник":
                return "Луч"
            else:
                return "Обыч"
        
        # Находим максимальную длину имени
        max_name_len = 4
        for c in characters:
            name_len = len(c.game_name)
            if name_len > max_name_len:
                max_name_len = min(name_len, 15)
        
        # Ширина колонок
        col_num = 3
        col_name = max_name_len + 2
        col_class = 6
        col_stat = 4
        
        total = col_num + col_name + col_class + col_stat * 4 + 13
        
        # Верхняя граница
        print("\n" + "─" * total)
        print(f"{title:^{total}}")
        print("─" * total)
        
        # Заголовки
        print(f"│ {'№':<{col_num}} │ {'Имя':<{col_name}} │ {'Класс':^{col_class}} │ "
              f"{'HP':^{col_stat}} │ {'STA':^{col_stat}} │ {'PWR':^{col_stat}} │ {'INT':^{col_stat}} │")
        print("─" * total)
        
        # Данные
        for i, c in enumerate(characters, 1):
            name = c.game_name
            if len(name) > col_name:
                name = name[:col_name-2] + ".."
            
            class_short = get_class_short(c)
            
            print(f"│ {i:<{col_num}} │ {name:<{col_name}} │ {class_short:^{col_class}} │ "
                  f"{c.health:>{col_stat}} │ {c.stamina:>{col_stat}} │ "
                  f"{c.power:>{col_stat}} │ {c.intelligence:>{col_stat}} │")
        
        # Нижняя граница
        print("─" * total)
        print(f"Всего: {len(characters)} персонаж(ей)")
    
    def _add_character(self) -> None:
        print("\n" + "-" * 40)
        print("Добавление нового персонажа")
        print("-" * 40)
        
        print("\nВыберите класс персонажа:")
        print(" 1. Обычный персонаж")
        print(" 2. Воин")
        print(" 3. Маг")
        print(" 4. Лучник")
        
        class_choice = self._get_int_input("Ваш выбор (1-4): ", 1, 4)
        if class_choice is None:
            return
        
        name = input("Имя персонажа: ").strip()
        if not name:
            print("Ошибка: имя не может быть пустым")
            return
        
        health = self._get_int_input("Здоровье (0-100): ", 0, 100)
        if health is None:
            return
        
        stamina = self._get_int_input("Выносливость (0-40): ", 0, 40)
        if stamina is None:
            return
        
        power = self._get_int_input("Сила (1-60): ", 1, 60)
        if power is None:
            return
        
        intelligence = self._get_int_input("Интеллект (1-80): ", 1, 80)
        if intelligence is None:
            return
        
        try:
            if class_choice == 1:
                character = Character(name, health, stamina, power, intelligence)
            elif class_choice == 2:
                weapon = input("Оружие: ").strip()
                armor = self._get_int_input("Рейтинг брони (1-10): ", 1, 10)
                if armor is None:
                    return
                character = Warrior(name, health, stamina, power, intelligence, weapon, armor)
            elif class_choice == 3:
                magic_school = input("Школа магии: ").strip()
                mana = self._get_int_input("Мана (0-200): ", 0, 200)
                if mana is None:
                    return
                character = Mage(name, health, stamina, power, intelligence, magic_school, mana)
            else:
                bow_type = input("Тип лука: ").strip()
                accuracy = self._get_int_input("Точность (1-100): ", 1, 100)
                if accuracy is None:
                    return
                character = Archer(name, health, stamina, power, intelligence, bow_type, accuracy)
            
            self._app.add_character(character)
            print(f"\n✓ Персонаж '{name}' успешно добавлен!")
            
        except DuplicateCharacterError as e:
            print(f"\n✗ Ошибка: {e}")
        except (ValueError, TypeError) as e:
            print(f"\n✗ Ошибка: {e}")
    
    def _show_all_characters(self) -> None:
        self._print_characters_table(self._app.get_all_characters(), "Все персонажи")
    
    def _find_character(self) -> None:
        print("\n" + "-" * 40)
        print("Поиск персонажа")
        print("-" * 40)
        
        name = input("Введите имя персонажа: ").strip()
        if not name:
            print("Ошибка: имя не может быть пустым")
            return
        
        character = self._app.find_character_by_name(name)
        if character:
            print("\n" + "=" * 40)
            print(str(character))
            print("=" * 40)
        else:
            print(f"\n✗ Персонаж с именем '{name}' не найден.")
    
    def _filter_characters(self) -> None:
        print("\n" + "-" * 40)
        print("Фильтрация персонажей")
        print("-" * 40)
        print(" 1. По классу")
        print(" 2. По здоровью (здоровые > 50)")
        print(" 3. По силе (сильные > 30)")
        print(" 4. По диапазону здоровья")
        print(" 5. По диапазону силы")
        print(" 0. Назад")
        
        choice = self._get_int_input("Ваш выбор: ", 0, 5)
        if choice is None or choice == 0:
            return
        
        try:
            if choice == 1:
                print("\nВыберите класс:")
                print(" 1. Воин")
                print(" 2. Маг")
                print(" 3. Лучник")
                class_choice = self._get_int_input("Ваш выбор (1-3): ", 1, 3)
                if class_choice is None:
                    return
                class_map = {1: 'Воин', 2: 'Маг', 3: 'Лучник'}
                characters = self._app.filter_by_class(class_map[class_choice])
                self._print_characters_table(characters, f"Персонажи - {class_map[class_choice]}")
            elif choice == 2:
                characters = self._app.filter_by_health()
                self._print_characters_table(characters, "Здоровые персонажи (HP > 50)")
            elif choice == 3:
                characters = self._app.filter_by_power()
                self._print_characters_table(characters, "Сильные персонажи (PWR > 30)")
            elif choice == 4:
                min_health = self._get_int_input("Минимальное здоровье (0-100): ", 0, 100)
                if min_health is None:
                    return
                max_health = self._get_int_input("Максимальное здоровье (0-100): ", min_health, 100)
                if max_health is None:
                    return
                characters = self._app.find_characters_by_health_range(min_health, max_health)
                self._print_characters_table(characters, f"Персонажи (HP: {min_health}-{max_health})")
            elif choice == 5:
                min_power = self._get_int_input("Минимальная сила (1-60): ", 1, 60)
                if min_power is None:
                    return
                max_power = self._get_int_input("Максимальная сила (1-60): ", min_power, 60)
                if max_power is None:
                    return
                characters = self._app.find_characters_by_power_range(min_power, max_power)
                self._print_characters_table(characters, f"Персонажи (PWR: {min_power}-{max_power})")
        except InvalidClassTypeError as e:
            print(f"\n✗ Ошибка: {e}")
    
    def _sort_characters(self) -> None:
        print("\n" + "-" * 40)
        print("Сортировка персонажей")
        print("-" * 40)
        print(" 1. По имени")
        print(" 2. По здоровью")
        print(" 3. По силе")
        print(" 4. По интеллекту")
        print(" 5. По выносливости")
        print(" 6. По классу")
        print(" 7. По рейтингу силы")
        print(" 8. По дате создания")
        print(" 0. Назад")
        
        choice = self._get_int_input("Ваш выбор: ", 0, 8)
        if choice is None or choice == 0:
            return
        
        sort_map = {
            1: 'name', 2: 'health', 3: 'power', 4: 'intelligence',
            5: 'stamina', 6: 'class', 7: 'power_rating', 8: 'created_at'
        }
        
        order = input("Сортировать по убыванию? (yes/no): ").strip().lower()
        reverse = order == 'yes'
        
        try:
            self._app.sort_characters(sort_map[choice], reverse)
            print("\n✓ Сортировка выполнена!")
            self._show_all_characters()
        except ValueError as e:
            print(f"\n✗ Ошибка: {e}")
    
    def _remove_character(self) -> None:
        print("\n" + "-" * 40)
        print("Удаление персонажа")
        print("-" * 40)
        
        name = input("Введите имя персонажа для удаления: ").strip()
        if not name:
            print("Ошибка: имя не может быть пустым")
            return
        
        character = self._app.find_character_by_name(name)
        if not character:
            print(f"\n✗ Персонаж с именем '{name}' не найден.")
            return
        
        print(f"\nПерсонаж найден:")
        print(str(character))
        
        confirm = input(f"\nУдалить персонажа '{name}'? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Удаление отменено.")
            return
        
        try:
            removed = self._app.remove_character(name)
            print(f"\n✓ Персонаж '{removed.game_name}' успешно удален!")
        except CharacterNotFoundError as e:
            print(f"\n✗ Ошибка: {e}")
    
    def _show_stats(self) -> None:
        stats = self._app.get_stats()
        
        print("\n" + "=" * 50)
        print(" " * 15 + "Статистика коллекции")
        print("=" * 50)
        print(f" Всего персонажей:      {stats['total']}")
        print(f" Среднее здоровье:      {stats['avg_health']:.1f}")
        print(f" Средняя сила:          {stats['avg_power']:.1f}")
        print(f" Средний интеллект:     {stats['avg_intelligence']:.1f}")
        print("-" * 50)
        print(f" Воинов:                {stats['warriors']}")
        print(f" Магов:                 {stats['mages']}")
        print(f" Лучников:              {stats['archers']}")
        print("=" * 50)
    
    def _clear_collection(self) -> None:
        print("\n" + "-" * 40)
        print("Очистка коллекции")
        print("-" * 40)
        
        count = len(self._app.get_all_characters())
        if count == 0:
            print("Коллекция уже пуста.")
            return
        
        confirm = input(f"\nВнимание! Будет удалено {count} персонаж(ей). Продолжить? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Операция отменена.")
            return
        
        self._app.clear_collection()
        print(f"\n✓ Коллекция очищена. Удалено {count} персонаж(ей).")
    
    def _save_data(self) -> None:
        try:
            save_collection(self._app.collection, self._data_file)
            print(f"\n✓ Данные сохранены в файл '{self._data_file}'")
        except Exception as e:
            print(f"\n✗ Ошибка при сохранении: {e}")
    
    def _load_data(self) -> None:
        try:
            loaded_collection = load_collection(self._data_file, CharacterCollection)
            self._app._collection = loaded_collection
            count = len(self._app.get_all_characters())
            print(f"\n✓ Загружено {count} персонаж(ей) из файла '{self._data_file}'")
        except Exception as e:
            print(f"\n✗ Ошибка при загрузке: {e}")
    
    def run(self) -> None:
        print("\n" + "=" * 60)
        print(" " * 15 + "Добро пожаловать в систему управления песронажами")
        print("=" * 60)
        
        self._load_data()
        
        while self._running:
            self._print_menu()
            choice = self._get_int_input("Выберите пункт меню (0-8): ", 0, 8)
            
            if choice == 0:
                self._save_data()
                print("\nДо свидания!")
                self._running = False
            elif choice == 1:
                self._add_character()
            elif choice == 2:
                self._show_all_characters()
            elif choice == 3:
                self._find_character()
            elif choice == 4:
                self._filter_characters()
            elif choice == 5:
                self._sort_characters()
            elif choice == 6:
                self._remove_character()
            elif choice == 7:
                self._show_stats()
            elif choice == 8:
                self._clear_collection()
            
            if self._running:
                input("\nНажмите Enter для продолжения...")