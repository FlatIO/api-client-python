# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ResourceRights(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'acl_read': 'bool',
        'acl_write': 'bool',
        'acl_admin': 'bool',
        'is_collaborator': 'bool'
    }

    attribute_map = {
        'acl_read': 'aclRead',
        'acl_write': 'aclWrite',
        'acl_admin': 'aclAdmin',
        'is_collaborator': 'isCollaborator'
    }

    def __init__(self, acl_read=False, acl_write=False, acl_admin=False, is_collaborator=False):  # noqa: E501
        """ResourceRights - a model defined in OpenAPI"""  # noqa: E501

        self._acl_read = None
        self._acl_write = None
        self._acl_admin = None
        self._is_collaborator = None
        self.discriminator = None

        if acl_read is not None:
            self.acl_read = acl_read
        if acl_write is not None:
            self.acl_write = acl_write
        if acl_admin is not None:
            self.acl_admin = acl_admin
        if is_collaborator is not None:
            self.is_collaborator = is_collaborator

    @property
    def acl_read(self):
        """Gets the acl_read of this ResourceRights.  # noqa: E501

        `True` if the current user can read the current document   # noqa: E501

        :return: The acl_read of this ResourceRights.  # noqa: E501
        :rtype: bool
        """
        return self._acl_read

    @acl_read.setter
    def acl_read(self, acl_read):
        """Sets the acl_read of this ResourceRights.

        `True` if the current user can read the current document   # noqa: E501

        :param acl_read: The acl_read of this ResourceRights.  # noqa: E501
        :type: bool
        """

        self._acl_read = acl_read

    @property
    def acl_write(self):
        """Gets the acl_write of this ResourceRights.  # noqa: E501

        `True` if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the `capabilities` property as the end-user to have the complete possibilities with the collection.   # noqa: E501

        :return: The acl_write of this ResourceRights.  # noqa: E501
        :rtype: bool
        """
        return self._acl_write

    @acl_write.setter
    def acl_write(self, acl_write):
        """Sets the acl_write of this ResourceRights.

        `True` if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the `capabilities` property as the end-user to have the complete possibilities with the collection.   # noqa: E501

        :param acl_write: The acl_write of this ResourceRights.  # noqa: E501
        :type: bool
        """

        self._acl_write = acl_write

    @property
    def acl_admin(self):
        """Gets the acl_admin of this ResourceRights.  # noqa: E501

        `True` if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the `capabilities` property as the end-user to have the complete possibilities with the collection.   # noqa: E501

        :return: The acl_admin of this ResourceRights.  # noqa: E501
        :rtype: bool
        """
        return self._acl_admin

    @acl_admin.setter
    def acl_admin(self, acl_admin):
        """Sets the acl_admin of this ResourceRights.

        `True` if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the `capabilities` property as the end-user to have the complete possibilities with the collection.   # noqa: E501

        :param acl_admin: The acl_admin of this ResourceRights.  # noqa: E501
        :type: bool
        """

        self._acl_admin = acl_admin

    @property
    def is_collaborator(self):
        """Gets the is_collaborator of this ResourceRights.  # noqa: E501

        `True` if the current user is a collaborator of the current document (direct or via group).   # noqa: E501

        :return: The is_collaborator of this ResourceRights.  # noqa: E501
        :rtype: bool
        """
        return self._is_collaborator

    @is_collaborator.setter
    def is_collaborator(self, is_collaborator):
        """Sets the is_collaborator of this ResourceRights.

        `True` if the current user is a collaborator of the current document (direct or via group).   # noqa: E501

        :param is_collaborator: The is_collaborator of this ResourceRights.  # noqa: E501
        :type: bool
        """

        self._is_collaborator = is_collaborator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
