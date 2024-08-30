from tortoise.contrib import test

class TestSomething(test.TestCase):
    def test_something(self):
        ...

    async def test_something_async(self):
        ...

    @test.skip('Skip this')
    def test_skip(self):
        ...

    @test.expectedFailure
    def test_something(self):
        ...


# from fastapi.testclient import TestClient
# from .main import app
#
# client = TestClient(app)
#
#
# def test_get_users():
#     response = client.get("/users")
#     assert response.status_code == 200
#
# def test_create_users():
#     response = client.post(
#         "/create_user",
#         json={
#             "name": "test_pytest",
#             "last_name": "test_pytest",
#             "login": "test_pytest",
#             "password": "test_pytest",
#             "email": "test_pytest@gmail.com"
#         },
#     )
#     assert response.status_code == 200

