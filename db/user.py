from pymongo import MongoClient 
from bson.objectid import ObjectId 
from dotenv import load_dotenv 
import os

# Load environment variables from .env file
load_dotenv()

class UserDatabase:
    def __init__(self):
        # Retrieve the MongoDB URI from the environment variable
        mongo_uri = os.getenv("MONGO_URI")
        
        # Connect to MongoDB using the URI from the environment
        self.client = MongoClient(mongo_uri)
        self.db = self.client.cafe  # Name of your database
        self.collection = self.db.users  # Name of your collection

    def get_user(self, user_id):
        try:
            user_id = ObjectId(user_id)  # Convert string ID to ObjectId
            user = self.collection.find_one({"_id": user_id})
            if user:
                return {
                    'id': str(user['_id']),  # Convert ObjectId to string
                    'username': user['username'],
                    'password': user['password']
                }
        except Exception as e:
            print(f"An error occurred: {e}")
        return {}

    def add_user(self, username, password):
        try:
            if self.collection.find_one({'username': username}):
                return False
        
            self.collection.insert_one({
                'username': username,
                'password': password
            })
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def delete_user(self, user_id):
        try:
            user_id = ObjectId(user_id)  # Convert string ID to ObjectId
            result = self.collection.delete_one({"_id": user_id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def verify_user(self, username, password):
        try:
            user = self.collection.find_one({
                'username': username,
                'password': password
            })
            if user:
                return str(user['_id'])  # Convert ObjectId to string
        except Exception as e:
            print(f"An error occurred: {e}")
        return None
