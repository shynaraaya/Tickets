from pymongo import MongoClient

HOST = 'localhost'
PORT = 27017

client = MongoClient(HOST, PORT)


def insert(data, db='ticketsdb', collection='messages'):
    _id = client[db][collection].insert(data)
    return _id


def get(db='ticketsdb', collection='messages'):
    return client[db][collection].find()