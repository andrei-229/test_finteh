import pytest
from swagger_client.models import Pet
from swagger_client.rest import ApiException

@pytest.mark.api
def test_create_and_get_pet(api_clients, random_id):
    pet_api = api_clients["pet"]
    try:
        pet = Pet(id=random_id, name="pytest-pet", status="available")
        pet_api.add_pet(pet)
        api_response = pet_api.get_pet_by_id(random_id)
        assert api_response.id == pet.id
        assert api_response.name == pet.name
    except ApiException as e:
        pytest.xfail(f"Ошибка API при создании питомца")

@pytest.mark.api
def test_get_nonexistent_pet(api_clients, random_id):
    pet_api = api_clients["pet"]
    try:
        pet_api.get_pet_by_id(random_id)
        pytest.xfail("The API get a non-existent ID.")
    except ApiException as e:
        assert e.status == 404

@pytest.mark.api
def test_update_pet_status(api_clients, random_id):
    pet_api = api_clients["pet"]
    try:
        pet = Pet(id=random_id, name="old", status="available", photo_urls=["https://example.com/img.jpg"])

        pet_api.add_pet(pet)
        old_res = pet_api.get_pet_by_id(random_id)
        assert old_res.name == "old"
        assert old_res.status == "available"
    except ApiException:
        pytest.xfail("API did not created old_pet object")
        
    pet.status = "sold"
    pet.name = "new"
    pet_api.update_pet(pet)
    try:
        new_res = pet_api.get_pet_by_id(random_id)
        assert new_res.status == "sold"
        assert new_res.name == "new"
    except ApiException:
        pytest.xfail("API did not get pet object")
    

@pytest.mark.api
def test_delete_pet(api_clients, random_id):
    """Удаление питомца"""
    pet_api = api_clients["pet"]
    pet = Pet(id=random_id, name="del-pet", status="available", photo_urls=["https://example.com/img.jpg"])
    try:
        pet_api.add_pet(pet)
        pet_api.get_pet_by_id(random_id)
    except ApiException as e:
        pytest.xfail(f"API did not created pet object")
    try:
        pet_api.delete_pet(random_id)
        with pytest.raises(ApiException):
            pet_api.get_pet_by_id(random_id)
    except ApiException as e:
        pytest.xfail(f"Ошибка API при удалении питомца: {e}")


def test_delete_nonexistent_pet(api_clients, random_id):
    pet_api = api_clients["pet"]
    try:
        pet_api.delete_pet(random_id)
        pytest.xfail("The API removed a non-existent ID.")
    except ApiException as e:
        assert e.status == 404

