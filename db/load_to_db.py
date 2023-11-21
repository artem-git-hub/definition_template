import json
from pymongo import MongoClient

from mongo_service import get_coolections
from server import app

@app.on_event("startup")
def load_to_db():
    """Запись базовых шаблонов из файла в БД"""

    with open("templates.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    collection = get_coolections()

    collection.insert_many(data)
