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


class UserPublicSummary(object):
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
        'username': 'str',
        'picture': 'str',
        'name': 'str',
        'firstname': 'str',
        'is_power_user': 'bool',
        'is_flat_team': 'bool',
        'lastname': 'str',
        'html_url': 'str',
        'printable_name': 'str',
        'organization_role': 'OrganizationRoles',
        'class_role': 'ClassRoles',
        'organization': 'str',
        'type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'username': 'username',
        'picture': 'picture',
        'name': 'name',
        'firstname': 'firstname',
        'is_power_user': 'isPowerUser',
        'is_flat_team': 'isFlatTeam',
        'lastname': 'lastname',
        'html_url': 'htmlUrl',
        'printable_name': 'printableName',
        'organization_role': 'organizationRole',
        'class_role': 'classRole',
        'organization': 'organization',
        'type': 'type',
        'id': 'id'
    }

    def __init__(self, username=None, picture=None, name=None, firstname=None, is_power_user=None, is_flat_team=None, lastname=None, html_url=None, printable_name=None, organization_role=None, class_role=None, organization=None, type=None, id=None):  # noqa: E501
        """UserPublicSummary - a model defined in OpenAPI"""  # noqa: E501

        self._username = None
        self._picture = None
        self._name = None
        self._firstname = None
        self._is_power_user = None
        self._is_flat_team = None
        self._lastname = None
        self._html_url = None
        self._printable_name = None
        self._organization_role = None
        self._class_role = None
        self._organization = None
        self._type = None
        self._id = None
        self.discriminator = None

        if username is not None:
            self.username = username
        self.picture = picture
        if name is not None:
            self.name = name
        if firstname is not None:
            self.firstname = firstname
        if is_power_user is not None:
            self.is_power_user = is_power_user
        if is_flat_team is not None:
            self.is_flat_team = is_flat_team
        if lastname is not None:
            self.lastname = lastname
        if html_url is not None:
            self.html_url = html_url
        if printable_name is not None:
            self.printable_name = printable_name
        if organization_role is not None:
            self.organization_role = organization_role
        if class_role is not None:
            self.class_role = class_role
        if organization is not None:
            self.organization = organization
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id

    @property
    def username(self):
        """Gets the username of this UserPublicSummary.  # noqa: E501

        The user name (unique for the organization)  # noqa: E501

        :return: The username of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserPublicSummary.

        The user name (unique for the organization)  # noqa: E501

        :param username: The username of this UserPublicSummary.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def picture(self):
        """Gets the picture of this UserPublicSummary.  # noqa: E501

        The URL of the picture to display  # noqa: E501

        :return: The picture of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this UserPublicSummary.

        The URL of the picture to display  # noqa: E501

        :param picture: The picture of this UserPublicSummary.  # noqa: E501
        :type: str
        """

        self._picture = picture

    @property
    def name(self):
        """Gets the name of this UserPublicSummary.  # noqa: E501

        A displayable name for the user (for consumer users)  # noqa: E501

        :return: The name of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserPublicSummary.

        A displayable name for the user (for consumer users)  # noqa: E501

        :param name: The name of this UserPublicSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def firstname(self):
        """Gets the firstname of this UserPublicSummary.  # noqa: E501

        Firstname of the user (for education users)  # noqa: E501

        :return: The firstname of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserPublicSummary.

        Firstname of the user (for education users)  # noqa: E501

        :param firstname: The firstname of this UserPublicSummary.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def is_power_user(self):
        """Gets the is_power_user of this UserPublicSummary.  # noqa: E501

        User license status. 'true' if user is an individual Power user  # noqa: E501

        :return: The is_power_user of this UserPublicSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_power_user

    @is_power_user.setter
    def is_power_user(self, is_power_user):
        """Sets the is_power_user of this UserPublicSummary.

        User license status. 'true' if user is an individual Power user  # noqa: E501

        :param is_power_user: The is_power_user of this UserPublicSummary.  # noqa: E501
        :type: bool
        """

        self._is_power_user = is_power_user

    @property
    def is_flat_team(self):
        """Gets the is_flat_team of this UserPublicSummary.  # noqa: E501

        Will be 'true' if user is part of the Flat Team  # noqa: E501

        :return: The is_flat_team of this UserPublicSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_flat_team

    @is_flat_team.setter
    def is_flat_team(self, is_flat_team):
        """Sets the is_flat_team of this UserPublicSummary.

        Will be 'true' if user is part of the Flat Team  # noqa: E501

        :param is_flat_team: The is_flat_team of this UserPublicSummary.  # noqa: E501
        :type: bool
        """

        self._is_flat_team = is_flat_team

    @property
    def lastname(self):
        """Gets the lastname of this UserPublicSummary.  # noqa: E501

        Lastname of the user (for education users)  # noqa: E501

        :return: The lastname of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserPublicSummary.

        Lastname of the user (for education users)  # noqa: E501

        :param lastname: The lastname of this UserPublicSummary.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def html_url(self):
        """Gets the html_url of this UserPublicSummary.  # noqa: E501

        Link to user profile (for Indiv. users only)  # noqa: E501

        :return: The html_url of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this UserPublicSummary.

        Link to user profile (for Indiv. users only)  # noqa: E501

        :param html_url: The html_url of this UserPublicSummary.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def printable_name(self):
        """Gets the printable_name of this UserPublicSummary.  # noqa: E501

        The name that can be directly printed (name, firstname & lastname, or username)  # noqa: E501

        :return: The printable_name of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._printable_name

    @printable_name.setter
    def printable_name(self, printable_name):
        """Sets the printable_name of this UserPublicSummary.

        The name that can be directly printed (name, firstname & lastname, or username)  # noqa: E501

        :param printable_name: The printable_name of this UserPublicSummary.  # noqa: E501
        :type: str
        """

        self._printable_name = printable_name

    @property
    def organization_role(self):
        """Gets the organization_role of this UserPublicSummary.  # noqa: E501


        :return: The organization_role of this UserPublicSummary.  # noqa: E501
        :rtype: OrganizationRoles
        """
        return self._organization_role

    @organization_role.setter
    def organization_role(self, organization_role):
        """Sets the organization_role of this UserPublicSummary.


        :param organization_role: The organization_role of this UserPublicSummary.  # noqa: E501
        :type: OrganizationRoles
        """

        self._organization_role = organization_role

    @property
    def class_role(self):
        """Gets the class_role of this UserPublicSummary.  # noqa: E501


        :return: The class_role of this UserPublicSummary.  # noqa: E501
        :rtype: ClassRoles
        """
        return self._class_role

    @class_role.setter
    def class_role(self, class_role):
        """Sets the class_role of this UserPublicSummary.


        :param class_role: The class_role of this UserPublicSummary.  # noqa: E501
        :type: ClassRoles
        """

        self._class_role = class_role

    @property
    def organization(self):
        """Gets the organization of this UserPublicSummary.  # noqa: E501

        Organization ID (for Edu users only)  # noqa: E501

        :return: The organization of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this UserPublicSummary.

        Organization ID (for Edu users only)  # noqa: E501

        :param organization: The organization of this UserPublicSummary.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def type(self):
        """Gets the type of this UserPublicSummary.  # noqa: E501

        The type of user account  # noqa: E501

        :return: The type of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserPublicSummary.

        The type of user account  # noqa: E501

        :param type: The type of this UserPublicSummary.  # noqa: E501
        :type: str
        """
        allowed_values = ["user", "guest"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """Gets the id of this UserPublicSummary.  # noqa: E501

        The user unique identifier  # noqa: E501

        :return: The id of this UserPublicSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserPublicSummary.

        The user unique identifier  # noqa: E501

        :param id: The id of this UserPublicSummary.  # noqa: E501
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
        if not isinstance(other, UserPublicSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
