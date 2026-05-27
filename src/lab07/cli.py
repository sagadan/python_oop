from __future__ import annotations

from typing import Optional, List

from app import CharacterApp
from models import Character, Warrior, Mage, Archer
from exceptions import (
    CharacterNotFoundError,
    DuplicateCharacterError,
    InvalidClassTypeError
)
from storage import save_collection, load_collection
from models import CharacterCollection


class CliInterface:
    
    def __init__(self, app: CharacterApp, data_file: str = "characters.json") -> None:
        
        self._app: CharacterApp = app
        self._data_file: str = data_file

    def run(self) -> None:
        
        print("\n" + "=" * 72)
        print("Консольное приложение")
        print("=" * 72)
        print(f"Автоматически загружено объектов: {len(self._app.get_all_characters())}")

        commands = {
            1: self._add_character,
            2: self._show_all,
            3: self._find_by_name,
            4: self._filter_menu,
            5: self._sort_menu,
            6: self._delete_by_name,
            7: self._show_stats,
            8: self._clear_collection,
            9: self._save_now
        }

        while True:
            self._print_menu()

            choice = self._read_int("Выберите пункт: ")

            if choice == 0:
                self._exit_program()
                break

            command = commands.get(choice)

            if command is None:
                print("Ошибка: такого пункта меню нет.")
                continue

            command()

    def _print_menu(self) -> None:
        """
        Выводит главное меню приложения.
        """
        print("""
------------------------------------------------------------------------
1. Добавить персонажа
2. Показать всех персонажей
3. Найти персонажа по имени
4. Фильтрация персонажей
5. Сортировка персонажей
6. Удалить персонажа по имени
7. Показать статистику
8. Очистить коллекцию
9. Сохранить данные
0. Выход
------------------------------------------------------------------------
""")

    def _add_character(self) -> None:
        
        print("\nДобавление персонажа")
        print("Введите 0 на любом шаге, чтобы вернуться в главное меню.\n")

        # Выбор класса
        print("Выберите класс персонажа:")
        print("1. Обычный персонаж")
        print("2. Воин")
        print("3. Маг")
        print("4. Лучник")
        print("0. Назад")

        class_choice = self._read_int("Ваш выбор: ")
        if class_choice == 0:
            return
        if class_choice not in [1, 2, 3, 4]:
            print("Ошибка: неверный выбор класса.")
            return

        # Общие атрибуты
        name = self._read_text("Имя персонажа: ", allow_back=True)
        if name is None:
            return

        health = self._read_positive_int("Здоровье (0-100): ", max_val=100, allow_back=True)
        if health is None:
            return

        stamina = self._read_positive_int("Выносливость (0-40): ", max_val=40, allow_back=True)
        if stamina is None:
            return

        power = self._read_positive_int("Сила (1-60): ", min_val=1, max_val=60, allow_back=True)
        if power is None:
            return

        intelligence = self._read_positive_int("Интеллект (1-80): ", min_val=1, max_val=80, allow_back=True)
        if intelligence is None:
            return

        try:
            if class_choice == 1:  # Обычный персонаж
                character = Character(name, health, stamina, power, intelligence)

            elif class_choice == 2:  # Воин
                weapon = self._read_text("Оружие: ", allow_back=True)
                if weapon is None:
                    return
                armor = self._read_positive_int("Рейтинг брони (1-10): ", min_val=1, max_val=10, allow_back=True)
                if armor is None:
                    return
                character = Warrior(name, health, stamina, power, intelligence, weapon, armor)

            elif class_choice == 3:  # Маг
                magic_school = self._read_text("Школа магии: ", allow_back=True)
                if magic_school is None:
                    return
                mana = self._read_positive_int("Мана (0-200): ", min_val=0, max_val=200, allow_back=True)
                if mana is None:
                    return
                character = Mage(name, health, stamina, power, intelligence, magic_school, mana)

            else:  # Лучник
                bow_type = self._read_text("Тип лука: ", allow_back=True)
                if bow_type is None:
                    return
                accuracy = self._read_positive_int("Точность (1-100): ", min_val=1, max_val=100, allow_back=True)
                if accuracy is None:
                    return
                character = Archer(name, health, stamina, power, intelligence, bow_type, accuracy)

            self._app.add_character(character)
            print(f"Персонаж '{name}' успешно добавлен.")

        except (DuplicateCharacterError, ValueError, TypeError) as error:
            print(f"Ошибка: {error}")

    def _show_all(self) -> None:
        characters = self._app.get_all_characters()
        self._print_characters(characters, "Все персонажи")

    def _find_by_name(self) -> None:
        
        print("\nПоиск персонажа")
        print("Введите 0, чтобы вернуться в главное меню.\n")

        name = self._read_text("Введите имя для поиска: ", allow_back=True)

        if name is None:
            return

        try:
            character = self._app.find_character_by_name(name)
            self._print_characters([character], "Найденный персонаж")

        except CharacterNotFoundError as error:
            print(f"Ошибка: {error}")

    def _delete_by_name(self) -> None:
        
        print("\nУдаление персонажа")
        print("Введите 0, чтобы вернуться в главное меню.\n")

        name = self._read_text("Введите имя для удаления: ", allow_back=True)

        if name is None:
            return

        try:
            character = self._app.find_character_by_name(name)
            self._print_characters([character], "Персонаж для удаления")

            confirm = self._read_bool(
                f'Удалить персонажа "{character.game_name}"? (y/n, 0 — назад): ',
                allow_back=True
            )

            if confirm is None:
                return

            if confirm:
                self._app.remove_character(name)
                print("Персонаж удалён.")
            else:
                print("Удаление отменено.")

        except CharacterNotFoundError as error:
            print(f"Ошибка: {error}")

    def _filter_menu(self) -> None:
        
        while True:
            print("""
------------------------------------------------------------------------
Фильтрация
1. По классу
2. По здоровью (здоровые > 50)
3. По силе (сильные > 30)
4. По диапазону здоровья
5. По диапазону силы
0. Назад
------------------------------------------------------------------------
""")

            choice = self._read_int("Выберите вариант фильтрации: ")

            if choice == 0:
                return

            if choice == 1:
                self._filter_by_class()
                return

            if choice == 2:
                characters = self._app.filter_by_health()
                self._print_characters(characters, "Здоровые персонажи (HP > 50)")
                return

            if choice == 3:
                characters = self._app.filter_by_power()
                self._print_characters(characters, "Сильные персонажи (PWR > 30)")
                return

            if choice == 4:
                self._filter_by_health_range()
                return

            if choice == 5:
                self._filter_by_power_range()
                return

            print("Ошибка: неверный вариант фильтрации.")

    def _filter_by_class(self) -> None:
        
        print("\nВыберите класс:")
        print("1. Воин")
        print("2. Маг")
        print("3. Лучник")
        print("0. Назад")

        class_choice = self._read_int("Ваш выбор: ")

        if class_choice == 0:
            return

        class_map = {1: 'Воин', 2: 'Маг', 3: 'Лучник'}

        if class_choice not in class_map:
            print("Ошибка: неверный выбор класса.")
            return

        try:
            characters = self._app.filter_by_class(class_map[class_choice])
            self._print_characters(characters, f"Персонажи - {class_map[class_choice]}")
        except InvalidClassTypeError as error:
            print(f"Ошибка: {error}")

    def _filter_by_health_range(self) -> None:
        
        print("\nФильтр по диапазону здоровья")
        print("Введите 0, чтобы вернуться в главное меню.\n")

        min_health = self._read_positive_int("Минимальное здоровье (0-100): ", min_val=0, max_val=100, allow_back=True)
        if min_health is None:
            return

        max_health = self._read_positive_int("Максимальное здоровье: ", min_val=min_health, max_val=100, allow_back=True)
        if max_health is None:
            return

        characters = self._app.find_characters_by_health_range(min_health, max_health)
        self._print_characters(characters, f"Персонажи (HP: {min_health}-{max_health})")

    def _filter_by_power_range(self) -> None:
        
        print("\nФильтр по диапазону силы")
        print("Введите 0, чтобы вернуться в главное меню.\n")

        min_power = self._read_positive_int("Минимальная сила (1-60): ", min_val=1, max_val=60, allow_back=True)
        if min_power is None:
            return

        max_power = self._read_positive_int("Максимальная сила: ", min_val=min_power, max_val=60, allow_back=True)
        if max_power is None:
            return

        characters = self._app.find_characters_by_power_range(min_power, max_power)
        self._print_characters(characters, f"Персонажи (PWR: {min_power}-{max_power})")

    def _sort_menu(self) -> None:
        
        while True:
            print("""
------------------------------------------------------------------------
Сортировка
1. По имени
2. По здоровью
3. По силе
4. По интеллекту
5. По выносливости
6. По классу
7. По рейтингу силы
8. По дате создания
0. Назад
------------------------------------------------------------------------
""")

            choice = self._read_int("Выберите вариант сортировки: ")

            if choice == 0:
                return

            sort_map = {
                1: 'name', 2: 'health', 3: 'power', 4: 'intelligence',
                5: 'stamina', 6: 'class', 7: 'power_rating', 8: 'created_at'
            }

            if choice not in sort_map:
                print("Ошибка: неверный вариант сортировки.")
                continue

            reverse = self._read_bool("Сортировать по убыванию? (y/n): ")

            try:
                self._app.sort_characters(sort_map[choice], reverse)
                characters = self._app.get_all_characters()
                self._print_characters(characters, f"Сортировка по {sort_map[choice]}")
            except ValueError as error:
                print(f"Ошибка: {error}")

            return

    def _show_stats(self) -> None:
        
        stats = self._app.get_stats()

        print("\n" + "=" * 50)
        print(" " * 15 + "СТАТИСТИКА КОЛЛЕКЦИИ")
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
        
        count = len(self._app.get_all_characters())

        if count == 0:
            print("Коллекция уже пуста.")
            return

        confirm = self._read_bool(f"ВНИМАНИЕ! Будет удалено {count} персонаж(ей). Продолжить? (y/n): ")

        if confirm:
            self._app.clear_collection()
            print(f"Коллекция очищена. Удалено {count} персонаж(ей).")
        else:
            print("Операция отменена.")

    def _save_now(self) -> None:
        
        try:
            save_collection(self._app.collection, "characters.json")
            print("Данные успешно сохранены.")
        except Exception as error:
            print(f"Ошибка сохранения: {error}")

    def _exit_program(self) -> None:
        
        try:
            save_collection(self._app.collection, "characters.json")
            print("Данные сохранены.")
            print("Завершение работы программы.")
        except Exception as error:
            print(f"Ошибка сохранения: {error}")
            print("Программа завершена без сохранения.")

    def _print_characters(
        self,
        characters: List[Character],
        title: str
    ) -> None:
        
        print("\n" + title)

        if not characters:
            print("Список пуст.")
            return

        # Функция для получения короткого названия класса
        def get_class_short(c: Character) -> str:
            t = c.get_class_type()
            if t == "Воин":
                return "Воин"
            elif t == "Маг":
                return "Маг"
            elif t == "Лучник":
                return "Луч"
            else:
                return "Обыч"

        print("-" * 68)
        print(f"{'№':<4}{'Имя':<20}{'Класс':<8}{'HP':>6}{'STA':>6}{'PWR':>6}{'INT':>6}")
        print("-" * 68)

        for index, character in enumerate(characters, start=1):
            print(
                f"{index:<4}"
                f"{character.game_name:<20}"
                f"{get_class_short(character):<8}"
                f"{character.health:>6}"
                f"{character.stamina:>6}"
                f"{character.power:>6}"
                f"{character.intelligence:>6}"
            )

        print("-" * 68)

    def _read_text(
        self,
        prompt: str,
        allow_back: bool = False
    ) -> Optional[str]:
        
        while True:
            raw_value = input(prompt).strip()

            if allow_back and raw_value == "0":
                return None

            if raw_value:
                return raw_value

            print("Ошибка: строка не может быть пустой.")

    def _read_int(
        self,
        prompt: str
    ) -> int:
        
        while True:
            raw_value = input(prompt).strip()

            try:
                return int(raw_value)

            except ValueError:
                print("Ошибка: введите целое число.")

    def _read_positive_int(
        self,
        prompt: str,
        min_val: int = 1,
        max_val: Optional[int] = None,
        allow_back: bool = False
    ) -> Optional[int]:
        
        while True:
            raw_value = input(prompt).strip()

            if allow_back and raw_value == "0":
                return None

            try:
                value = int(raw_value)

            except ValueError:
                print("Ошибка: введите целое число.")
                continue

            if value < min_val:
                print(f"Ошибка: значение должно быть не меньше {min_val}.")
                continue

            if max_val is not None and value > max_val:
                print(f"Ошибка: значение должно быть не больше {max_val}.")
                continue

            return value

    def _read_bool(
        self,
        prompt: str,
        allow_back: bool = False
    ) -> Optional[bool]:
    
        while True:
            raw_value = input(prompt).strip().lower()

            if allow_back and raw_value == "0":
                return None

            if raw_value in {"y", "yes", "д", "да", "1"}:
                return True

            if raw_value in {"n", "no", "н", "нет"}:
                return False

            print("Ошибка: введите y/n, да/нет или 0 для возврата.")