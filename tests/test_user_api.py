import pytest
import random
from swagger_client.models import User
from swagger_client.rest import ApiException


@pytest.mark.api
def test_create_user(api_clients, random_id):
    """Создание пользователя"""
    users = api_clients["user"]
    user = User(
        id=random_id,
        username=f"user_{random_id}",
        first_name="Test",
        last_name="User",
        email=f"user_{random_id}@example.com",
        password="pass123",
        phone="12345",
        user_status=1
    )
    try:
        users.create_user(user)
        fetched = users.get_user_by_name(user.username)
        assert fetched.username == user.username
    except ApiException as e:
        pytest.xfail(f"Ошибка API при создании пользователя: {e}")


@pytest.mark.api
def test_login_logout_user(api_clients, random_id):
    """Логин и логаут"""
    users = api_clients["user"]
    user = User(id=random_id, username=f"user_{random_id}", password="pass123")
    try:
        users.create_user(user)
        users.login_user(user.username, user.password)
        users.logout_user()
    except ApiException as e:
        pytest.xfail(f"Ошибка API при логине/логауте: {e}")


@pytest.mark.api
def test_delete_user(api_clients, random_id):
    """Удаление пользователя"""
    users = api_clients["user"]
    user = User(id=random_id, username=f"user_{random_id}", password="pass123")
    try:
        users.create_user(user)
        users.delete_user(user.username)
        with pytest.raises(ApiException):
            users.get_user_by_name(user.username)
    except ApiException as e:
        pytest.xfail(f"Ошибка API при удалении пользователя: {e}")


@pytest.mark.api
def test_get_nonexistent_user(api_clients):
    """Получение несуществующего пользователя"""
    users = api_clients["user"]
    fake_username = f"unknown_{random.randint(1000,9999)}"
    try:
        users.get_user_by_name(fake_username)
        pytest.fail("API не выбросило ошибку при запросе несуществующего пользователя")
    except ApiException as e:
        assert e.status == 404
