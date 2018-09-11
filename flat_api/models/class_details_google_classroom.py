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


class ClassDetailsGoogleClassroom(object):
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
        'name': 'str',
        'alternate_link': 'str',
        'section': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'alternate_link': 'alternateLink',
        'section': 'section',
        'id': 'id'
    }

    def __init__(self, name=None, alternate_link=None, section=None, id=None):  # noqa: E501
        """ClassDetailsGoogleClassroom - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._alternate_link = None
        self._section = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if alternate_link is not None:
            self.alternate_link = alternate_link
        if section is not None:
            self.section = section
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this ClassDetailsGoogleClassroom.  # noqa: E501

        The name of the course on Google Classroom  # noqa: E501

        :return: The name of this ClassDetailsGoogleClassroom.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClassDetailsGoogleClassroom.

        The name of the course on Google Classroom  # noqa: E501

        :param name: The name of this ClassDetailsGoogleClassroom.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def alternate_link(self):
        """Gets the alternate_link of this ClassDetailsGoogleClassroom.  # noqa: E501

        Absolute link to this course in the Classroom web UI  # noqa: E501

        :return: The alternate_link of this ClassDetailsGoogleClassroom.  # noqa: E501
        :rtype: str
        """
        return self._alternate_link

    @alternate_link.setter
    def alternate_link(self, alternate_link):
        """Sets the alternate_link of this ClassDetailsGoogleClassroom.

        Absolute link to this course in the Classroom web UI  # noqa: E501

        :param alternate_link: The alternate_link of this ClassDetailsGoogleClassroom.  # noqa: E501
        :type: str
        """

        self._alternate_link = alternate_link

    @property
    def section(self):
        """Gets the section of this ClassDetailsGoogleClassroom.  # noqa: E501

        The section of the course on Google Classroom  # noqa: E501

        :return: The section of this ClassDetailsGoogleClassroom.  # noqa: E501
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this ClassDetailsGoogleClassroom.

        The section of the course on Google Classroom  # noqa: E501

        :param section: The section of this ClassDetailsGoogleClassroom.  # noqa: E501
        :type: str
        """

        self._section = section

    @property
    def id(self):
        """Gets the id of this ClassDetailsGoogleClassroom.  # noqa: E501

        The course identifier on Google Classroom  # noqa: E501

        :return: The id of this ClassDetailsGoogleClassroom.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClassDetailsGoogleClassroom.

        The course identifier on Google Classroom  # noqa: E501

        :param id: The id of this ClassDetailsGoogleClassroom.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, ClassDetailsGoogleClassroom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
