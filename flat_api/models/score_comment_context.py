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


class ScoreCommentContext(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, part_uuid=None, staff_idx=None, measure_uuids=None, start_time_pos=None, stop_time_pos=None, start_dpq=None, stop_dpq=None):
        """
        ScoreCommentContext - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'part_uuid': 'str',
            'staff_idx': 'float',
            'measure_uuids': 'list[str]',
            'start_time_pos': 'float',
            'stop_time_pos': 'float',
            'start_dpq': 'float',
            'stop_dpq': 'float'
        }

        self.attribute_map = {
            'part_uuid': 'partUuid',
            'staff_idx': 'staffIdx',
            'measure_uuids': 'measureUuids',
            'start_time_pos': 'startTimePos',
            'stop_time_pos': 'stopTimePos',
            'start_dpq': 'startDpq',
            'stop_dpq': 'stopDpq'
        }

        self._part_uuid = part_uuid
        self._staff_idx = staff_idx
        self._measure_uuids = measure_uuids
        self._start_time_pos = start_time_pos
        self._stop_time_pos = stop_time_pos
        self._start_dpq = start_dpq
        self._stop_dpq = stop_dpq

    @property
    def part_uuid(self):
        """
        Gets the part_uuid of this ScoreCommentContext.
        The unique identifier (UUID) of the score part

        :return: The part_uuid of this ScoreCommentContext.
        :rtype: str
        """
        return self._part_uuid

    @part_uuid.setter
    def part_uuid(self, part_uuid):
        """
        Sets the part_uuid of this ScoreCommentContext.
        The unique identifier (UUID) of the score part

        :param part_uuid: The part_uuid of this ScoreCommentContext.
        :type: str
        """
        if part_uuid is None:
            raise ValueError("Invalid value for `part_uuid`, must not be `None`")

        self._part_uuid = part_uuid

    @property
    def staff_idx(self):
        """
        Gets the staff_idx of this ScoreCommentContext.
        The identififer of the staff

        :return: The staff_idx of this ScoreCommentContext.
        :rtype: float
        """
        return self._staff_idx

    @staff_idx.setter
    def staff_idx(self, staff_idx):
        """
        Sets the staff_idx of this ScoreCommentContext.
        The identififer of the staff

        :param staff_idx: The staff_idx of this ScoreCommentContext.
        :type: float
        """
        if staff_idx is None:
            raise ValueError("Invalid value for `staff_idx`, must not be `None`")

        self._staff_idx = staff_idx

    @property
    def measure_uuids(self):
        """
        Gets the measure_uuids of this ScoreCommentContext.
        The list of measure UUIds

        :return: The measure_uuids of this ScoreCommentContext.
        :rtype: list[str]
        """
        return self._measure_uuids

    @measure_uuids.setter
    def measure_uuids(self, measure_uuids):
        """
        Sets the measure_uuids of this ScoreCommentContext.
        The list of measure UUIds

        :param measure_uuids: The measure_uuids of this ScoreCommentContext.
        :type: list[str]
        """
        if measure_uuids is None:
            raise ValueError("Invalid value for `measure_uuids`, must not be `None`")

        self._measure_uuids = measure_uuids

    @property
    def start_time_pos(self):
        """
        Gets the start_time_pos of this ScoreCommentContext.

        :return: The start_time_pos of this ScoreCommentContext.
        :rtype: float
        """
        return self._start_time_pos

    @start_time_pos.setter
    def start_time_pos(self, start_time_pos):
        """
        Sets the start_time_pos of this ScoreCommentContext.

        :param start_time_pos: The start_time_pos of this ScoreCommentContext.
        :type: float
        """
        if start_time_pos is None:
            raise ValueError("Invalid value for `start_time_pos`, must not be `None`")

        self._start_time_pos = start_time_pos

    @property
    def stop_time_pos(self):
        """
        Gets the stop_time_pos of this ScoreCommentContext.

        :return: The stop_time_pos of this ScoreCommentContext.
        :rtype: float
        """
        return self._stop_time_pos

    @stop_time_pos.setter
    def stop_time_pos(self, stop_time_pos):
        """
        Sets the stop_time_pos of this ScoreCommentContext.

        :param stop_time_pos: The stop_time_pos of this ScoreCommentContext.
        :type: float
        """
        if stop_time_pos is None:
            raise ValueError("Invalid value for `stop_time_pos`, must not be `None`")

        self._stop_time_pos = stop_time_pos

    @property
    def start_dpq(self):
        """
        Gets the start_dpq of this ScoreCommentContext.

        :return: The start_dpq of this ScoreCommentContext.
        :rtype: float
        """
        return self._start_dpq

    @start_dpq.setter
    def start_dpq(self, start_dpq):
        """
        Sets the start_dpq of this ScoreCommentContext.

        :param start_dpq: The start_dpq of this ScoreCommentContext.
        :type: float
        """
        if start_dpq is None:
            raise ValueError("Invalid value for `start_dpq`, must not be `None`")

        self._start_dpq = start_dpq

    @property
    def stop_dpq(self):
        """
        Gets the stop_dpq of this ScoreCommentContext.

        :return: The stop_dpq of this ScoreCommentContext.
        :rtype: float
        """
        return self._stop_dpq

    @stop_dpq.setter
    def stop_dpq(self, stop_dpq):
        """
        Sets the stop_dpq of this ScoreCommentContext.

        :param stop_dpq: The stop_dpq of this ScoreCommentContext.
        :type: float
        """
        if stop_dpq is None:
            raise ValueError("Invalid value for `stop_dpq`, must not be `None`")

        self._stop_dpq = stop_dpq

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
        if not isinstance(other, ScoreCommentContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
