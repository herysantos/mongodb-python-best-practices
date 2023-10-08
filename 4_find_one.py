import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId

load_dotenv()
MONGO_URI = os.environ["MONGO_URI"]

client = MongoClient(MONGO_URI)

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)

client.close()