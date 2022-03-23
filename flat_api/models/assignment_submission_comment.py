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


class AssignmentSubmissionComment(object):
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
        'user': 'str',
        'submission': 'str',
        'date': 'datetime',
        'modification_date': 'datetime',
        'comment': 'str',
        'unread': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'submission': 'submission',
        'date': 'date',
        'modification_date': 'modificationDate',
        'comment': 'comment',
        'unread': 'unread'
    }

    def __init__(self, id=None, user=None, submission=None, date=None, modification_date=None, comment=None, unread=None):  # noqa: E501
        """AssignmentSubmissionComment - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._user = None
        self._submission = None
        self._date = None
        self._modification_date = None
        self._comment = None
        self._unread = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if submission is not None:
            self.submission = submission
        if date is not None:
            self.date = date
        if modification_date is not None:
            self.modification_date = modification_date
        if comment is not None:
            self.comment = comment
        if unread is not None:
            self.unread = unread

    @property
    def id(self):
        """Gets the id of this AssignmentSubmissionComment.  # noqa: E501

        The comment unique identifier  # noqa: E501

        :return: The id of this AssignmentSubmissionComment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssignmentSubmissionComment.

        The comment unique identifier  # noqa: E501

        :param id: The id of this AssignmentSubmissionComment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this AssignmentSubmissionComment.  # noqa: E501

        The author unique identifier  # noqa: E501

        :return: The user of this AssignmentSubmissionComment.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AssignmentSubmissionComment.

        The author unique identifier  # noqa: E501

        :param user: The user of this AssignmentSubmissionComment.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def submission(self):
        """Gets the submission of this AssignmentSubmissionComment.  # noqa: E501

        The submission unique identifier  # noqa: E501

        :return: The submission of this AssignmentSubmissionComment.  # noqa: E501
        :rtype: str
        """
        return self._submission

    @submission.setter
    def submission(self, submission):
        """Sets the submission of this AssignmentSubmissionComment.

        The submission unique identifier  # noqa: E501

        :param submission: The submission of this AssignmentSubmissionComment.  # noqa: E501
        :type: str
        """

        self._submission = submission

    @property
    def date(self):
        """Gets the date of this AssignmentSubmissionComment.  # noqa: E501

        The date when the comment was posted  # noqa: E501

        :return: The date of this AssignmentSubmissionComment.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this AssignmentSubmissionComment.

        The date when the comment was posted  # noqa: E501

        :param date: The date of this AssignmentSubmissionComment.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def modification_date(self):
        """Gets the modification_date of this AssignmentSubmissionComment.  # noqa: E501

        The date of the last comment modification  # noqa: E501

        :return: The modification_date of this AssignmentSubmissionComment.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this AssignmentSubmissionComment.

        The date of the last comment modification  # noqa: E501

        :param modification_date: The modification_date of this AssignmentSubmissionComment.  # noqa: E501
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def comment(self):
        """Gets the comment of this AssignmentSubmissionComment.  # noqa: E501

        The comment text  # noqa: E501

        :return: The comment of this AssignmentSubmissionComment.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AssignmentSubmissionComment.

        The comment text  # noqa: E501

        :param comment: The comment of this AssignmentSubmissionComment.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def unread(self):
        """Gets the unread of this AssignmentSubmissionComment.  # noqa: E501

        True if the comment is unread by the current user  # noqa: E501

        :return: The unread of this AssignmentSubmissionComment.  # noqa: E501
        :rtype: bool
        """
        return self._unread

    @unread.setter
    def unread(self, unread):
        """Sets the unread of this AssignmentSubmissionComment.

        True if the comment is unread by the current user  # noqa: E501

        :param unread: The unread of this AssignmentSubmissionComment.  # noqa: E501
        :type: bool
        """

        self._unread = unread

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
        if not isinstance(other, AssignmentSubmissionComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other