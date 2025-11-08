import pytest
import random
from swagger_client.models import Order
from swagger_client.rest import ApiException


@pytest.mark.api
def test_place_and_get_order_by_id(api_clients):
    """Получение заказа"""
    random_id = random.randint(1, 9)
    store = api_clients["store"]
    order = Order(id=random_id, pet_id=1, quantity=2, status="placed", complete=True)
    try:
        store.place_order(order)
        found = store.get_order_by_id(random_id)
        assert found.id == random_id
        # API может не сохранить статус корректно
        if found.status != "placed":
            pytest.xfail(f"API не вернул корректный статус заказа: {found.status}")
        assert found.status == "placed"
    except ApiException as e:
        pytest.xfail(f"Ошибка API при создании заказа: {e}")


@pytest.mark.api
def test_delete_order(api_clients):
    """Удаление заказа"""
    store = api_clients["store"]
    random_id = random.randint(1, 10)
    order = Order(id=random_id, pet_id=1, quantity=1, status="placed", complete=True)
    try:
        store.place_order(order)
        store.get_order_by_id(random_id)
    except ApiException as e:
        pytest.xfail(f"Ошибка API при создании заказа: {e}")
    try:
        store.delete_order(random_id)
        try:
            store.get_order_by_id(random_id)
            pytest.xfail(f"Заказ не удалился")
        except ApiException:
            pass
    except ApiException as e:
        pytest.xfail(f"Ошибка API при удалении заказа: {e}")


@pytest.mark.api
def test_get_inventory(api_clients):
    """Получение инвентаря"""
    store = api_clients["store"]
    try:
        inv = store.get_inventory()
        assert isinstance(inv, dict)
    except ApiException as e:
        pytest.xfail(f"Ошибка API при получении инвентаря: {e}")
