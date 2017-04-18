# coding: utf-8

"""
    Flat API

    # Introduction The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:     - Creating and importing new music scores using MusicXML or MIDI files    - Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI)    - Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  # Beta Please note that this public API is currently in beta and subject to change.  Our whole platform and apps are based on this API, however not all the endpoints are available publicly yet. Feel free to [contact us](mailto:developers@flat.io) if you have any questions, feedback or features requests.  We don't offer any guarantees during this beta period. By using this API, you agree to update your app in a timely fashion in response to any beta-period changes that are rolled out.  By using this API, and especially on the behalf of a user account, you must accept, respect and enforce our [Terms of Service and Privacy Policy](https://flat.io/legal).  # SDKs  Our team maintains the following SDKs:   - [Python](https://github.com/FlatIO/api-client-python)   - [JavaScript (Node.js and Browser)](https://github.com/FlatIO/api-client-js)   - [PHP](https://github.com/FlatIO/api-client-php)  # Authentication The Flat API supports OAuth2, you can request API credentials [on our website](https://flat.io/developers). We provide two types of credentials:    - **Account Access Tokens**: Simple access tokens that allow to try and use this API **with your own account**. This is a great solution to create private apps.   - **OAuth2 Credentials**: If you plan to use the Flat API **on the behalf of mutliple users** or make this app public, request OAuth2 Credentials.  <!-- ReDoc-Inject: <security-definitions> -->  ### OAuth2 Authorization page  The Authorization page (`https://flat.io/auth/oauth`) supports all the standard parameters from the **Authorization Code** flow ([RFC6749/4.1.1](https://tools.ietf.org/html/rfc6749#section-4.1.1)) and the **Implicit** flow ([RFC6749/4.2.1](https://tools.ietf.org/html/rfc6749#section-4.2.1)). Here is a summary of the parameters available, including non-standard and optional parameters. All of them can be passed as query string when redirecting the end-user to the authorization page.  Property name  | Required | Values and Description ---------------|----------|----------------------- `client_id`    | Required | The client id (aka key) from the couple key/secret provided by Flat `response_type`| Required | We support `code` (**Authorization Code** flow, [RFC6749/4.1.1](https://tools.ietf.org/html/rfc6749#section-4.1.1)) and `token`, [RFC6749/4.2.1](https://tools.ietf.org/html/rfc6749#section-4.2.1)). It is strongly advised to use the Authorization Code flow for any server-side usage and the Implicit flow for any client-side (e.g. JavaScript) usage. `scope`        | Required | You must provide a list of scopes listed above and granted for your app, separated with a space. `redirect_uri` | Required | Determines where the response is sent. The value of this parameter must exactly match the value specified in your App Credentials settings. `state`        | Optional | An opaque string that is round-tripped in the protocol; that is to say, it is returned as a URI parameter in the Basic flow, and in the URI #fragment in the Implicit flow. `access_type`  | Optional, only available for the Authorization Code flow | The acceptable values are `online` and `offline`. When specifying `offline`, the API will return a refresh token during the access token exchange.  ### OAuth2 tokens revocation  This OAuth2 API supports token revocation ([RFC 7009](http://tools.ietf.org/html/rfc7009)) at the following endpoint: `https://api.flat.io/oauth/invalidate_token`.  # CORS This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/). And that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.  # Rate Limiting For authenticated requests, you can make up to 5,000 requests per hour. For unauthenticated requests, the rate limit allows you to make up to 500 requests per hour. Unauthenticated requests are associated with your IP address, and not the user or app making requests. You can contact us if you need [extra quota](https://flat.io/developers). To protect our quality of service, additional rate limits may apply to some API calls or actions.  You can check the returned HTTP headers of any API request to see your current rate limit status: ```bash curl -i https://api.flat.io/v2/me HTTP/1.1 200 OK Date: Sat, 25 Mar 2017 17:06:20 GMT X-RateLimit-Limit: 5000 X-RateLimit-Remaining: 4999 X-RateLimit-Reset: 1490465178 ```  The headers tell you everything you need to know about your current rate limit status:  Header name | Description ------------|------------ `X-RateLimit-Limit` | The maximum number of requests that the consumer is permitted to make per hour. `X-RateLimit-Remaining` | The number of requests remaining in the current rate limit window. This value can be negative if you try to go over the allowed quota. `X-RateLimit-Reset` | The time at which the current rate limit window resets in [UTC epoch seconds](http://en.wikipedia.org/wiki/Unix_time).  If you need the time in a different format, any modern programming language can get the job done. For example, if you open up the console on your web browser, you can easily get the reset time as a JavaScript Date object.  ```javascript new Date(1490465178 * 1000).toString() 'Sat Mar 25 2017 19:06:18 GMT+0100 (CET)' ```  Once you go over the rate limit you will receive an error response: ```bash curl -i https://api.flat.io/v2/me HTTP/1.1 403 Forbidden X-RateLimit-Limit: 5000 X-RateLimit-Remaining: 0 X-RateLimit-Reset: 1490465829  {   \"message\": \"API rate limit exceeded for xx.xxx.xxx.xx\",   \"code\": \"API_RATE_LIMIT_EXCEEDED\" } ``` 

    OpenAPI spec version: 2.0.0
    Contact: developers@flat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import io
import json
import ssl
import certifi
import logging
import re

# python 2 and python 3 compatibility library
from six import PY3
from six.moves.urllib.parse import urlencode

from .configuration import Configuration

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """
        Returns a dictionary of the response headers.
        """
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """
        Returns a given response header.
        """
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, pools_size=4, maxsize=4):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680
        # maxsize is the number of requests to host that are allowed in parallel
        # ca_certs vs cert_file vs key_file
        # http://stackoverflow.com/a/23957365/2985775

        # cert_reqs
        if Configuration().verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if Configuration().ssl_ca_cert:
            ca_certs = Configuration().ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        # cert_file
        cert_file = Configuration().cert_file

        # key file
        key_file = Configuration().key_file

        # proxy
        proxy = Configuration().proxy

        # https pool manager
        if proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=cert_file,
                key_file=key_file,
                proxy_url=proxy
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=cert_file,
                key_file=key_file
            )


    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True, _request_timeout=None):
        """
        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will be returned without
                                 reading/decoding response data. Default is True.
        :param _request_timeout: timeout setting for this request. If one number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, ) if PY3 else (int, long)):
                timeout = urllib3.Timeout(total=_request_timeout)
            elif isinstance(_request_timeout, tuple) and len(_request_timeout) == 2:
                timeout = urllib3.Timeout(connect=_request_timeout[0], read=_request_timeout[1])

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = None
                    if body:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(method, url,
                                                  body=request_body,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':
                    r = self.pool_manager.request(method, url,
                                                  fields=post_params,
                                                  encode_multipart=False,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct Content-Type
                    # which generated by urllib3 will be overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(method, url,
                                                  fields=post_params,
                                                  encode_multipart=True,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is provided
                # in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(method, url,
                                                  body=request_body,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided arguments.
                             Please check that your arguments match declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # In the python 3, the response.data is bytes.
            # we need to decode it to string.
            if PY3:
                r.data = r.data.decode('utf8')

            # log response body
            logger.debug("response body: %s", r.data)

        if r.status not in range(200, 206):
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None, _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
             _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
            _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
              _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """
        Custom error messages for exception
        """
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
