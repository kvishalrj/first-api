from pymongo import MongoClient 
from bson.objectid import ObjectId 
from dotenv import load_dotenv 
import os

# Load environment variables from .env file
load_dotenv()

class BlocklistDatabase:
    def __init__(self):
        # Retrieve the MongoDB URI from the environment variable
        mongo_uri = os.getenv("MONGO_URI")
        
        # Connect to MongoDB using the URI from the environment
        self.client = MongoClient(mongo_uri)
        self.db = self.client.cafe  # Name of your database
        self.collection = self.db.blocklist  # Name of your collection

    