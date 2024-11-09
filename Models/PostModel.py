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

    def get_all_posts(self, new_posts=None):
        all_posts = self.Posts.find()
        new_posts = []

        for post in all_posts:
            print(post)
            post['user'] = self.Users.find_one({'username': post['username']})
            new_posts.append(post)

        return new_posts
