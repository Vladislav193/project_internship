from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI


TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'user': 'postgres',
                'password': '12345',
                'database': 'postgres',
            }
        },
    },
    'apps': {
        'models': {
            'models': ["app.models", "aerich.models"],  #  aerich.models migration model
            'default_connection': 'default',
        }
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        # db_url="sqlite://:db.sqlite3",
        config=TORTOISE_ORM,
        modules={"models": ["app.models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

