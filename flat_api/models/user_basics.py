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


class UserBasics(object):
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
        'id': 'str',
        'username': 'str',
        'name': 'str',
        'printable_name': 'str',
        'picture': 'str',
        'is_power_user': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'name': 'name',
        'printable_name': 'printableName',
        'picture': 'picture',
        'is_power_user': 'isPowerUser'
    }

    discriminator_value_class_map = {
        'UserDetails': 'UserDetails',
        'UserPublic': 'UserPublic',
        'UserPublicSummary': 'UserPublicSummary',
        'UserDetailsAdmin': 'UserDetailsAdmin'
    }

    def __init__(self, id=None, username=None, name=None, printable_name=None, picture=None, is_power_user=None):  # noqa: E501
        """UserBasics - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._username = None
        self._name = None
        self._printable_name = None
        self._picture = None
        self._is_power_user = None
        self.discriminator = 'userType'

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if name is not None:
            self.name = name
        if printable_name is not None:
            self.printable_name = printable_name
        if picture is not None:
            self.picture = picture
        if is_power_user is not None:
            self.is_power_user = is_power_user

    @property
    def id(self):
        """Gets the id of this UserBasics.  # noqa: E501

        The user unique identifier  # noqa: E501

        :return: The id of this UserBasics.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserBasics.

        The user unique identifier  # noqa: E501

        :param id: The id of this UserBasics.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this UserBasics.  # noqa: E501

        The user name (unique for the organization)  # noqa: E501

        :return: The username of this UserBasics.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserBasics.

        The user name (unique for the organization)  # noqa: E501

        :param username: The username of this UserBasics.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def name(self):
        """Gets the name of this UserBasics.  # noqa: E501

        A displayable name for the user  # noqa: E501

        :return: The name of this UserBasics.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserBasics.

        A displayable name for the user  # noqa: E501

        :param name: The name of this UserBasics.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def printable_name(self):
        """Gets the printable_name of this UserBasics.  # noqa: E501

        The name that can be directly printed (name or username)  # noqa: E501

        :return: The printable_name of this UserBasics.  # noqa: E501
        :rtype: str
        """
        return self._printable_name

    @printable_name.setter
    def printable_name(self, printable_name):
        """Sets the printable_name of this UserBasics.

        The name that can be directly printed (name or username)  # noqa: E501

        :param printable_name: The printable_name of this UserBasics.  # noqa: E501
        :type: str
        """

        self._printable_name = printable_name

    @property
    def picture(self):
        """Gets the picture of this UserBasics.  # noqa: E501

        User pictue  # noqa: E501

        :return: The picture of this UserBasics.  # noqa: E501
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this UserBasics.

        User pictue  # noqa: E501

        :param picture: The picture of this UserBasics.  # noqa: E501
        :type: str
        """

        self._picture = picture

    @property
    def is_power_user(self):
        """Gets the is_power_user of this UserBasics.  # noqa: E501

        User license status. 'True' if user is an individual Power user  # noqa: E501

        :return: The is_power_user of this UserBasics.  # noqa: E501
        :rtype: bool
        """
        return self._is_power_user

    @is_power_user.setter
    def is_power_user(self, is_power_user):
        """Sets the is_power_user of this UserBasics.

        User license status. 'True' if user is an individual Power user  # noqa: E501

        :param is_power_user: The is_power_user of this UserBasics.  # noqa: E501
        :type: bool
        """

        self._is_power_user = is_power_user

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, UserBasics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
