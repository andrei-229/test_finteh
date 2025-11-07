import requests
import pytest
import random

BASE_URL = "https://petstore.swagger.io/v2"

def test_create_pet():
    pet_id = random.randint(1000000, 9999999)
    pet = {
        "id": pet_id,
        "name": "doggie",
        "status": "available"
    }
    res = requests.post(f"{BASE_URL}/pet", json=pet)
    assert res.status_code == 200
    assert res.json()["name"] == pet["name"], f"Запись не соответствует ожидаемой: {res.json()['name']} != {pet["name"]}"

def test_get_pet():
    pet_id = random.randint(1000000, 9999999)
    pet = {
        "id": pet_id,
        "name": "doggie",
        "status": "available"
    }
    res = requests.post(f"{BASE_URL}/pet", json=pet)
    if res.status_code != 200:
        pytest.xfail(f"Ошибка API при добавлении питомца")
    res = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert res.status_code == 200
    assert res.json()['name'] == pet["name"], f"Запись не соответствует ожидаемой: {res.json()['name']} != {pet["name"]}"

def test_update_pet():
    pet_id = random.randint(1000000, 9999999)
    pet = {
        "id": pet_id,
        "name": "doggie",
        "status": "available"
    }
    res = requests.post(f"{BASE_URL}/pet", json=pet)
    assert res.status_code == 200
    pet = {
        "id": pet_id,
        "name": "updated-dog",
        "status": "sold"
    }
    res = requests.put(f"{BASE_URL}/pet", json=pet)
    assert res.status_code == 200
    res = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert res.status_code == 200
    assert res.json()['name'] == pet['name'], f"Запись не соответствует ожидаемой: {res.json()['name']} != {pet['name']}"

def test_delete_pet():
    res = requests.delete(f"{BASE_URL}/pet/123456")
    assert res.status_code in [200, 404]
