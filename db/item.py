from pymongo import MongoClient 
from bson.objectid import ObjectId 
from dotenv import load_dotenv 
import os

# Load environment variables from .env file
load_dotenv()

class ItemDatabase:
    def __init__(self):
        # Retrieve the MongoDB URI from the environment variable
        mongo_uri = os.getenv("MONGO_URI")
        
        # Connect to MongoDB using the URI from the environment
        self.client = MongoClient(mongo_uri)
        self.db = self.client.cafe  # Name of your database
        self.collection = self.db.item  # Name of your collection

    def get_items(self):
        result = []
        for row in self.collection.find():
            item_dict = {
                'id': str(row['_id']),  # Convert ObjectId to string
                'name': row['name'],
                'price': row['price']
            }
            result.append(item_dict)
        return result

    def get_item(self, item_id):
        item_id = ObjectId(item_id)  # Convert string ID to ObjectId
        item = self.collection.find_one({'_id': item_id})
        if item:
            return {
                'id': str(item['_id']),  # Convert ObjectId to string
                'name': item['name'],
                'price': item['price']
            }
        return None

    def add_item(self, body):
        try:
            self.collection.insert_one({
                'name': body['name'],
                'price': body['price']
            })
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def update_item(self, item_id, body):
        item_id = ObjectId(item_id)  # Convert string ID to ObjectId
        result = self.collection.update_one(
            {'_id': item_id},
            {'$set': {'name': body['name'], 'price': body['price']}}
        )
        return result.modified_count > 0

    def delete_item(self, item_id):
        item_id = ObjectId(item_id)  # Convert string ID to ObjectId
        result = self.collection.delete_one({'_id': item_id})
        return result.deleted_count > 0
