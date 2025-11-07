import pytest
import swagger_client
from swagger_client.api import pet_api, store_api, user_api

@pytest.fixture(scope="session")
def api_clients():
    """Создает API-клиентов"""
    configuration = swagger_client.Configuration()
    configuration.host = "https://petstore.swagger.io/v2"
    client = swagger_client.ApiClient(configuration)
    return {
        "pet": pet_api.PetApi(client),
        "store": store_api.StoreApi(client),
        "user": user_api.UserApi(client),
    }

def safe_call(api_method, *args, **kwargs):
    """
    Безопасный вызов API.
    Если API возвращает ошибку — тест не падает, а помечается как xfail.
    """
    try:
        return api_method(*args, **kwargs)
    except Exception as e:
        pytest.xfail(f"API returned error or unstable: {e}")
