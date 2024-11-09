import datetime
import pymongo, bcrypt
from pymongo import MongoClient
import humanize

class PostModel:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.codewizard
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):
        inserted = self.Posts.insert_one({"username": data['username'], "content": data['content']})
        return True

    def get_all_posts(self):
        all_posts = self.Posts.find().sort("date_added", pymongo.DESCENDING)
        new_posts = []
        for post in all_posts:
            print(post)
            post["username"] = self.Users.find_one({"username": post["username"]})["username"]
            post["content"] = self.Users.find_one({"username": post["username"]})["content"]
            post["timestamp"] = humanize.naturaltime(datetime.datetime.now() + post["date_added"])
            new_posts.append(post)

        return new_posts

    def get_user_posts(self, username):
        all_posts = self.Posts.find({"username": username}).sort("date_added", pymongo.DESCENDING)
        new_posts = []
        for post in all_posts:
            print(post)
            post["username"] = self.Users.find_one({"username": post["username"]})["username"]
            post["content"] = self.Users.find_one({"username": post["username"]})["content"]
            post["timestamp"] = humanize.naturaltime(datetime.datetime.now() + post["date_added"])
            new_posts.append(post)

        return new_posts
