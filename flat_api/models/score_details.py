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


class ScoreDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, sharing_key=None, title=None, privacy=None, user=None, html_url=None, rights=None, collaborators=None, creation_date=None, modification_date=None, organization=None, parent_score=None, instruments=None, google_drive_file_id=None, likes=None, comments=None, views=None):
        """
        ScoreDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'sharing_key': 'str',
            'title': 'str',
            'privacy': 'ScorePrivacy',
            'user': 'UserPublicSummary',
            'html_url': 'str',
            'rights': 'ScoreRights',
            'collaborators': 'list[ScoreCollaborator]',
            'creation_date': 'datetime',
            'modification_date': 'datetime',
            'organization': 'str',
            'parent_score': 'str',
            'instruments': 'list[str]',
            'google_drive_file_id': 'str',
            'likes': 'ScoreLikesCounts',
            'comments': 'ScoreCommentsCounts',
            'views': 'ScoreViewsCounts'
        }

        self.attribute_map = {
            'id': 'id',
            'sharing_key': 'sharingKey',
            'title': 'title',
            'privacy': 'privacy',
            'user': 'user',
            'html_url': 'htmlUrl',
            'rights': 'rights',
            'collaborators': 'collaborators',
            'creation_date': 'creationDate',
            'modification_date': 'modificationDate',
            'organization': 'organization',
            'parent_score': 'parentScore',
            'instruments': 'instruments',
            'google_drive_file_id': 'googleDriveFileId',
            'likes': 'likes',
            'comments': 'comments',
            'views': 'views'
        }

        self._id = id
        self._sharing_key = sharing_key
        self._title = title
        self._privacy = privacy
        self._user = user
        self._html_url = html_url
        self._rights = rights
        self._collaborators = collaborators
        self._creation_date = creation_date
        self._modification_date = modification_date
        self._organization = organization
        self._parent_score = parent_score
        self._instruments = instruments
        self._google_drive_file_id = google_drive_file_id
        self._likes = likes
        self._comments = comments
        self._views = views

    @property
    def id(self):
        """
        Gets the id of this ScoreDetails.
        The unique identifier of the score

        :return: The id of this ScoreDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScoreDetails.
        The unique identifier of the score

        :param id: The id of this ScoreDetails.
        :type: str
        """

        self._id = id

    @property
    def sharing_key(self):
        """
        Gets the sharing_key of this ScoreDetails.
        The private sharing key of the score (available when the `privacy` mode is set to `privateLink`)

        :return: The sharing_key of this ScoreDetails.
        :rtype: str
        """
        return self._sharing_key

    @sharing_key.setter
    def sharing_key(self, sharing_key):
        """
        Sets the sharing_key of this ScoreDetails.
        The private sharing key of the score (available when the `privacy` mode is set to `privateLink`)

        :param sharing_key: The sharing_key of this ScoreDetails.
        :type: str
        """

        self._sharing_key = sharing_key

    @property
    def title(self):
        """
        Gets the title of this ScoreDetails.
        The title of the score

        :return: The title of this ScoreDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ScoreDetails.
        The title of the score

        :param title: The title of this ScoreDetails.
        :type: str
        """

        self._title = title

    @property
    def privacy(self):
        """
        Gets the privacy of this ScoreDetails.

        :return: The privacy of this ScoreDetails.
        :rtype: ScorePrivacy
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """
        Sets the privacy of this ScoreDetails.

        :param privacy: The privacy of this ScoreDetails.
        :type: ScorePrivacy
        """

        self._privacy = privacy

    @property
    def user(self):
        """
        Gets the user of this ScoreDetails.

        :return: The user of this ScoreDetails.
        :rtype: UserPublicSummary
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this ScoreDetails.

        :param user: The user of this ScoreDetails.
        :type: UserPublicSummary
        """

        self._user = user

    @property
    def html_url(self):
        """
        Gets the html_url of this ScoreDetails.
        The url where the score can be viewed in a web browser

        :return: The html_url of this ScoreDetails.
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """
        Sets the html_url of this ScoreDetails.
        The url where the score can be viewed in a web browser

        :param html_url: The html_url of this ScoreDetails.
        :type: str
        """

        self._html_url = html_url

    @property
    def rights(self):
        """
        Gets the rights of this ScoreDetails.

        :return: The rights of this ScoreDetails.
        :rtype: ScoreRights
        """
        return self._rights

    @rights.setter
    def rights(self, rights):
        """
        Sets the rights of this ScoreDetails.

        :param rights: The rights of this ScoreDetails.
        :type: ScoreRights
        """

        self._rights = rights

    @property
    def collaborators(self):
        """
        Gets the collaborators of this ScoreDetails.
        The list of the collaborators of the score

        :return: The collaborators of this ScoreDetails.
        :rtype: list[ScoreCollaborator]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """
        Sets the collaborators of this ScoreDetails.
        The list of the collaborators of the score

        :param collaborators: The collaborators of this ScoreDetails.
        :type: list[ScoreCollaborator]
        """

        self._collaborators = collaborators

    @property
    def creation_date(self):
        """
        Gets the creation_date of this ScoreDetails.
        The date when the score was created

        :return: The creation_date of this ScoreDetails.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this ScoreDetails.
        The date when the score was created

        :param creation_date: The creation_date of this ScoreDetails.
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """
        Gets the modification_date of this ScoreDetails.
        The date of the last revision of the score

        :return: The modification_date of this ScoreDetails.
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """
        Sets the modification_date of this ScoreDetails.
        The date of the last revision of the score

        :param modification_date: The modification_date of this ScoreDetails.
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def organization(self):
        """
        Gets the organization of this ScoreDetails.
        If the score has been created in an organization, the identifier of this organization. This property is especially used with the score privacy `organizationPublic`. 

        :return: The organization of this ScoreDetails.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this ScoreDetails.
        If the score has been created in an organization, the identifier of this organization. This property is especially used with the score privacy `organizationPublic`. 

        :param organization: The organization of this ScoreDetails.
        :type: str
        """

        self._organization = organization

    @property
    def parent_score(self):
        """
        Gets the parent_score of this ScoreDetails.
        If the score has been forked, the unique identifier of the parent score. 

        :return: The parent_score of this ScoreDetails.
        :rtype: str
        """
        return self._parent_score

    @parent_score.setter
    def parent_score(self, parent_score):
        """
        Sets the parent_score of this ScoreDetails.
        If the score has been forked, the unique identifier of the parent score. 

        :param parent_score: The parent_score of this ScoreDetails.
        :type: str
        """

        self._parent_score = parent_score

    @property
    def instruments(self):
        """
        Gets the instruments of this ScoreDetails.
        An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat's UI or instruments icons. The format of the strings is `{instrument-group}.{instrument-id}`. 

        :return: The instruments of this ScoreDetails.
        :rtype: list[str]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """
        Sets the instruments of this ScoreDetails.
        An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat's UI or instruments icons. The format of the strings is `{instrument-group}.{instrument-id}`. 

        :param instruments: The instruments of this ScoreDetails.
        :type: list[str]
        """

        self._instruments = instruments

    @property
    def google_drive_file_id(self):
        """
        Gets the google_drive_file_id of this ScoreDetails.
        If the user uses Google Drive and the score exists on Google Drive, this field will contain the unique identifier of the Flat score on Google Drive. You can access the document using the url: `https://drive.google.com/open?id={googleDriveFileId}` 

        :return: The google_drive_file_id of this ScoreDetails.
        :rtype: str
        """
        return self._google_drive_file_id

    @google_drive_file_id.setter
    def google_drive_file_id(self, google_drive_file_id):
        """
        Sets the google_drive_file_id of this ScoreDetails.
        If the user uses Google Drive and the score exists on Google Drive, this field will contain the unique identifier of the Flat score on Google Drive. You can access the document using the url: `https://drive.google.com/open?id={googleDriveFileId}` 

        :param google_drive_file_id: The google_drive_file_id of this ScoreDetails.
        :type: str
        """

        self._google_drive_file_id = google_drive_file_id

    @property
    def likes(self):
        """
        Gets the likes of this ScoreDetails.

        :return: The likes of this ScoreDetails.
        :rtype: ScoreLikesCounts
        """
        return self._likes

    @likes.setter
    def likes(self, likes):
        """
        Sets the likes of this ScoreDetails.

        :param likes: The likes of this ScoreDetails.
        :type: ScoreLikesCounts
        """

        self._likes = likes

    @property
    def comments(self):
        """
        Gets the comments of this ScoreDetails.

        :return: The comments of this ScoreDetails.
        :rtype: ScoreCommentsCounts
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this ScoreDetails.

        :param comments: The comments of this ScoreDetails.
        :type: ScoreCommentsCounts
        """

        self._comments = comments

    @property
    def views(self):
        """
        Gets the views of this ScoreDetails.

        :return: The views of this ScoreDetails.
        :rtype: ScoreViewsCounts
        """
        return self._views

    @views.setter
    def views(self, views):
        """
        Sets the views of this ScoreDetails.

        :param views: The views of this ScoreDetails.
        :type: ScoreViewsCounts
        """

        self._views = views

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
        if not isinstance(other, ScoreDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
