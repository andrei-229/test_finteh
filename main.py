# from __future__ import print_function
# import time
# import swagger_client
# from swagger_client.rest import ApiException
# from pprint import pprint

# # Configure OAuth2 access token for authorization: petstore_auth
# configuration = swagger_client.Configuration()

# # create an instance of the API class
# api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
# pet_data = {"id": 123, "name": "TestPet", "status": "available"}
# body = swagger_client.Pet(id=123, name= "TestPet", status= "available", photo_urls={ "wrapped": True }) # Pet | Pet object that needs to be added to the store

# try:
#     # Add a new pet to the store
#     api_instance.add_pet(body)
# except ApiException as e:
#     print("Exception when calling PetApi->add_pet: %s\n" % e)

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.User(id=123, username="vasya") # User | Created user object

try:
    # Create user
    api_instance.create_user(body)
    api_response = api_instance.get_user_by_name("vasya")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)