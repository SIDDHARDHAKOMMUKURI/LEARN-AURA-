import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def init_db():
    """Initialize MongoDB connection and return database object"""
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise ValueError("❌ MONGO_URI not found in .env file!")

    client = MongoClient(mongo_uri)
    db = client["learnaura"]  # Database name
    return db


def register_user(db, user_id, username):
    """Register or update user in DB"""
    users = db["users"]
    users.update_one(
        {"user_id": user_id},
        {"$set": {"username": username}},
        upsert=True
    )


def log_interaction(db, user_id, command, query, response=None):
    """Log user interactions"""
    logs = db["logs"]
    logs.insert_one({
        "user_id": user_id,
        "command": command,
        "query": query,
        "response": response
    })
