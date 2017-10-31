from mongo_client import mongodb_client
from src.config.mongo_config import MONGO_CONFIG
class MongoDBDao:
    def __init__(self, mongodb_client, collection):
        self.client = mongodb_client
        self.collection = mongodb_client.get_collection(collection)


    def fetch_single_doc(self, filter, projection={'_id': False}):
        doc = self.collection.find_one(filter, projection)
        if not doc:
            doc = dict()
        return doc


    def fetch_batch_docs(self, filter, projection={'_id': False}):
        docs = list(self.collection.find(filter, projection))
        return docs


    def insert_single_doc(self, doc):
        self.collection.insert_one(doc)


    def update_single_doc(self, filter, doc, upsert=False):
        update = { '$set': doc }
        self.collection.update_one(filter, update, upsert=upsert)


    def count_docs(self, filter):
        count = self.collection.count(filter)
        return count

    
    def delete_single_doc(self, filter):
        self.collection.delete_one(filter)

group_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.COLLECTION['group'])
player_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.COLLECTION['player'])
game_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.COLLECTION['game'])
log_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.COLLECTION['log'])
round_log_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.COLLECTION['round_log'])
seq_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.COLLECTION['seq'])