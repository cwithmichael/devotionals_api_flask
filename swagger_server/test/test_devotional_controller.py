# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.api_response import ApiResponse
from swagger_server.models.devotional import Devotional
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDevotionalController(BaseTestCase):
    """ DevotionalController integration test stubs """
    def setUp(self):
        self.devotionalId = '5a2cadcbf28892b469e93490'

    def test_add_devotional(self):
        """
        Test case for add_devotional

        Add a new devotional to the datastore
        """
        body = Devotional()
        response = self.client.open('/api/v1/devotionals',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        assert response.status_code == 201, "Response body is : " + response.data.decode('utf-8')

    def test_delete_devotional(self):
        """
        Test case for delete_devotional

        Deletes a devotional
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open('/api/v1/devotionals/{devotionalId}'.format(devotionalId=self.devotionalId),
                                    method='DELETE',
                                    headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_devotionals_by_tags(self):
        """
        Test case for find_devotionals_by_tags

        Finds Devotionals by tags
        """
        query_string = [('tags', 'tags_example')]
        response = self.client.open('/api/v1/devotionals/findByTags',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_devotional_by_id(self):
        """
        Test case for get_devotional_by_id

        Find devotional by ID
        """
        response = self.client.open('/api/v1/devotionals/{devotionalId}'.format(devotionalId=self.devotionalId),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_devotionals(self):
        """
        Test case for get_devotionals

        Get all devotionals
        """
        response = self.client.open('/api/v1/devotionals',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_devotional(self):
        """
        Test case for update_devotional

        Update an existing devotional
        """
        body = Devotional()
        response = self.client.open('/api/v1/devotionals/{devotionalId}'.format(devotionalId=self.devotionalId),
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        assert response.status_code == 201, "Response body is : " + response.data.decode('utf-8')

    def test_upload_file(self):
        """
        Test case for upload_file

        uploads an image
        """
        data = dict(additionalMetadata='additionalMetadata_example',
                    file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open('/api/v1/devotionals/{devotionalId}/uploadImage'.format(devotionalId=self.devotionalId),
                                    method='POST',
                                    data=data,
                                    content_type='multipart/form-data')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
