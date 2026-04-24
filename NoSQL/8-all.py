#!/usr/bin/env python3
"""Module that provides a function to list all documents in a collection."""


def list_all(mongo_collection):
    """List all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of all documents, or an empty list if the collection is empty.
    """
    return list(mongo_collection.find())
