import pytest

from httpx import AsyncClient,ASGITransport
from fastapi import FastAPI
from tortoise import Tortoise
from app.main import app  # Замените на путь к вашему файлу main.py

@pytest.fixture
async def setup_db():
    await Tortoise.init(
        db_url="postgres://postgres:12345@localhost:5432/test_database_name",
        modules={"models": ["app.users.models", "app.division.models"]},
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()

transport = ASGITransport(app=app)
@pytest.mark.anyio
async def test_post_division(setup_db):
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/division/create", json={
    "name": "Отдел кадров2",
    "director": "Putin2"
    })
    assert response.status_code == 200
