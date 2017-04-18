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


class ScoreComment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, type=None, user=None, score=None, revision=None, reply_to=None, date=None, modification_date=None, comment=None, raw_comment=None, context=None, mentions=None, resolved=None, resolved_by=None, spam=None):
        """
        ScoreComment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'user': 'str',
            'score': 'str',
            'revision': 'str',
            'reply_to': 'str',
            'date': 'datetime',
            'modification_date': 'datetime',
            'comment': 'str',
            'raw_comment': 'str',
            'context': 'ScoreCommentContext',
            'mentions': 'list[str]',
            'resolved': 'bool',
            'resolved_by': 'str',
            'spam': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'user': 'user',
            'score': 'score',
            'revision': 'revision',
            'reply_to': 'replyTo',
            'date': 'date',
            'modification_date': 'modificationDate',
            'comment': 'comment',
            'raw_comment': 'rawComment',
            'context': 'context',
            'mentions': 'mentions',
            'resolved': 'resolved',
            'resolved_by': 'resolvedBy',
            'spam': 'spam'
        }

        self._id = id
        self._type = type
        self._user = user
        self._score = score
        self._revision = revision
        self._reply_to = reply_to
        self._date = date
        self._modification_date = modification_date
        self._comment = comment
        self._raw_comment = raw_comment
        self._context = context
        self._mentions = mentions
        self._resolved = resolved
        self._resolved_by = resolved_by
        self._spam = spam

    @property
    def id(self):
        """
        Gets the id of this ScoreComment.
        The comment unique identifier

        :return: The id of this ScoreComment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScoreComment.
        The comment unique identifier

        :param id: The id of this ScoreComment.
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this ScoreComment.
        The type of the comment

        :return: The type of this ScoreComment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ScoreComment.
        The type of the comment

        :param type: The type of this ScoreComment.
        :type: str
        """
        allowed_values = ["document", "inline"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user(self):
        """
        Gets the user of this ScoreComment.
        The author unique identifier

        :return: The user of this ScoreComment.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this ScoreComment.
        The author unique identifier

        :param user: The user of this ScoreComment.
        :type: str
        """

        self._user = user

    @property
    def score(self):
        """
        Gets the score of this ScoreComment.
        The unique identifier of the score where the comment was posted

        :return: The score of this ScoreComment.
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this ScoreComment.
        The unique identifier of the score where the comment was posted

        :param score: The score of this ScoreComment.
        :type: str
        """

        self._score = score

    @property
    def revision(self):
        """
        Gets the revision of this ScoreComment.
        The unique identifier of revision the comment was posted

        :return: The revision of this ScoreComment.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ScoreComment.
        The unique identifier of revision the comment was posted

        :param revision: The revision of this ScoreComment.
        :type: str
        """

        self._revision = revision

    @property
    def reply_to(self):
        """
        Gets the reply_to of this ScoreComment.
        When the comment is a reply to another comment, the unique identifier of the parent comment 

        :return: The reply_to of this ScoreComment.
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """
        Sets the reply_to of this ScoreComment.
        When the comment is a reply to another comment, the unique identifier of the parent comment 

        :param reply_to: The reply_to of this ScoreComment.
        :type: str
        """

        self._reply_to = reply_to

    @property
    def date(self):
        """
        Gets the date of this ScoreComment.
        The date when the comment was posted

        :return: The date of this ScoreComment.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this ScoreComment.
        The date when the comment was posted

        :param date: The date of this ScoreComment.
        :type: datetime
        """

        self._date = date

    @property
    def modification_date(self):
        """
        Gets the modification_date of this ScoreComment.
        The date of the last comment modification

        :return: The modification_date of this ScoreComment.
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """
        Sets the modification_date of this ScoreComment.
        The date of the last comment modification

        :param modification_date: The modification_date of this ScoreComment.
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def comment(self):
        """
        Gets the comment of this ScoreComment.
        The comment text that can includes mentions using the following format: `@[id:username]`. 

        :return: The comment of this ScoreComment.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this ScoreComment.
        The comment text that can includes mentions using the following format: `@[id:username]`. 

        :param comment: The comment of this ScoreComment.
        :type: str
        """

        self._comment = comment

    @property
    def raw_comment(self):
        """
        Gets the raw_comment of this ScoreComment.
        A raw version of the comment, that can be displayed without parsing the mentions. 

        :return: The raw_comment of this ScoreComment.
        :rtype: str
        """
        return self._raw_comment

    @raw_comment.setter
    def raw_comment(self, raw_comment):
        """
        Sets the raw_comment of this ScoreComment.
        A raw version of the comment, that can be displayed without parsing the mentions. 

        :param raw_comment: The raw_comment of this ScoreComment.
        :type: str
        """

        self._raw_comment = raw_comment

    @property
    def context(self):
        """
        Gets the context of this ScoreComment.

        :return: The context of this ScoreComment.
        :rtype: ScoreCommentContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this ScoreComment.

        :param context: The context of this ScoreComment.
        :type: ScoreCommentContext
        """

        self._context = context

    @property
    def mentions(self):
        """
        Gets the mentions of this ScoreComment.
        The list of user identifier mentioned on the score

        :return: The mentions of this ScoreComment.
        :rtype: list[str]
        """
        return self._mentions

    @mentions.setter
    def mentions(self, mentions):
        """
        Sets the mentions of this ScoreComment.
        The list of user identifier mentioned on the score

        :param mentions: The mentions of this ScoreComment.
        :type: list[str]
        """

        self._mentions = mentions

    @property
    def resolved(self):
        """
        Gets the resolved of this ScoreComment.
        For inline comments, the comment can be marked as resolved and will be hidden in the future responses 

        :return: The resolved of this ScoreComment.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """
        Sets the resolved of this ScoreComment.
        For inline comments, the comment can be marked as resolved and will be hidden in the future responses 

        :param resolved: The resolved of this ScoreComment.
        :type: bool
        """

        self._resolved = resolved

    @property
    def resolved_by(self):
        """
        Gets the resolved_by of this ScoreComment.
        If the user is marked as resolved, this will contain the unique identifier of the User who marked this comment as resolved 

        :return: The resolved_by of this ScoreComment.
        :rtype: str
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        """
        Sets the resolved_by of this ScoreComment.
        If the user is marked as resolved, this will contain the unique identifier of the User who marked this comment as resolved 

        :param resolved_by: The resolved_by of this ScoreComment.
        :type: str
        """

        self._resolved_by = resolved_by

    @property
    def spam(self):
        """
        Gets the spam of this ScoreComment.
        `true  if the message has been detected as spam and hidden from other users 

        :return: The spam of this ScoreComment.
        :rtype: bool
        """
        return self._spam

    @spam.setter
    def spam(self, spam):
        """
        Sets the spam of this ScoreComment.
        `true  if the message has been detected as spam and hidden from other users 

        :param spam: The spam of this ScoreComment.
        :type: bool
        """

        self._spam = spam

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
        if not isinstance(other, ScoreComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
