from pymongo import MongoClient
import json
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
import datetime

class DevotionalDataStore():
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['dev_db']

    def add_devotional(self, devotional):
        devotional.publishDate = datetime.datetime.utcnow()
        devotional_id = self.db.devotionals.insert_one(devotional).inserted_id
        return dumps(devotional_id)

    def get_devotionals(self):
        devotionals = []
        for devotional in self.db.devotionals.find():
            devotionals.append(devotional)
        return dumps(devotionals)

    def get_devotional(self, devotionalId):
        devotional = self.db.devotionals.find_one({'_id': ObjectId(devotionalId)})
        return dumps(devotional)

    def update_devotional(self, devotionalId, devotional):
        result = self.db.devotionals.replace_one({'_id': ObjectId(devotionalId)}, devotional)
        return dumps(result.raw_result)

    def delete_devotional(self, devotionalId):
        result = self.db.devotionals.delete_one({'_id': ObjectId(devotionalId)})
        return dumps(result.raw_result)