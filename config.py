"""
    Файл создания конфигурационных классов и загрузки из .env файла переменных окружения 
"""

from dataclasses import dataclass

from environs import Env


@dataclass
class MongoConfig:
    """Класс для конфигурации базы данных MongoDB"""

    username: str
    password: str
    port: int

    database: str
    collection: str


@dataclass
class Config:
    """Общий класс конфигурации"""

    mongo: MongoConfig


def load_config():
    """
        Функция загрузки конфигурационных переменных в класс конфигурации
    """

    env = Env()
    env.read_env(".env")

    return Config(
        mongo=MongoConfig(
            username=env.str("MONGO_INITDB_ROOT_USERNAME"),
            password=env.str("MONGO_INITDB_ROOT_PASSWORD"),
            port=env.int("MONGO_INITDB_ROOT_PORT"),

            database=env.str("MONGO_DATABASE"),
            collection=env.str("MONGO_COLLECTION")
        ),
    )

config = load_config()
