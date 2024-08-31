import os
import pytest
from tortoise.contrib.test import initializer, finalizer


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    db_url = os.environ.get("TORTOISE_TEST_DB", "sqlite://:memory")
    initializer(["tests.testmodels"], db_url=db_url, app_label="models")
    request.addfinalizator(finalizer)
