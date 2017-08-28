# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML or MIDI files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html) 

    OpenAPI spec version: 2.2.0
    Contact: developers@flat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'username': 'str',
        'name': 'str',
        'printable_name': 'str',
        'picture': 'str',
        'is_power_user': 'bool',
        'organization': 'str',
        'organization_role': 'OrganizationRoles',
        'class_role': 'ClassRoles',
        'html_url': 'str',
        'bio': 'str',
        'registration_date': 'datetime',
        'liked_scores_count': 'int',
        'followers_count': 'int',
        'following_count': 'int',
        'owned_public_scores_count': 'int',
        'profile_theme': 'str',
        'instruments': 'UserInstruments',
        'type': 'str',
        'private_profile': 'bool',
        'locale': 'FlatLocales'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'name': 'name',
        'printable_name': 'printableName',
        'picture': 'picture',
        'is_power_user': 'isPowerUser',
        'organization': 'organization',
        'organization_role': 'organizationRole',
        'class_role': 'classRole',
        'html_url': 'htmlUrl',
        'bio': 'bio',
        'registration_date': 'registrationDate',
        'liked_scores_count': 'likedScoresCount',
        'followers_count': 'followersCount',
        'following_count': 'followingCount',
        'owned_public_scores_count': 'ownedPublicScoresCount',
        'profile_theme': 'profileTheme',
        'instruments': 'instruments',
        'type': 'type',
        'private_profile': 'privateProfile',
        'locale': 'locale'
    }

    def __init__(self, id=None, username=None, name=None, printable_name=None, picture=None, is_power_user=None, organization=None, organization_role=None, class_role=None, html_url=None, bio=None, registration_date=None, liked_scores_count=None, followers_count=None, following_count=None, owned_public_scores_count=None, profile_theme=None, instruments=None, type=None, private_profile=None, locale=None):
        """
        UserDetails - a model defined in Swagger
        """

        self._id = None
        self._username = None
        self._name = None
        self._printable_name = None
        self._picture = None
        self._is_power_user = None
        self._organization = None
        self._organization_role = None
        self._class_role = None
        self._html_url = None
        self._bio = None
        self._registration_date = None
        self._liked_scores_count = None
        self._followers_count = None
        self._following_count = None
        self._owned_public_scores_count = None
        self._profile_theme = None
        self._instruments = None
        self._type = None
        self._private_profile = None
        self._locale = None

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
        if organization is not None:
          self.organization = organization
        if organization_role is not None:
          self.organization_role = organization_role
        if class_role is not None:
          self.class_role = class_role
        if html_url is not None:
          self.html_url = html_url
        if bio is not None:
          self.bio = bio
        if registration_date is not None:
          self.registration_date = registration_date
        if liked_scores_count is not None:
          self.liked_scores_count = liked_scores_count
        if followers_count is not None:
          self.followers_count = followers_count
        if following_count is not None:
          self.following_count = following_count
        if owned_public_scores_count is not None:
          self.owned_public_scores_count = owned_public_scores_count
        if profile_theme is not None:
          self.profile_theme = profile_theme
        if instruments is not None:
          self.instruments = instruments
        if type is not None:
          self.type = type
        if private_profile is not None:
          self.private_profile = private_profile
        if locale is not None:
          self.locale = locale

    @property
    def id(self):
        """
        Gets the id of this UserDetails.
        Identifier of the user

        :return: The id of this UserDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserDetails.
        Identifier of the user

        :param id: The id of this UserDetails.
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this UserDetails.
        The user name (unique for the organization)

        :return: The username of this UserDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserDetails.
        The user name (unique for the organization)

        :param username: The username of this UserDetails.
        :type: str
        """

        self._username = username

    @property
    def name(self):
        """
        Gets the name of this UserDetails.
        A displayable name for the user

        :return: The name of this UserDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserDetails.
        A displayable name for the user

        :param name: The name of this UserDetails.
        :type: str
        """

        self._name = name

    @property
    def printable_name(self):
        """
        Gets the printable_name of this UserDetails.
        The name that can be directly printed (name or username)

        :return: The printable_name of this UserDetails.
        :rtype: str
        """
        return self._printable_name

    @printable_name.setter
    def printable_name(self, printable_name):
        """
        Sets the printable_name of this UserDetails.
        The name that can be directly printed (name or username)

        :param printable_name: The printable_name of this UserDetails.
        :type: str
        """

        self._printable_name = printable_name

    @property
    def picture(self):
        """
        Gets the picture of this UserDetails.
        User pictue

        :return: The picture of this UserDetails.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """
        Sets the picture of this UserDetails.
        User pictue

        :param picture: The picture of this UserDetails.
        :type: str
        """

        self._picture = picture

    @property
    def is_power_user(self):
        """
        Gets the is_power_user of this UserDetails.
        User license status. 'True' if user is an individual Power user

        :return: The is_power_user of this UserDetails.
        :rtype: bool
        """
        return self._is_power_user

    @is_power_user.setter
    def is_power_user(self, is_power_user):
        """
        Sets the is_power_user of this UserDetails.
        User license status. 'True' if user is an individual Power user

        :param is_power_user: The is_power_user of this UserDetails.
        :type: bool
        """

        self._is_power_user = is_power_user

    @property
    def organization(self):
        """
        Gets the organization of this UserDetails.
        Organization ID (for Edu users only)

        :return: The organization of this UserDetails.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this UserDetails.
        Organization ID (for Edu users only)

        :param organization: The organization of this UserDetails.
        :type: str
        """

        self._organization = organization

    @property
    def organization_role(self):
        """
        Gets the organization_role of this UserDetails.

        :return: The organization_role of this UserDetails.
        :rtype: OrganizationRoles
        """
        return self._organization_role

    @organization_role.setter
    def organization_role(self, organization_role):
        """
        Sets the organization_role of this UserDetails.

        :param organization_role: The organization_role of this UserDetails.
        :type: OrganizationRoles
        """

        self._organization_role = organization_role

    @property
    def class_role(self):
        """
        Gets the class_role of this UserDetails.

        :return: The class_role of this UserDetails.
        :rtype: ClassRoles
        """
        return self._class_role

    @class_role.setter
    def class_role(self, class_role):
        """
        Sets the class_role of this UserDetails.

        :param class_role: The class_role of this UserDetails.
        :type: ClassRoles
        """

        self._class_role = class_role

    @property
    def html_url(self):
        """
        Gets the html_url of this UserDetails.
        Link to user profile (for Indiv. users only)

        :return: The html_url of this UserDetails.
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """
        Sets the html_url of this UserDetails.
        Link to user profile (for Indiv. users only)

        :param html_url: The html_url of this UserDetails.
        :type: str
        """

        self._html_url = html_url

    @property
    def bio(self):
        """
        Gets the bio of this UserDetails.
        User's biography

        :return: The bio of this UserDetails.
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """
        Sets the bio of this UserDetails.
        User's biography

        :param bio: The bio of this UserDetails.
        :type: str
        """

        self._bio = bio

    @property
    def registration_date(self):
        """
        Gets the registration_date of this UserDetails.
        Date the user signed up

        :return: The registration_date of this UserDetails.
        :rtype: datetime
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """
        Sets the registration_date of this UserDetails.
        Date the user signed up

        :param registration_date: The registration_date of this UserDetails.
        :type: datetime
        """

        self._registration_date = registration_date

    @property
    def liked_scores_count(self):
        """
        Gets the liked_scores_count of this UserDetails.
        Number of the scores liked by the user

        :return: The liked_scores_count of this UserDetails.
        :rtype: int
        """
        return self._liked_scores_count

    @liked_scores_count.setter
    def liked_scores_count(self, liked_scores_count):
        """
        Sets the liked_scores_count of this UserDetails.
        Number of the scores liked by the user

        :param liked_scores_count: The liked_scores_count of this UserDetails.
        :type: int
        """

        self._liked_scores_count = liked_scores_count

    @property
    def followers_count(self):
        """
        Gets the followers_count of this UserDetails.
        Number of followers the user have

        :return: The followers_count of this UserDetails.
        :rtype: int
        """
        return self._followers_count

    @followers_count.setter
    def followers_count(self, followers_count):
        """
        Sets the followers_count of this UserDetails.
        Number of followers the user have

        :param followers_count: The followers_count of this UserDetails.
        :type: int
        """

        self._followers_count = followers_count

    @property
    def following_count(self):
        """
        Gets the following_count of this UserDetails.
        Number of people the user follow

        :return: The following_count of this UserDetails.
        :rtype: int
        """
        return self._following_count

    @following_count.setter
    def following_count(self, following_count):
        """
        Sets the following_count of this UserDetails.
        Number of people the user follow

        :param following_count: The following_count of this UserDetails.
        :type: int
        """

        self._following_count = following_count

    @property
    def owned_public_scores_count(self):
        """
        Gets the owned_public_scores_count of this UserDetails.
        Number of public scores the user have

        :return: The owned_public_scores_count of this UserDetails.
        :rtype: int
        """
        return self._owned_public_scores_count

    @owned_public_scores_count.setter
    def owned_public_scores_count(self, owned_public_scores_count):
        """
        Sets the owned_public_scores_count of this UserDetails.
        Number of public scores the user have

        :param owned_public_scores_count: The owned_public_scores_count of this UserDetails.
        :type: int
        """

        self._owned_public_scores_count = owned_public_scores_count

    @property
    def profile_theme(self):
        """
        Gets the profile_theme of this UserDetails.
        Theme (background) for the profile

        :return: The profile_theme of this UserDetails.
        :rtype: str
        """
        return self._profile_theme

    @profile_theme.setter
    def profile_theme(self, profile_theme):
        """
        Sets the profile_theme of this UserDetails.
        Theme (background) for the profile

        :param profile_theme: The profile_theme of this UserDetails.
        :type: str
        """

        self._profile_theme = profile_theme

    @property
    def instruments(self):
        """
        Gets the instruments of this UserDetails.

        :return: The instruments of this UserDetails.
        :rtype: UserInstruments
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """
        Sets the instruments of this UserDetails.

        :param instruments: The instruments of this UserDetails.
        :type: UserInstruments
        """

        self._instruments = instruments

    @property
    def type(self):
        """
        Gets the type of this UserDetails.
        The type of account

        :return: The type of this UserDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserDetails.
        The type of account

        :param type: The type of this UserDetails.
        :type: str
        """
        allowed_values = ["user", "guest"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def private_profile(self):
        """
        Gets the private_profile of this UserDetails.
        Tell either this user profile is private or not (individual accounts only)

        :return: The private_profile of this UserDetails.
        :rtype: bool
        """
        return self._private_profile

    @private_profile.setter
    def private_profile(self, private_profile):
        """
        Sets the private_profile of this UserDetails.
        Tell either this user profile is private or not (individual accounts only)

        :param private_profile: The private_profile of this UserDetails.
        :type: bool
        """

        self._private_profile = private_profile

    @property
    def locale(self):
        """
        Gets the locale of this UserDetails.

        :return: The locale of this UserDetails.
        :rtype: FlatLocales
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this UserDetails.

        :param locale: The locale of this UserDetails.
        :type: FlatLocales
        """

        self._locale = locale

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UserDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
