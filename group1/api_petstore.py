import requests
import json


class PetStoreApi:

    @staticmethod
    def add_new_pet():
        with open("./group1/new_pet.json") as json_load:
            data = json.load(json_load)
        requests.post("https://petstore.swagger.io/v2/pet", json=data)

    @staticmethod
    def verify_new_pet():
        with open("./group1/new_pet.json") as json_load:
            data = json.load(json_load)
        pet_21 = requests.get("https://petstore.swagger.io/v2/pet/21").json()
        assert pet_21 == data

    @staticmethod
    def delete_pet():
        requests.delete("https://petstore.swagger.io/v2/pet/21")

    @staticmethod
    def verify_pet_deleted():
        with open("./group1/new_pet.json") as json_load:
            data = json.load(json_load)
        pet_21 = requests.get("https://petstore.swagger.io/v2/pet/21").json()
        assert data != pet_21
