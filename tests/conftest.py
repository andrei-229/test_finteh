import pytest
import swagger_client
from swagger_client.api import pet_api, store_api, user_api

@pytest.fixture(scope="session")
def api_clients():
    configuration = swagger_client.Configuration()
    configuration.host = "https://petstore.swagger.io/v2"
    client = swagger_client.ApiClient(configuration)
    return {
        "pet": pet_api.PetApi(client),
        "store": store_api.StoreApi(client),
        "user": user_api.UserApi(client),
    }
