import pytest
from pprint import pprint
from swagger_client.models import Pet, Category, Tag
from swagger_client.rest import ApiException

class TestPetAPI:
    def test_create_pet(self, api_clients):
        pet_api = api_clients["pet"]

        pet = Pet(id=987654, name="pytest-pet", status="available", photo_urls=['https://example.com/pic.jpg'])
        pet_api.add_pet(pet)
        api_response = pet_api.get_pet_by_id(987654)

        assert api_response.id == pet.id
        assert api_response.name == pet.name
        assert api_response.photo_urls == pet.photo_urls

    def test_get_nonexistent_pet(self, api_clients):
        pet_api = api_clients["pet"]
        
        non_existent_id = 0
        try:
            response = pet_api.get_pet_by_id(non_existent_id)
            pprint(f"Unexpected response for id {non_existent_id}: {response}")
            assert False, f"Expected ApiException for non-existent pet with id {non_existent_id}"
        except ApiException as e:
            pprint(f"Correctly caught exception for id {non_existent_id}: {e}")
            print(e.body)
            assert e.status == 404
            assert e.body == '{"code":1,"type":"error","message":"Pet not found"}'

    def test_update_pet(self, api_clients):
        pet_api = api_clients["pet"]
        pet_old = Pet(id=987655, name="old", status="available", photo_urls=['https://example.com/pic.jpg'])
        pet_api.add_pet(pet_old)
        pprint(pet_api)
        api_response_old = pet_api.get_pet_by_id(987655)
        assert api_response_old.name == 'old'

        pet_new = Pet(id=987655, name="new", status="available", photo_urls=['https://example.com/pic.jpg'])
        pet_api.update_pet(pet_new)
        # pet_api.update_pet_with_form(987655, name="updated-with-form", status="pending")
        api_response_new = pet_api.get_pet_by_id(987655)
        pprint(api_response_old)
        pprint(api_response_new)


# class TestCleanup:
#     """Тесты для очистки тестовых данных"""
    
#     def test_cleanup_test_pets(self, api_clients):
#         """Очистка всех созданных тестовых питомцев"""
#         pet_api = api_clients["pet"]
        
#         test_pet_ids = [987654, 987655, 987656, 987657, 987658, 987659, 987660]
        
#         for pet_id in test_pet_ids:
#             try:
#                 pet_api.delete_pet(pet_id, api_key="special-key")
#                 pprint(f"Cleaned up pet {pet_id}")
#             except ApiException as e:
#                 if e.status != 404:  # Игнорируем если питомец уже не существует
#                     pprint(f"Error cleaning up pet {pet_id}: {e}")