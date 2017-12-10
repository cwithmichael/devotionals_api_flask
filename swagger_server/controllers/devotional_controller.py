import connexion
from swagger_server.models.api_response import ApiResponse
from swagger_server.models.devotional import Devotional
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
import json
from ..util import deserialize_date, deserialize_datetime
from ..db import DevotionalDataStore

def add_devotional(body):
    """
    Add a new devotional to the datastore
    
    :param body: Devotional object that needs to be added to the datastore
    :type body: dict | bytes

    :rtype: None
    """
    ds = DevotionalDataStore()
    devotional_id = json.loads(ds.add_devotional(connexion.request.get_json()))
    return devotional_id, 201


def delete_devotional(devotionalId, api_key=None):
    """
    Deletes a devotional
    
    :param devotionalId: Devotional id to delete
    :type devotionalId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    ds = DevotionalDataStore()
    devotional_id = json.loads(ds.delete_devotional(devotionalId))
    return devotional_id, 200


def find_devotionals_by_tags(tags):
    """
    Finds Devotionals by tags
    Muliple tags can be provided with comma separated strings. Use         tag1, tag2, tag3 for testing.
    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[Devotional]
    """
    return 'do some magic!'


def get_devotional_by_id(devotionalId):
    """
    Find devotional by ID
    Returns a single devotional
    :param devotionalId: ID of devotional to return
    :type devotionalId: int

    :rtype: Devotional
    """
    ds = DevotionalDataStore()
    devotional = json.loads(ds.get_devotional(devotionalId))
    return devotional, 200


def get_devotionals():
    """
    Get all devotionals
    Returns all the devotionals from the datastore

    :rtype: None
    """
    ds = DevotionalDataStore()
    devotionals = json.loads(ds.get_devotionals())
    return devotionals, 200


def update_devotional(devotionalId, body):
    """
    Update an existing devotional
    
    :param body: Devotional object that needs to be updated in the datastore
    :type body: dict | bytes

    :rtype: None
    """
    ds = DevotionalDataStore()
    devotional_id= json.loads(ds.update_devotional(devotionalId, connexion.request.get_json()))
    return devotional_id, 201


def upload_file(devotionalId, additionalMetadata=None, file=None):
    """
    uploads an image
    
    :param devotionalId: ID of devotional to update
    :type devotionalId: int
    :param additionalMetadata: Additional data to pass to server
    :type additionalMetadata: str
    :param file: file to upload
    :type file: werkzeug.datastructures.FileStorage

    :rtype: ApiResponse
    """
    return 'do some magic!'
