#!/usr/bin/env python3
"""
    Python function that inserts a new document in a collection based on kwargs
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """Return the _id of the insetsion"""
    ans = mongo_collection.insert_one(kwargs)
    return ans.inserted_id
