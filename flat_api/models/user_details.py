# coding: utf-8

"""
    Flat API

    # Introduction The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:     - Creating and importing new music scores using MusicXML or MIDI files    - Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI)    - Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  # Beta Please note that this public API is currently in beta and subject to change.  Our whole platform and apps are based on this API, however not all the endpoints are available publicly yet. Feel free to [contact us](mailto:developers@flat.io) if you have any questions, feedback or features requests.  We don't offer any guarantees during this beta period. By using this API, you agree to update your app in a timely fashion in response to any beta-period changes that are rolled out.  By using this API, and especially on the behalf of a user account, you must accept, respect and enforce our [Terms of Service and Privacy Policy](https://flat.io/legal).  # SDKs  Our team maintains the following SDKs:   - [Python](https://github.com/FlatIO/api-client-python)   - [JavaScript (Node.js and Browser)](https://github.com/FlatIO/api-client-js)   - [PHP](https://github.com/FlatIO/api-client-php)  # Authentication The Flat API supports OAuth2, you can request API credentials [on our website](https://flat.io/developers). We provide two types of credentials:    - **Account Access Tokens**: Simple access tokens that allow to try and use this API **with your own account**. This is a great solution to create private apps.   - **OAuth2 Credentials**: If you plan to use the Flat API **on the behalf of mutliple users** or make this app public, request OAuth2 Credentials.  <!-- ReDoc-Inject: <security-definitions> -->  ### OAuth2 Authorization page  The Authorization page (`https://flat.io/auth/oauth`) supports all the standard parameters from the **Authorization Code** flow ([RFC6749/4.1.1](https://tools.ietf.org/html/rfc6749#section-4.1.1)) and the **Implicit** flow ([RFC6749/4.2.1](https://tools.ietf.org/html/rfc6749#section-4.2.1)). Here is a summary of the parameters available, including non-standard and optional parameters. All of them can be passed as query string when redirecting the end-user to the authorization page.  Property name  | Required | Values and Description ---------------|----------|----------------------- `client_id`    | Required | The client id (aka key) from the couple key/secret provided by Flat `response_type`| Required | We support `code` (**Authorization Code** flow, [RFC6749/4.1.1](https://tools.ietf.org/html/rfc6749#section-4.1.1)) and `token`, [RFC6749/4.2.1](https://tools.ietf.org/html/rfc6749#section-4.2.1)). It is strongly advised to use the Authorization Code flow for any server-side usage and the Implicit flow for any client-side (e.g. JavaScript) usage. `scope`        | Required | You must provide a list of scopes listed above and granted for your app, separated with a space. `redirect_uri` | Required | Determines where the response is sent. The value of this parameter must exactly match the value specified in your App Credentials settings. `state`        | Optional | An opaque string that is round-tripped in the protocol; that is to say, it is returned as a URI parameter in the Basic flow, and in the URI #fragment in the Implicit flow. `access_type`  | Optional, only available for the Authorization Code flow | The acceptable values are `online` and `offline`. When specifying `offline`, the API will return a refresh token during the access token exchange.  ### OAuth2 tokens revocation  This OAuth2 API supports token revocation ([RFC 7009](http://tools.ietf.org/html/rfc7009)) at the following endpoint: `https://api.flat.io/oauth/invalidate_token`.  # CORS This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/). And that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.  # Rate Limiting For authenticated requests, you can make up to 5,000 requests per hour. For unauthenticated requests, the rate limit allows you to make up to 500 requests per hour. Unauthenticated requests are associated with your IP address, and not the user or app making requests. You can contact us if you need [extra quota](https://flat.io/developers). To protect our quality of service, additional rate limits may apply to some API calls or actions.  You can check the returned HTTP headers of any API request to see your current rate limit status: ```bash curl -i https://api.flat.io/v2/me HTTP/1.1 200 OK Date: Sat, 25 Mar 2017 17:06:20 GMT X-RateLimit-Limit: 5000 X-RateLimit-Remaining: 4999 X-RateLimit-Reset: 1490465178 ```  The headers tell you everything you need to know about your current rate limit status:  Header name | Description ------------|------------ `X-RateLimit-Limit` | The maximum number of requests that the consumer is permitted to make per hour. `X-RateLimit-Remaining` | The number of requests remaining in the current rate limit window. This value can be negative if you try to go over the allowed quota. `X-RateLimit-Reset` | The time at which the current rate limit window resets in [UTC epoch seconds](http://en.wikipedia.org/wiki/Unix_time).  If you need the time in a different format, any modern programming language can get the job done. For example, if you open up the console on your web browser, you can easily get the reset time as a JavaScript Date object.  ```javascript new Date(1490465178 * 1000).toString() 'Sat Mar 25 2017 19:06:18 GMT+0100 (CET)' ```  Once you go over the rate limit you will receive an error response: ```bash curl -i https://api.flat.io/v2/me HTTP/1.1 403 Forbidden X-RateLimit-Limit: 5000 X-RateLimit-Remaining: 0 X-RateLimit-Reset: 1490465829  {   \"message\": \"API rate limit exceeded for xx.xxx.xxx.xx\",   \"code\": \"API_RATE_LIMIT_EXCEEDED\" } ``` 

    OpenAPI spec version: 2.0.0
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
    def __init__(self, id=None, username=None, name=None, printable_name=None, picture=None, is_power_user=None, organization=None, organization_role=None, class_role=None, html_url=None, bio=None, registration_date=None, liked_scores_count=None, followers_count=None, following_count=None, owned_public_scores_count=None, type=None, private_profile=None, locale=None):
        """
        UserDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
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
            'type': 'str',
            'private_profile': 'bool',
            'locale': 'FlatLocales'
        }

        self.attribute_map = {
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
            'type': 'type',
            'private_profile': 'privateProfile',
            'locale': 'locale'
        }

        self._id = id
        self._username = username
        self._name = name
        self._printable_name = printable_name
        self._picture = picture
        self._is_power_user = is_power_user
        self._organization = organization
        self._organization_role = organization_role
        self._class_role = class_role
        self._html_url = html_url
        self._bio = bio
        self._registration_date = registration_date
        self._liked_scores_count = liked_scores_count
        self._followers_count = followers_count
        self._following_count = following_count
        self._owned_public_scores_count = owned_public_scores_count
        self._type = type
        self._private_profile = private_profile
        self._locale = locale

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
        Number of public score the user have

        :return: The owned_public_scores_count of this UserDetails.
        :rtype: int
        """
        return self._owned_public_scores_count

    @owned_public_scores_count.setter
    def owned_public_scores_count(self, owned_public_scores_count):
        """
        Sets the owned_public_scores_count of this UserDetails.
        Number of public score the user have

        :param owned_public_scores_count: The owned_public_scores_count of this UserDetails.
        :type: int
        """

        self._owned_public_scores_count = owned_public_scores_count

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
