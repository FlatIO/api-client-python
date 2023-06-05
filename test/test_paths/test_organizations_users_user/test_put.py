# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import flat_api
from flat_api.paths.organizations_users_user import put  # noqa: E501
from flat_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOrganizationsUsersUser(ApiTestMixin, unittest.TestCase):
    """
    OrganizationsUsersUser unit test stubs
        Update account information  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()