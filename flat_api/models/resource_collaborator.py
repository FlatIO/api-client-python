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


class ResourceCollaborator(object):
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
        'score': 'str',
        'collection': 'str',
        'user': 'UserPublic',
        'group': 'Group',
        'user_email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'score': 'score',
        'collection': 'collection',
        'user': 'user',
        'group': 'group',
        'user_email': 'userEmail'
    }

    def __init__(self, id=None, score=None, collection=None, user=None, group=None, user_email=None):  # noqa: E501
        """ResourceCollaborator - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._score = None
        self._collection = None
        self._user = None
        self._group = None
        self._user_email = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if score is not None:
            self.score = score
        if collection is not None:
            self.collection = collection
        if user is not None:
            self.user = user
        if group is not None:
            self.group = group
        if user_email is not None:
            self.user_email = user_email

    @property
    def id(self):
        """Gets the id of this ResourceCollaborator.  # noqa: E501

        The unique identifier of the permission  # noqa: E501

        :return: The id of this ResourceCollaborator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceCollaborator.

        The unique identifier of the permission  # noqa: E501

        :param id: The id of this ResourceCollaborator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def score(self):
        """Gets the score of this ResourceCollaborator.  # noqa: E501

        If this object is a permission of a score, this property will contain the unique identifier of the score  # noqa: E501

        :return: The score of this ResourceCollaborator.  # noqa: E501
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ResourceCollaborator.

        If this object is a permission of a score, this property will contain the unique identifier of the score  # noqa: E501

        :param score: The score of this ResourceCollaborator.  # noqa: E501
        :type: str
        """

        self._score = score

    @property
    def collection(self):
        """Gets the collection of this ResourceCollaborator.  # noqa: E501

        If this object is a permission of a collection, this property will contain the unique identifier of the collection  # noqa: E501

        :return: The collection of this ResourceCollaborator.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this ResourceCollaborator.

        If this object is a permission of a collection, this property will contain the unique identifier of the collection  # noqa: E501

        :param collection: The collection of this ResourceCollaborator.  # noqa: E501
        :type: str
        """

        self._collection = collection

    @property
    def user(self):
        """Gets the user of this ResourceCollaborator.  # noqa: E501


        :return: The user of this ResourceCollaborator.  # noqa: E501
        :rtype: UserPublic
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ResourceCollaborator.


        :param user: The user of this ResourceCollaborator.  # noqa: E501
        :type: UserPublic
        """

        self._user = user

    @property
    def group(self):
        """Gets the group of this ResourceCollaborator.  # noqa: E501


        :return: The group of this ResourceCollaborator.  # noqa: E501
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ResourceCollaborator.


        :param group: The group of this ResourceCollaborator.  # noqa: E501
        :type: Group
        """

        self._group = group

    @property
    def user_email(self):
        """Gets the user_email of this ResourceCollaborator.  # noqa: E501

        If the collaborator is not a user of Flat yet, this field will contain his email.   # noqa: E501

        :return: The user_email of this ResourceCollaborator.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this ResourceCollaborator.

        If the collaborator is not a user of Flat yet, this field will contain his email.   # noqa: E501

        :param user_email: The user_email of this ResourceCollaborator.  # noqa: E501
        :type: str
        """

        self._user_email = user_email

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
        if not isinstance(other, ResourceCollaborator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
