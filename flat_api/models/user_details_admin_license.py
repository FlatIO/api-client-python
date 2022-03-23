# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and introduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    The version of the OpenAPI document: 2.17.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from flat_api.configuration import Configuration


class UserDetailsAdminLicense(object):
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
        'expiration_date': 'datetime',
        'source': 'LicenseSources',
        'mode': 'LicenseMode',
        'active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'expiration_date': 'expirationDate',
        'source': 'source',
        'mode': 'mode',
        'active': 'active'
    }

    def __init__(self, id=None, expiration_date=None, source=None, mode=None, active=None, local_vars_configuration=None):  # noqa: E501
        """UserDetailsAdminLicense - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._expiration_date = None
        self._source = None
        self._mode = None
        self._active = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if source is not None:
            self.source = source
        if mode is not None:
            self.mode = mode
        if active is not None:
            self.active = active

    @property
    def id(self):
        """Gets the id of this UserDetailsAdminLicense.  # noqa: E501

        ID of the current license  # noqa: E501

        :return: The id of this UserDetailsAdminLicense.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDetailsAdminLicense.

        ID of the current license  # noqa: E501

        :param id: The id of this UserDetailsAdminLicense.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def expiration_date(self):
        """Gets the expiration_date of this UserDetailsAdminLicense.  # noqa: E501

        Date when the license expires  # noqa: E501

        :return: The expiration_date of this UserDetailsAdminLicense.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this UserDetailsAdminLicense.

        Date when the license expires  # noqa: E501

        :param expiration_date: The expiration_date of this UserDetailsAdminLicense.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def source(self):
        """Gets the source of this UserDetailsAdminLicense.  # noqa: E501


        :return: The source of this UserDetailsAdminLicense.  # noqa: E501
        :rtype: LicenseSources
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UserDetailsAdminLicense.


        :param source: The source of this UserDetailsAdminLicense.  # noqa: E501
        :type: LicenseSources
        """

        self._source = source

    @property
    def mode(self):
        """Gets the mode of this UserDetailsAdminLicense.  # noqa: E501


        :return: The mode of this UserDetailsAdminLicense.  # noqa: E501
        :rtype: LicenseMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this UserDetailsAdminLicense.


        :param mode: The mode of this UserDetailsAdminLicense.  # noqa: E501
        :type: LicenseMode
        """

        self._mode = mode

    @property
    def active(self):
        """Gets the active of this UserDetailsAdminLicense.  # noqa: E501

        ID of the current license  # noqa: E501

        :return: The active of this UserDetailsAdminLicense.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UserDetailsAdminLicense.

        ID of the current license  # noqa: E501

        :param active: The active of this UserDetailsAdminLicense.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if not isinstance(other, UserDetailsAdminLicense):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserDetailsAdminLicense):
            return True

        return self.to_dict() != other.to_dict()
