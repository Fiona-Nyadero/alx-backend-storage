#!/usr/bin/env python3
'''Module lists collections with a specific arg'''


def schools_by_topic(mongo_collection, topic):
    '''Returns a list of schools with given topic'''
    sch_lists = mongo_collection.find({"topics": topic})

    return sch_lists
