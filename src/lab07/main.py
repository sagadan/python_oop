"""
Главный модуль - точка входа в приложение
"""

import sys
import os

# Добавляем путь к модулям
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli import CliInterface
from app import CharacterApp
from models import CharacterCollection


def main() -> None:
    """
    Главная функция приложения
    """
    # Инициализация приложения
    collection = CharacterCollection()
    app = CharacterApp(collection)
    
    # Запуск CLI
    cli = CliInterface(app, "characters.json")
    
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
        # Сохраняем данные при прерывании
        try:
            from storage import save_collection
            save_collection(app.collection, "characters.json")
            print("Данные сохранены.")
        except:
            pass
        sys.exit(0)


if __name__ == "__main__":
    main()