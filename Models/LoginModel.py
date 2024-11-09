import pymongo, bcrypt
from pymongo import MongoClient

class LoginModel:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.codewizard
        self.Users = self.db.users

    def check_login(self, data):
        print("data is", data)

        user = self.Users.find_one({'username': data.username})
        print("user retrieved is", user)

        if user:
            if bcrypt.checkpw(data.password.encode('utf-8'), user['password']):
                print("Login successful")
                return user
            else:
                return False
        else:
            return False

    def update_info(self, data):
        print("data is", data)

        updated = self.Users.update_one({'username': data['username']}, {'$set': data})

        return True

    def get_profile(self, data):
        print("data is", data)

        user_info = self.Users.find_one({'username': data['username']})
        if user_info:
            return user_info

    def update_image(self, data):
        print("image is", data)
        updated = self.Users.update_one({'username': data['username']}, {'$set': data})

        return True