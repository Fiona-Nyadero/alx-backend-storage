#!/usr/bin/env python3
'''Module lists all docs in a collection'''
from pymongo import MongoClient


def list_all(mongo_collection):
    '''Fx returns list of doc or empty list'''
    return mongo_collection.find()
