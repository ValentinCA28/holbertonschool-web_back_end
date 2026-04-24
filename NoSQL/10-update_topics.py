#!/usr/bin/env python3
"""Module that provides a function to update topics of school documents."""


def update_topics(mongo_collection, name, topics):
    """Change all topics of school documents matching a given name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): school name to match.
        topics (list[str]): new list of topics replacing the existing one.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
