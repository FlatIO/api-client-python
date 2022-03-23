# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and introduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    OpenAPI spec version: 2.17.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ScoreCreationBuilderData(object):
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
        'score_data': 'ScoreCreationBuilderDataScoreData',
        'layout_data': 'ScoreCreationBuilderDataLayoutData'
    }

    attribute_map = {
        'score_data': 'scoreData',
        'layout_data': 'layoutData'
    }

    def __init__(self, score_data=None, layout_data=None):  # noqa: E501
        """ScoreCreationBuilderData - a model defined in OpenAPI"""  # noqa: E501

        self._score_data = None
        self._layout_data = None
        self.discriminator = None

        if score_data is not None:
            self.score_data = score_data
        if layout_data is not None:
            self.layout_data = layout_data

    @property
    def score_data(self):
        """Gets the score_data of this ScoreCreationBuilderData.  # noqa: E501


        :return: The score_data of this ScoreCreationBuilderData.  # noqa: E501
        :rtype: ScoreCreationBuilderDataScoreData
        """
        return self._score_data

    @score_data.setter
    def score_data(self, score_data):
        """Sets the score_data of this ScoreCreationBuilderData.


        :param score_data: The score_data of this ScoreCreationBuilderData.  # noqa: E501
        :type: ScoreCreationBuilderDataScoreData
        """

        self._score_data = score_data

    @property
    def layout_data(self):
        """Gets the layout_data of this ScoreCreationBuilderData.  # noqa: E501


        :return: The layout_data of this ScoreCreationBuilderData.  # noqa: E501
        :rtype: ScoreCreationBuilderDataLayoutData
        """
        return self._layout_data

    @layout_data.setter
    def layout_data(self, layout_data):
        """Sets the layout_data of this ScoreCreationBuilderData.


        :param layout_data: The layout_data of this ScoreCreationBuilderData.  # noqa: E501
        :type: ScoreCreationBuilderDataLayoutData
        """

        self._layout_data = layout_data

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
        if not isinstance(other, ScoreCreationBuilderData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other