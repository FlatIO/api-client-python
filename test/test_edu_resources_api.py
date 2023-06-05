"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and introduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    The version of the OpenAPI document: 2.18.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import flat_api
from flat_api.api.edu_resources_api import EduResourcesApi  # noqa: E501


class TestEduResourcesApi(unittest.TestCase):
    """EduResourcesApi unit test stubs"""

    def setUp(self):
        self.api = EduResourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_copy_edu_resource(self):
        """Test case for copy_edu_resource

        Copy an education resource to a Resource Library  # noqa: E501
        """
        pass

    def test_copy_edu_resource_to_demo_class(self):
        """Test case for copy_edu_resource_to_demo_class

        Copy an education assignment to a teacher demo class  # noqa: E501
        """
        pass

    def test_create_edu_resource(self):
        """Test case for create_edu_resource

        Create a new education resource  # noqa: E501
        """
        pass

    def test_delete_edu_resource(self):
        """Test case for delete_edu_resource

        Delete an education resource  # noqa: E501
        """
        pass

    def test_get_edu_resource(self):
        """Test case for get_edu_resource

        Get an education resource  # noqa: E501
        """
        pass

    def test_list_edu_libraries(self):
        """Test case for list_edu_libraries

        List the education libraries  # noqa: E501
        """
        pass

    def test_list_edu_resources(self):
        """Test case for list_edu_resources

        List education resources in a library or folder  # noqa: E501
        """
        pass

    def test_move_edu_resource(self):
        """Test case for move_edu_resource

        Move an education resource  # noqa: E501
        """
        pass

    def test_update_edu_resource(self):
        """Test case for update_edu_resource

        Update an education resource metadata  # noqa: E501
        """
        pass

    def test_update_edu_resource_assignment(self):
        """Test case for update_edu_resource_assignment

        Update an education resource assignment  # noqa: E501
        """
        pass

    def test_use_edu_resource_in_class(self):
        """Test case for use_edu_resource_in_class

        Use an education resource in a class  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()