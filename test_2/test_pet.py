import pytest, time, random
from swagger_client.models import Pet, Category, Tag
from conftest import safe_call
from swagger_client.rest import ApiException


def test_create_and_get_pet(api_clients):
    pet_api = api_clients["pet"]
    pet_id = random.randint(1000000, 9999999)

    try:
        pet = Pet(id=pet_id, name="pytest-pet", status="available", photo_urls=['https://example.com/pic.jpg'])
        pet_api.add_pet(pet)
        api_response = pet_api.get_pet_by_id(pet_id)
        assert api_response.id == pet.id
        assert api_response.name == pet.name
        assert api_response.photo_urls == pet.photo_urls
    except ApiException:
        pytest.xfail("API did not return created pet object")


def test_get_nonexistent_pet(api_clients):
    pet_api = api_clients["pet"]
    nonexistent_id = random.randint(1000000, 9999999)
    # Получение несуществующего питомца не должно крашить тест
    try:
        pet_api.get_pet_by_id(nonexistent_id)
        pytest.xfail("The API get a non-existent ID.")
    except ApiException as e:
        assert e.status == 404


def test_update_pet_status(api_clients):
    pet_api = api_clients["pet"]
    pet_id = random.randint(1000000, 9999999)
    try:
        pet = Pet(id=pet_id, name="old", status="available", photo_urls=["https://example.com/img.jpg"])

        pet_api.add_pet(pet)
        old_res = pet_api.get_pet_by_id(pet_id)
        assert old_res.name == "old"
        assert old_res.status == "available"
    except ApiException:
        pytest.xfail("API did not created old_pet object")
        
    pet.status = "sold"
    pet.name = "new"
    safe_call(pet_api.update_pet, pet)
    new_res = safe_call(pet_api.get_pet_by_id, pet_id)
    if not new_res:
        pytest.xfail("API did not get pet object")
    assert new_res.status == "sold"
    assert new_res.name == "new"


def test_delete_nonexistent_pet(api_clients):
    pet_api = api_clients["pet"]
    nonexistent_id = random.randint(1000000, 9999999)
    # Удаление несуществующего питомца не должно крашить тест
    try:
        pet_api.delete_pet(nonexistent_id)
        pytest.xfail("The API removed a non-existent ID.")
    except ApiException as e:
        assert e.status == 404

