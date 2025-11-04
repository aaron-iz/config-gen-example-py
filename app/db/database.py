# TODO: This is just a placeholder implementation
from typing import Dict

db_mock: Dict[str, list] = {}

def ensure_exists(collection_key = "users"):
    if collection_key not in db_mock:
        db_mock[collection_key] = []

def save(data, collection_key = "users"):
    ensure_exists(collection_key)    
    db_mock[collection_key].append(data)
    
def find(id, collection_key = "users"):
    ensure_exists(collection_key)
    collection = db_mock[collection_key]
    for item in collection:
        if item["id"] == id:
            return item
        
    return None

def find_all(collection_key = "users"):
    ensure_exists(collection_key)
    return db_mock[collection_key]

def delete(id, collection_key = "users"):
    ensure_exists(collection_key)
    collection = db_mock[collection_key]
    for item in collection:
        if item["id"] == id:
            collection.remove(item)
            return
        
def update(id, data, collection_key = "users"):
    delete(id, collection_key)
    save(data, collection_key)