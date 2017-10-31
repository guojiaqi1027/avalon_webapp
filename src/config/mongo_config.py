class MongoConfig:
    DB_NAME = 'avalon'
    COLLECTION = {
        'group': 'group',
        'player': 'player',
        'game': 'game',
        'log': 'log',
        'round_log': 'round_log',
        'seq': 'seq'
    }


class MongoLocalConfig(MongoConfig):
    ENTRY_POINT = '127.0.0.1'
    PORT = 27017

MONGO_CONFIG = MongoLocalConfig()