import os

from tortoise import Tortoise
from dotenv import load_dotenv

load_dotenv()
# Конфигурация подключения к базе данных
DATABASE_CONFIG = {
    'connections': {
        'default': {
            'engine': os.getenv('DB_ENGINE'),
            'credentials': {
                'host': os.getenv('DB_HOST'),
                'port': os.getenv('DB_PORT'),
                'user': os.getenv('POSTGRES_USER'),
                'password': os.getenv('POSTGRES_PASSWORD'),
                'database': os.getenv('DB_DATABASE'),
            }
        },
    },
    'apps': {
        'models': {
            'models': ["app.users.models", "app.division.models", "app.task_service.models", "aerich.models"],  #  aerich.models migration model
            'default_connection': 'default',
        }
    },
}


# Асинхронная функция для инициализации Tortoise ORM
async def init():
    await Tortoise.init(config=DATABASE_CONFIG)
    await Tortoise.generate_schemas()  # Создание схем на основе моделей


# Асинхронная функция для закрытия соединений
async def close():
    await Tortoise.close_connections()