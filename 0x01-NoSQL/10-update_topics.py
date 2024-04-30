#!/usr/bin/env python3
'''Module changes all topics of a doc based on name'''


def update_topics(mongo_collection, name, topics):
    '''Updates specified document with specified topics'''
    doc_2update = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(doc_2update, new_topics)
