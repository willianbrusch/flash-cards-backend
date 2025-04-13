import pytest

from tests.utils import autenticate_user

_P_USER_EMAIL = "test@email.com"
_P_USER_PASSWORD = "123456"


@pytest.fixture
def url():
    return "http://localhost:8081"


@pytest.fixture
def api_token_user(url):
    return autenticate_user(url, _P_USER_EMAIL, _P_USER_PASSWORD)
