"""Доступ к базе данных"""

import logging

from pymongo import MongoClient

from config import config
            

logger = logging.getLogger(__file__)

def get_coolections():
    """Функция подключения к базе данных Mongo DB"""

    try:
        mongo_uri=f"mongodb://{config.mongo.username}:{config.mongo.password}@mongo_app:{config.mongo.port}/"

        client = MongoClient(mongo_uri)
        db = client[config.mongo.database]
        templates_collection = db[config.mongo.collection]

        return templates_collection

    except Exception as e:
        logger.info("Error in connection to DB: %s", e)