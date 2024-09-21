# #from tortoise.contrib import test
# import pytest
# from httpx import AsyncClient
#
# @pytest.mark.anyio
# async def test_get_division(client: AsyncClient):
#     response = await client.get("/division/create")
#     assert response.status_code == 200
#
# @pytest.mark.anyio
# async def test_post_division(client: AsyncClient):
#     print(client, "pytest1")
#     data = {
#     "name": "Отдел кадров2",
#     "director": "Putin2"
#     }
#     response = await client.post("/division/create", json=data)
#     assert response.status_code == 200
# @pytest.mark.anyio
# async def test_get_users(client: AsyncClient):
#     print(client, "pytest1")
#     data = {
#         "name": "test1",
#         "last_name": "test1",
#         "login": "test1",
#         "password": "test1",
#         "email": "test1@gmail.com",
#         "division_id":2,
#         "start_vacation": "2023-01-01",
#         "finish_vacation": "2023-01-05",
#         "start_business_trip": "2023-02-03",
#         "finish_business_trip": "2023-01-06"
#     }
#     response = await client.post("/users/create", json = data)
#     assert response.status_code == 200
#
#
#
#
#
#
#
#
# # class TestSomething(test.TestCase):
# #     def test_something(self):
# #         ...
# #
# #     async def test_something_async(self):
# #         ...
# #
# #     @test.skip('Skip this')
# #     def test_skip(self):
# #         ...
# #
# #     @test.expectedFailure
# #     def test_something(self):
# #         ...
#
#
# # from fastapi.testclient import TestClient
# # from .main import app
# #
# # client = TestClient(app)
# #
# #
# # def test_get_users():
# #     response = client.get("/users")
# #     assert response.status_code == 200
# #
# # def test_create_users():
# #     response = client.post(
# #         "/create_user",
# #         json={
# #             "name": "test_pytest",
# #             "last_name": "test_pytest",
# #             "login": "test_pytest",
# #             "password": "test_pytest",
# #             "email": "test_pytest@gmail.com"
# #         },
# #     )
# #     assert response.status_code == 200
#
