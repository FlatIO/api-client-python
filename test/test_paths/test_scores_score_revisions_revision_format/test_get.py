# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import flat_api
from flat_api.paths.scores_score_revisions_revision_format import get  # noqa: E501
from flat_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestScoresScoreRevisionsRevisionFormat(ApiTestMixin, unittest.TestCase):
    """
    ScoresScoreRevisionsRevisionFormat unit test stubs
        Get a score revision data  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
















if __name__ == '__main__':
    unittest.main()
