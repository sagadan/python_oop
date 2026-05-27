"""Сохранение/загрузка в JSON"""
import json, os
from datetime import datetime
from typing import List

def save_collection(collection, filepath: str) -> None:
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump([{k: v for k, v in c.__dict__.items()} for c in collection.get_all()], f, ensure_ascii=False, indent=2, default=str)

def load_collection(filepath: str, collection_class):
    coll = collection_class()
    if not os.path.exists(filepath): return coll
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for data in json.load(f):
                try:
                    from models import Character, Warrior, Mage, Archer
                    class_map = {"Воин": Warrior, "Маг": Mage, "Лучник": Archer}
                    cls = class_map.get(data.get('_class', 'Обычный персонаж'), Character)
                    # Создаем объект без вызова __init__ напрямую
                    obj = cls.__new__(cls)
                    for k, v in data.items():
                        if k.startswith('_'): setattr(obj, k, v)
                    coll.add(obj)
                except: pass
    except: pass
    return coll