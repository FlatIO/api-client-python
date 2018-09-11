# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import flat_api
from flat_api.api.organization_api import OrganizationApi  # noqa: E501
from flat_api.rest import ApiException


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self):
        self.api = flat_api.api.organization_api.OrganizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_lti_credentials(self):
        """Test case for create_lti_credentials

        Create a new couple of LTI 1.x credentials  # noqa: E501
        """
        pass

    def test_create_organization_invitation(self):
        """Test case for create_organization_invitation

        Create a new invitation to join the organization  # noqa: E501
        """
        pass

    def test_create_organization_user(self):
        """Test case for create_organization_user

        Create a new user account  # noqa: E501
        """
        pass

    def test_list_lti_credentials(self):
        """Test case for list_lti_credentials

        List LTI 1.x credentials  # noqa: E501
        """
        pass

    def test_list_organization_invitations(self):
        """Test case for list_organization_invitations

        List the organization invitations  # noqa: E501
        """
        pass

    def test_list_organization_users(self):
        """Test case for list_organization_users

        List the organization users  # noqa: E501
        """
        pass

    def test_remove_organization_invitation(self):
        """Test case for remove_organization_invitation

        Remove an organization invitation  # noqa: E501
        """
        pass

    def test_remove_organization_user(self):
        """Test case for remove_organization_user

        Remove an account from Flat  # noqa: E501
        """
        pass

    def test_revoke_lti_credentials(self):
        """Test case for revoke_lti_credentials

        Revoke LTI 1.x credentials  # noqa: E501
        """
        pass

    def test_update_organization_user(self):
        """Test case for update_organization_user

        Update account information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
