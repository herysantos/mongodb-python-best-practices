from pymongo import MongoClient

MONGO_URI = "mongodb://admin:admin@127.0.0.1:27017/"

client = MongoClient(MONGO_URI)

for db_name in client.list_database_names():
    print(db_name)
