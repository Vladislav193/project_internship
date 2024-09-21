# # import os
# # import pytest
# # from tortoise.contrib.test import initializer, finalizer
# from asgi_lifespan import LifespanManager
# from fastapi import FastAPI
# import pytest
# from tortoise.contrib.test import finalizer, initializer
# from tortoise import Tortoise
# from httpx import AsyncClient, ASGITransport
# # from app.main import app
# # import logging
# from contextlib import asynccontextmanager
#
# from fastapi import FastAPI
# from tortoise import Tortoise
# from tortoise.contrib.fastapi import RegisterTortoise
#
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     if getattr(app.state, "testing", False):
#         # If we're in unit tests, create a DB with a dynamic name (the {} placeholder), create schemas and drop
#         # the database when the app's lifespan ends
#         # logging.info("Initializing test db")
#         async with RegisterTortoise(
#             app=app,
#             db_url="postgres://tortoise_test:tortoise_test@127.0.0.1:5432/tortoise_test_{}",
#             modules={"models": ["app.users.models", "app.division.models"]},
#             _create_db=True,
#             generate_schemas=True,
#         ):
#             yield
#         await Tortoise._drop_databases()
#     else:
#         # logging.info("Initializing main db")
#         # Otherwise, we just use the regular DB for our regular work
#         async with RegisterTortoise(
#             app=app,
#             db_url="postgres://tortoise_test:tortoise_test@127.0.0.1:5432/tortoise_test",
#             modules={"models":["app.users.models", "app.division.models"]},
#         ):
#             yield
#
# app = FastAPI(lifespan=lifespan)
#
# # DB_URL = "postgres://user:password@localhost:5432/test_project"
#
#
# #
# # async def init_db(db_url, create_db: bool = False, schemas: bool = False):
# #     await Tortoise.init(
# #         db_url=db_url,
# #         modules={"models": ["app.users.models", "app.division.models"]}, _create_db=create_db
# #     )
# #     if create_db:
# #         print("Database created")
# #     if schemas:
# #         await Tortoise.generate_schemas()
# #         print("schemas created")
# #
# # async def init(db_url: str=DB_URL):
# #     await init_db(db_url, True, True)
# #
# @pytest.fixture(scope="session")
# def anyio_backend():
#     return "asyncio"
#
#
# @pytest.fixture(scope="session")
# async def client():
#     async with LifespanManager(app):
#         async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
#                 print("Client is ready")
#                 yield
# #
# # @pytest.fixture(scope="session")
# # async def initialize_tests():
# #     await init()
# #     yield
# #     await Tortoise._drop_databases()
# # @pytest.fixture(scope="session")
# # async def db_url():
# #     return "postgres://user:password@localhost:5432/test_project"
# #
# #
# # @pytest.fixture(scope="session")
# # async def db(db_url):
# #     print("перед инициализатором")
# #     await initializer(["app.users.models", "app.division.models"], db_url=db_url)
# #     yield
# #     print("перед финализатор")
# #     await finalizer()
# #
# #
# # @pytest.fixture(scope="function")
# # async def db_connection(db, db_url):
# #     async with Tortoise.get_connection("default"):
# #         print("торториз заработал")
# #         yield
# #
# #
#
#
#
#
#
#
# # @pytest.fixture(scope="session", autouse=True)
# # def initialize_tests(request):
# #     db_url = os.environ.get("TORTOISE_TEST_DB", "sqlite://:memory")
# #     initializer(["tests.testmodels"], db_url=db_url, app_label="models")
# #     request.addfinalizator(finalizer)
