#!/usr/bin/env python3
'''Module inserts a new document based on kwargs'''

def insert_school(mongo_collection, **kwargs):
    '''Returns the new doc _id'''
    return mongo_collection.insert_one(kwargs).inserted_id
