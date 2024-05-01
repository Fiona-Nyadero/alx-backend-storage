#!/usr/bin/env python3
'''Module gets a sorted list of items in a doc'''


def top_students(mongo_collection):
    '''returns the sorted list of students by aver score'''
    pipeline = [
        {
            '$addFields': {'averageScore': {'$avg': '$scores'}}
        },
        {'$sort': {'averageScore': -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))
