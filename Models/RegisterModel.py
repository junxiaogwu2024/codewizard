import bcrypt
import pymongo
from pymongo import MongoClient

class RegisterModel:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        id = self.Users.insert_one({"username": data.get("username"),
                                    "password": hashed,
                                    "email": data.get("email"),
                                    "avatar": "",
                                    "background": "",
                                    "about": "",
                                    "hobbies": "",
                                    "birthday": ""})
        print("data is", data)
        print("user id is", id)
        myuser = self.Users.find_one({"username": data.get("username")})

        if myuser:
            print("user already exists", myuser.get("username"))

        if bcrypt.checkpw("Blockchain1".encode('utf-8'), hashed):
            print("Password match")

