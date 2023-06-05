# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import flat_api
from flat_api.paths.edu_resources_resource_copy import post  # noqa: E501
from flat_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEduResourcesResourceCopy(ApiTestMixin, unittest.TestCase):
    """
    EduResourcesResourceCopy unit test stubs
        Copy an education resource to a Resource Library  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
