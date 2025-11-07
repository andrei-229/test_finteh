# Проект автотестов для Petstore API
## Описание
Задача — реализовать пример автотестов, проверяющих работу публичного API Petstore (https://petstore.swagger.io).

Проект демонстрирует два подхода к тестированию REST API:

1) Автоматически сгенерированный Swagger-клиент (swagger_client) — масштабируемый подход для крупных API.

2) Pytest + Requests — пример ручных HTTP-запросов к API.

## Технологический стек:

- Python 3.10+

- Pytest — фреймворк для автотестов

- Requests — работа с HTTP-запросами

- Swagger Codegen Client — автоматически сгенерированный SDK для Petstore

## Запуск проекта

```sh
pip install -r requirements.txt
```

```sh
python setup.py install
```
(or `sudo python setup.py install` to install the package for all users)

## Запустить тесты
```sh
pytest tests/ -v
```

## Покрытие API
| Раздел               | Методы                 | Пример теста               | Назначение                         |
| -------------------- | ---------------------- | -------------------------- | ---------------------------------- |
| 🐶 **Pet**           | GET, POST, PUT, DELETE | `test_pet_api.py`          | Работа с питомцами                 |
| 🏪 **Store**         | GET, POST, DELETE      | `test_store_api.py`        | Заказы и инвентарь                 |
| 👤 **User**          | GET, POST, DELETE      | `test_user_api.py`         | Пользователи, логин                |
| 🌐 **Requests Demo** | GET, POST, PUT, DELETE | `test_pet_api_requests.py` | Прямые HTTP-запросы через requests |

## Особенности реализации
* Тесты используют `try/except ApiException`.
* Ошибки API не ломают выполнение — тест помечается как XFAIL.
* Каждый тест независим (используются случайные id).

* Проверяются как позитивные, так и негативные сценарии.

* Возможна интеграция с pytest-html или Allure для отчётности.

## Примеры сценариев
* ✅ Создание и получение питомца `(POST /pet, GET /pet/{id})`

* ✅ Обновление питомца `(PUT /pet)`

* ✅ Удаление питомца `(DELETE /pet/{id})`

* ✅ Создание заказа `(POST /store/order)`

* ✅ Получение инвентаря `(GET /store/inventory)`

* ✅ Создание и логин пользователя `(POST /user, GET /user/login)`

## Swagger Client
Этот проект использует автоматически сгенерированный клиент для Petstore API.
Генерация выполнена с помощью команды:
```sh
curl -X POST -H "content-type:application/json" \
     -d '{"swaggerUrl":"https://petstore.swagger.io/v2/swagger.json"}' \
     https://generator.swagger.io/api/gen/clients/python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
body = swagger_client.Pet() # Pet | Pet object that needs to be added to the store

try:
    # Add a new pet to the store
    api_instance.add_pet(body)
except ApiException as e:
    print("Exception when calling PetApi->add_pet: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://petstore.swagger.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PetApi* | [**add_pet**](docs/PetApi.md#add_pet) | **POST** /pet | Add a new pet to the store
*PetApi* | [**delete_pet**](docs/PetApi.md#delete_pet) | **DELETE** /pet/{petId} | Deletes a pet
*PetApi* | [**find_pets_by_status**](docs/PetApi.md#find_pets_by_status) | **GET** /pet/findByStatus | Finds Pets by status
*PetApi* | [**find_pets_by_tags**](docs/PetApi.md#find_pets_by_tags) | **GET** /pet/findByTags | Finds Pets by tags
*PetApi* | [**get_pet_by_id**](docs/PetApi.md#get_pet_by_id) | **GET** /pet/{petId} | Find pet by ID
*PetApi* | [**update_pet**](docs/PetApi.md#update_pet) | **PUT** /pet | Update an existing pet
*PetApi* | [**update_pet_with_form**](docs/PetApi.md#update_pet_with_form) | **POST** /pet/{petId} | Updates a pet in the store with form data
*PetApi* | [**upload_file**](docs/PetApi.md#upload_file) | **POST** /pet/{petId}/uploadImage | uploads an image
*StoreApi* | [**delete_order**](docs/StoreApi.md#delete_order) | **DELETE** /store/order/{orderId} | Delete purchase order by ID
*StoreApi* | [**get_inventory**](docs/StoreApi.md#get_inventory) | **GET** /store/inventory | Returns pet inventories by status
*StoreApi* | [**get_order_by_id**](docs/StoreApi.md#get_order_by_id) | **GET** /store/order/{orderId} | Find purchase order by ID
*StoreApi* | [**place_order**](docs/StoreApi.md#place_order) | **POST** /store/order | Place an order for a pet
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create user
*UserApi* | [**create_users_with_array_input**](docs/UserApi.md#create_users_with_array_input) | **POST** /user/createWithArray | Creates list of users with given input array
*UserApi* | [**create_users_with_list_input**](docs/UserApi.md#create_users_with_list_input) | **POST** /user/createWithList | Creates list of users with given input array
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
*UserApi* | [**login_user**](docs/UserApi.md#login_user) | **GET** /user/login | Logs user into the system
*UserApi* | [**logout_user**](docs/UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{username} | Updated user


## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [Category](docs/Category.md)
 - [Order](docs/Order.md)
 - [Pet](docs/Pet.md)
 - [Tag](docs/Tag.md)
 - [User](docs/User.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## petstore_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://petstore.swagger.io/oauth/authorize
- **Scopes**: 
 - **read:pets**: read your pets
 - **write:pets**: modify pets in your account


## Author

apiteam@swagger.io

