import os

from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from tortoise import Tortoise
from dotenv import load_dotenv

load_dotenv()


TORTOISE_ORM = {
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
            'models': ["app.users.models", "app.division.models", "aerich.models"],  #  aerich.models migration model
            'default_connection': 'default',
        }
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        # db_url="sqlite://:db.sqlite3",
        config=TORTOISE_ORM,
        modules={"models": ["app.users.models", "app.division.models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


Tortoise.init_models(["app.users.models", "app.division.models"], "models")
