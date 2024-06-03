from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@<clustername>.7snapwc.mongodb.net/?retryWrites=true&w=majority&appName=cluster01")

db = client.trendingdb

collection_name = db["trending_collection"]