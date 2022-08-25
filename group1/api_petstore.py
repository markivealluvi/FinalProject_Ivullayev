import requests
import json


class PetStoreApi:

    @staticmethod
    def add_new_pet():
        with open("C:/Users/ikram/PycharmProjects/FinalProject/group1/new_pet.json") as json_load:
            data = json.load(json_load)
        requests.post("https://petstore.swagger.io/v2/pet", json=data)

    @staticmethod
    def verify_new_pet():
        with open("C:/Users/ikram/PycharmProjects/FinalProject/group1/new_pet.json") as json_load:
            data = json.load(json_load)
        pet_21 = requests.get("https://petstore.swagger.io/v2/pet/21").json()
        assert pet_21 == data

    @staticmethod
    def delete_pet():
        requests.delete("https://petstore.swagger.io/v2/pet/21")

    @staticmethod
    def verify_pet_deleted():
        with open("C:/Users/ikram/PycharmProjects/FinalProject/group1/new_pet.json") as json_load:
            data = json.load(json_load)
        pet_21 = requests.get("https://petstore.swagger.io/v2/pet/21").json()
        assert data != pet_21

    @staticmethod
    def create_user():
        with open("C:/Users/ikram/PycharmProjects/FinalProject/group1/new_user.json") as json_load:
            data = json.load(json_load)
        requests.post("https://petstore.swagger.io/v2/user", json=data)

    @staticmethod
    def get_user_data():
        user_data = requests.get("https://petstore.swagger.io/v2/user/haaland").json()
        print(user_data)

    @staticmethod
    def update_username():
        response = requests.get("https://petstore.swagger.io/v2/user/login?username=haaland&password=12345")
        response1 = requests.put("https://petstore.swagger.io/v2/user/haaland", json={
            "id": 21,
            "username": "haalandinho",
            "firstName": "Erling",
            "lastName": "Haaland",
            "email": "haaland@gmail.com",
            "password": "12345",
            "phone": "+77777777777",
            "userStatus": 0
        })
        print(response.ok, response1.ok)

    @staticmethod
    def verify_username_changed():
        user = requests.get("https://petstore.swagger.io/v2/user/haalandinho").json()
        assert user["username"] == 'haalandinho'

