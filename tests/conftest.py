import pytest
import swagger_client
import random
from swagger_client.api import pet_api, store_api, user_api
from swagger_client.rest import ApiException

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

@pytest.fixture
def random_id():
    return random.randint(1000000, 9999999)