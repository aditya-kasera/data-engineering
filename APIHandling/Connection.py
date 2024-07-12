from pymongo import MongoClient # class used to connect to a MongoDB server

def get_db():
    client = MongoClient(f"mongodb://localhost:27017") # MongoDB client object with connection string specifying the hostname (localhost) and the port (27017)
    db = client["freshers"] # selects a database named "freshers"
    return db