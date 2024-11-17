from pymongo.mongo_client import MongoClient

#in place of username and password , plase feed the user name and passowrd of your mongodb cluster
client = MongoClient("mongodb+srv://<username>:<password>@cluster01.7snapwc.mongodb.net/?retryWrites=true&w=majority&appName=cluster01")

db = client.trendingdb

collection_name = db["trending_collection"]
