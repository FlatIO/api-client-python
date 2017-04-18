# coding: utf-8

"""
    Flat API

    # Introduction The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:     - Creating and importing new music scores using MusicXML or MIDI files    - Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI)    - Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  # Beta Please note that this public API is currently in beta and subject to change.  Our whole platform and apps are based on this API, however not all the endpoints are available publicly yet. Feel free to [contact us](mailto:developers@flat.io) if you have any questions, feedback or features requests.  We don't offer any guarantees during this beta period. By using this API, you agree to update your app in a timely fashion in response to any beta-period changes that are rolled out.  By using this API, and especially on the behalf of a user account, you must accept, respect and enforce our [Terms of Service and Privacy Policy](https://flat.io/legal).  # SDKs  Our team maintains the following SDKs:   - [Python](https://github.com/FlatIO/api-client-python)   - [JavaScript (Node.js and Browser)](https://github.com/FlatIO/api-client-js)   - [PHP](https://github.com/FlatIO/api-client-php)  # Authentication The Flat API supports OAuth2, you can request API credentials [on our website](https://flat.io/developers). We provide two types of credentials:    - **Account Access Tokens**: Simple access tokens that allow to try and use this API **with your own account**. This is a great solution to create private apps.   - **OAuth2 Credentials**: If you plan to use the Flat API **on the behalf of mutliple users** or make this app public, request OAuth2 Credentials.  <!-- ReDoc-Inject: <security-definitions> -->  ### OAuth2 Authorization page  The Authorization page (`https://flat.io/auth/oauth`) supports all the standard parameters from the **Authorization Code** flow ([RFC6749/4.1.1](https://tools.ietf.org/html/rfc6749#section-4.1.1)) and the **Implicit** flow ([RFC6749/4.2.1](https://tools.ietf.org/html/rfc6749#section-4.2.1)). Here is a summary of the parameters available, including non-standard and optional parameters. All of them can be passed as query string when redirecting the end-user to the authorization page.  Property name  | Required | Values and Description ---------------|----------|----------------------- `client_id`    | Required | The client id (aka key) from the couple key/secret provided by Flat `response_type`| Required | We support `code` (**Authorization Code** flow, [RFC6749/4.1.1](https://tools.ietf.org/html/rfc6749#section-4.1.1)) and `token`, [RFC6749/4.2.1](https://tools.ietf.org/html/rfc6749#section-4.2.1)). It is strongly advised to use the Authorization Code flow for any server-side usage and the Implicit flow for any client-side (e.g. JavaScript) usage. `scope`        | Required | You must provide a list of scopes listed above and granted for your app, separated with a space. `redirect_uri` | Required | Determines where the response is sent. The value of this parameter must exactly match the value specified in your App Credentials settings. `state`        | Optional | An opaque string that is round-tripped in the protocol; that is to say, it is returned as a URI parameter in the Basic flow, and in the URI #fragment in the Implicit flow. `access_type`  | Optional, only available for the Authorization Code flow | The acceptable values are `online` and `offline`. When specifying `offline`, the API will return a refresh token during the access token exchange.  ### OAuth2 tokens revocation  This OAuth2 API supports token revocation ([RFC 7009](http://tools.ietf.org/html/rfc7009)) at the following endpoint: `https://api.flat.io/oauth/invalidate_token`.  # CORS This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/). And that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.  # Rate Limiting For authenticated requests, you can make up to 5,000 requests per hour. For unauthenticated requests, the rate limit allows you to make up to 500 requests per hour. Unauthenticated requests are associated with your IP address, and not the user or app making requests. You can contact us if you need [extra quota](https://flat.io/developers). To protect our quality of service, additional rate limits may apply to some API calls or actions.  You can check the returned HTTP headers of any API request to see your current rate limit status: ```bash curl -i https://api.flat.io/v2/me HTTP/1.1 200 OK Date: Sat, 25 Mar 2017 17:06:20 GMT X-RateLimit-Limit: 5000 X-RateLimit-Remaining: 4999 X-RateLimit-Reset: 1490465178 ```  The headers tell you everything you need to know about your current rate limit status:  Header name | Description ------------|------------ `X-RateLimit-Limit` | The maximum number of requests that the consumer is permitted to make per hour. `X-RateLimit-Remaining` | The number of requests remaining in the current rate limit window. This value can be negative if you try to go over the allowed quota. `X-RateLimit-Reset` | The time at which the current rate limit window resets in [UTC epoch seconds](http://en.wikipedia.org/wiki/Unix_time).  If you need the time in a different format, any modern programming language can get the job done. For example, if you open up the console on your web browser, you can easily get the reset time as a JavaScript Date object.  ```javascript new Date(1490465178 * 1000).toString() 'Sat Mar 25 2017 19:06:18 GMT+0100 (CET)' ```  Once you go over the rate limit you will receive an error response: ```bash curl -i https://api.flat.io/v2/me HTTP/1.1 403 Forbidden X-RateLimit-Limit: 5000 X-RateLimit-Remaining: 0 X-RateLimit-Reset: 1490465829  {   \"message\": \"API rate limit exceeded for xx.xxx.xxx.xx\",   \"code\": \"API_RATE_LIMIT_EXCEEDED\" } ``` 

    OpenAPI spec version: 2.0.0
    Contact: developers@flat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ScoreApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_score_collaborator(self, score, body, **kwargs):
        """
        Add a new collaborator
        Share a score with a single user or a group. This API call allows to add, invite and update the collaborators of a document. - To add an existing Flat user to the document, specify its unique identifier in the `user` property. - To invite an external user to the document, specify its email in the `userEmail` property. - To add a Flat group to the document, specify its unique identifier in the `group` property. - To update an existing collaborator, process the same request with different rights. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_score_collaborator(score, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreCollaboratorCreation body: (required)
        :return: ScoreCollaborator
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_score_collaborator_with_http_info(score, body, **kwargs)
        else:
            (data) = self.add_score_collaborator_with_http_info(score, body, **kwargs)
            return data

    def add_score_collaborator_with_http_info(self, score, body, **kwargs):
        """
        Add a new collaborator
        Share a score with a single user or a group. This API call allows to add, invite and update the collaborators of a document. - To add an existing Flat user to the document, specify its unique identifier in the `user` property. - To invite an external user to the document, specify its email in the `userEmail` property. - To add a Flat group to the document, specify its unique identifier in the `group` property. - To update an existing collaborator, process the same request with different rights. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_score_collaborator_with_http_info(score, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreCollaboratorCreation body: (required)
        :return: ScoreCollaborator
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_score_collaborator" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `add_score_collaborator`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_score_collaborator`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/collaborators', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreCollaborator',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_score(self, body, **kwargs):
        """
        Create a new score
        Use this API method to **create a new music score in the current User account**. You will need a MusicXML 3 (`vnd.recordare.musicxml` or `vnd.recordare.musicxml+xml`) or a MIDI (`audio/midi`) file to create the new Flat document.  This API call will automatically create the first revision of the document, the score can be modified by the using our web application or by uploading a new revision of this file (`POST /v2/scores/{score}/revisions/{revision}`).  The currently authenticated user will be granted owner of the file and will be able to add other collaborators (users and groups). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_score(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ScoreCreation body: (required)
        :return: ScoreDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_score_with_http_info(body, **kwargs)
        else:
            (data) = self.create_score_with_http_info(body, **kwargs)
            return data

    def create_score_with_http_info(self, body, **kwargs):
        """
        Create a new score
        Use this API method to **create a new music score in the current User account**. You will need a MusicXML 3 (`vnd.recordare.musicxml` or `vnd.recordare.musicxml+xml`) or a MIDI (`audio/midi`) file to create the new Flat document.  This API call will automatically create the first revision of the document, the score can be modified by the using our web application or by uploading a new revision of this file (`POST /v2/scores/{score}/revisions/{revision}`).  The currently authenticated user will be granted owner of the file and will be able to add other collaborators (users and groups). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_score_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ScoreCreation body: (required)
        :return: ScoreDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_score`")


        collection_formats = {}

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreDetails',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_score_revision(self, score, body, **kwargs):
        """
        Create a new revision
        Update a score by uploading a new revision for this one. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_score_revision(score, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreRevisionCreation body: (required)
        :return: ScoreRevision
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_score_revision_with_http_info(score, body, **kwargs)
        else:
            (data) = self.create_score_revision_with_http_info(score, body, **kwargs)
            return data

    def create_score_revision_with_http_info(self, score, body, **kwargs):
        """
        Create a new revision
        Update a score by uploading a new revision for this one. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_score_revision_with_http_info(score, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreRevisionCreation body: (required)
        :return: ScoreRevision
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_score_revision" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `create_score_revision`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_score_revision`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/revisions', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreRevision',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_score(self, score, **kwargs):
        """
        Delete a score
        This API call will schedule the deletion of the score, its revisions, and whole history. The user calling this API method must have the `aclAdmin` rights on this document to process this action. The score won't be accessible anymore after calling this method and the user's quota will directly be updated. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_score(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_score_with_http_info(score, **kwargs)
        else:
            (data) = self.delete_score_with_http_info(score, **kwargs)
            return data

    def delete_score_with_http_info(self, score, **kwargs):
        """
        Delete a score
        This API call will schedule the deletion of the score, its revisions, and whole history. The user calling this API method must have the `aclAdmin` rights on this document to process this action. The score won't be accessible anymore after calling this method and the user's quota will directly be updated. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_score_with_http_info(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `delete_score`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_score_comment(self, score, comment, **kwargs):
        """
        Delete a comment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_score_comment(score, comment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str comment: Unique identifier of a sheet music comment  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_score_comment_with_http_info(score, comment, **kwargs)
        else:
            (data) = self.delete_score_comment_with_http_info(score, comment, **kwargs)
            return data

    def delete_score_comment_with_http_info(self, score, comment, **kwargs):
        """
        Delete a comment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_score_comment_with_http_info(score, comment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str comment: Unique identifier of a sheet music comment  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'comment', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_score_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `delete_score_comment`")
        # verify the required parameter 'comment' is set
        if ('comment' not in params) or (params['comment'] is None):
            raise ValueError("Missing the required parameter `comment` when calling `delete_score_comment`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']
        if 'comment' in params:
            path_params['comment'] = params['comment']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/comments/{comment}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def edit_score(self, score, **kwargs):
        """
        Edit a score's metadata
        This API method allows you to change the metadata of a score document (e.g. its `title` or `privacy`), all the properties are optional.  To edit the file itself, create a new revision using the appropriate method (`POST /v2/scores/{score}/revisions/{revision}`). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.edit_score(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreModification body:
        :return: ScoreDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.edit_score_with_http_info(score, **kwargs)
        else:
            (data) = self.edit_score_with_http_info(score, **kwargs)
            return data

    def edit_score_with_http_info(self, score, **kwargs):
        """
        Edit a score's metadata
        This API method allows you to change the metadata of a score document (e.g. its `title` or `privacy`), all the properties are optional.  To edit the file itself, create a new revision using the appropriate method (`POST /v2/scores/{score}/revisions/{revision}`). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.edit_score_with_http_info(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreModification body:
        :return: ScoreDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `edit_score`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreDetails',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def fork_score(self, score, body, **kwargs):
        """
        Fork a score
        This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to `private`.  When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fork_score(score, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreFork body: (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.fork_score_with_http_info(score, body, **kwargs)
        else:
            (data) = self.fork_score_with_http_info(score, body, **kwargs)
            return data

    def fork_score_with_http_info(self, score, body, **kwargs):
        """
        Fork a score
        This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to `private`.  When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fork_score_with_http_info(score, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreFork body: (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'body', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fork_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `fork_score`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `fork_score`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/fork', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreDetails',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def ger_user_likes(self, user, **kwargs):
        """
        List liked scores
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.ger_user_likes(user, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user: Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user.  (required)
        :param bool ids: Return only the identifiers of the scores
        :return: list[ScoreDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.ger_user_likes_with_http_info(user, **kwargs)
        else:
            (data) = self.ger_user_likes_with_http_info(user, **kwargs)
            return data

    def ger_user_likes_with_http_info(self, user, **kwargs):
        """
        List liked scores
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.ger_user_likes_with_http_info(user, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user: Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user.  (required)
        :param bool ids: Return only the identifiers of the scores
        :return: list[ScoreDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user', 'ids']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ger_user_likes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in params) or (params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `ger_user_likes`")


        collection_formats = {}

        path_params = {}
        if 'user' in params:
            path_params['user'] = params['user']

        query_params = {}
        if 'ids' in params:
            query_params['ids'] = params['ids']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/users/{user}/likes', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ScoreDetails]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_group_scores(self, group, **kwargs):
        """
        List group's scores
        Get the list of scores shared with a group. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_group_scores(group, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group: Unique identifier of the group (required)
        :param str parent: Filter the score forked from the score id `parent`
        :return: list[ScoreDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_group_scores_with_http_info(group, **kwargs)
        else:
            (data) = self.get_group_scores_with_http_info(group, **kwargs)
            return data

    def get_group_scores_with_http_info(self, group, **kwargs):
        """
        List group's scores
        Get the list of scores shared with a group. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_group_scores_with_http_info(group, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group: Unique identifier of the group (required)
        :param str parent: Filter the score forked from the score id `parent`
        :return: list[ScoreDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group', 'parent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_scores" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group' is set
        if ('group' not in params) or (params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `get_group_scores`")


        collection_formats = {}

        path_params = {}
        if 'group' in params:
            path_params['group'] = params['group']

        query_params = {}
        if 'parent' in params:
            query_params['parent'] = params['parent']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/groups/{group}/scores', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ScoreDetails]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_score(self, score, **kwargs):
        """
        Get a score's metadata
        Get the details of a score identified by the `score` parameter in the URL. The currently authenticated user must have at least a read access to the document to use this API call. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_score_with_http_info(score, **kwargs)
        else:
            (data) = self.get_score_with_http_info(score, **kwargs)
            return data

    def get_score_with_http_info(self, score, **kwargs):
        """
        Get a score's metadata
        Get the details of a score identified by the `score` parameter in the URL. The currently authenticated user must have at least a read access to the document to use this API call. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_with_http_info(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `get_score`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreDetails',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_score_collaborator(self, score, collaborator, **kwargs):
        """
        Get a collaborator
        Get the information about a collaborator (User or Group). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_collaborator(score, collaborator, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str collaborator: Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreCollaborator
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_score_collaborator_with_http_info(score, collaborator, **kwargs)
        else:
            (data) = self.get_score_collaborator_with_http_info(score, collaborator, **kwargs)
            return data

    def get_score_collaborator_with_http_info(self, score, collaborator, **kwargs):
        """
        Get a collaborator
        Get the information about a collaborator (User or Group). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_collaborator_with_http_info(score, collaborator, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str collaborator: Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreCollaborator
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'collaborator', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_score_collaborator" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `get_score_collaborator`")
        # verify the required parameter 'collaborator' is set
        if ('collaborator' not in params) or (params['collaborator'] is None):
            raise ValueError("Missing the required parameter `collaborator` when calling `get_score_collaborator`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']
        if 'collaborator' in params:
            path_params['collaborator'] = params['collaborator']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/collaborators/{collaborator}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreCollaborator',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_score_collaborators(self, score, **kwargs):
        """
        List the collaborators
        This API call will list the different collaborators of a score and their rights on the document. The returned list will at least contain the owner of the document.  Collaborators can be a single user (the object `user` will be populated) or a group (the object `group` will be populated). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_collaborators(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: list[ScoreCollaborator]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_score_collaborators_with_http_info(score, **kwargs)
        else:
            (data) = self.get_score_collaborators_with_http_info(score, **kwargs)
            return data

    def get_score_collaborators_with_http_info(self, score, **kwargs):
        """
        List the collaborators
        This API call will list the different collaborators of a score and their rights on the document. The returned list will at least contain the owner of the document.  Collaborators can be a single user (the object `user` will be populated) or a group (the object `group` will be populated). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_collaborators_with_http_info(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: list[ScoreCollaborator]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_score_collaborators" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `get_score_collaborators`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/collaborators', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ScoreCollaborator]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_score_comments(self, score, **kwargs):
        """
        List comments
        This method lists the different comments added on a music score (documents and inline) sorted by their post dates.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_comments(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: list[ScoreComment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_score_comments_with_http_info(score, **kwargs)
        else:
            (data) = self.get_score_comments_with_http_info(score, **kwargs)
            return data

    def get_score_comments_with_http_info(self, score, **kwargs):
        """
        List comments
        This method lists the different comments added on a music score (documents and inline) sorted by their post dates.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_comments_with_http_info(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: list[ScoreComment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_score_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `get_score_comments`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/comments', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ScoreComment]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_score_revision(self, score, revision, **kwargs):
        """
        Get a score revision
        When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to get a specific revision metadata. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_revision(score, revision, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str revision: Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created.  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreRevision
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_score_revision_with_http_info(score, revision, **kwargs)
        else:
            (data) = self.get_score_revision_with_http_info(score, revision, **kwargs)
            return data

    def get_score_revision_with_http_info(self, score, revision, **kwargs):
        """
        Get a score revision
        When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to get a specific revision metadata. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_revision_with_http_info(score, revision, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str revision: Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created.  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreRevision
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'revision', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_score_revision" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `get_score_revision`")
        # verify the required parameter 'revision' is set
        if ('revision' not in params) or (params['revision'] is None):
            raise ValueError("Missing the required parameter `revision` when calling `get_score_revision`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']
        if 'revision' in params:
            path_params['revision'] = params['revision']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/scores/{score}/revisions/{revision}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreRevision',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_score_revision_data(self, score, revision, format, **kwargs):
        """
        Get a score revision data
        Retrieve the file corresponding to a score revision (the following formats are available: Flat JSON/Adagio JSON `json`, MusicXML `mxl`/`xml`, MP3 `mp3`, WAV `wav`, MIDI `midi`, or a tumbnail of the first page `thumbnail.png`). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_revision_data(score, revision, format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str revision: Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created.  (required)
        :param str format: The format of the file you will retrieve (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :param bool only_cached: Only return files already generated and cached in Flat's production cache. If the file is not availabe, a 404 will be returned 
        :param str parts: An optional a set of parts to be exported. This parameter must be specified with a list of integers. For example \"1,2,5\". 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_score_revision_data_with_http_info(score, revision, format, **kwargs)
        else:
            (data) = self.get_score_revision_data_with_http_info(score, revision, format, **kwargs)
            return data

    def get_score_revision_data_with_http_info(self, score, revision, format, **kwargs):
        """
        Get a score revision data
        Retrieve the file corresponding to a score revision (the following formats are available: Flat JSON/Adagio JSON `json`, MusicXML `mxl`/`xml`, MP3 `mp3`, WAV `wav`, MIDI `midi`, or a tumbnail of the first page `thumbnail.png`). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_revision_data_with_http_info(score, revision, format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str revision: Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created.  (required)
        :param str format: The format of the file you will retrieve (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :param bool only_cached: Only return files already generated and cached in Flat's production cache. If the file is not availabe, a 404 will be returned 
        :param str parts: An optional a set of parts to be exported. This parameter must be specified with a list of integers. For example \"1,2,5\". 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'revision', 'format', 'sharing_key', 'only_cached', 'parts']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_score_revision_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `get_score_revision_data`")
        # verify the required parameter 'revision' is set
        if ('revision' not in params) or (params['revision'] is None):
            raise ValueError("Missing the required parameter `revision` when calling `get_score_revision_data`")
        # verify the required parameter 'format' is set
        if ('format' not in params) or (params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `get_score_revision_data`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']
        if 'revision' in params:
            path_params['revision'] = params['revision']
        if 'format' in params:
            path_params['format'] = params['format']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']
        if 'only_cached' in params:
            query_params['onlyCached'] = params['only_cached']
        if 'parts' in params:
            query_params['parts'] = params['parts']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/vnd.recordare.musicxml+xml', 'application/vnd.recordare.musicxml', 'audio/mp3', 'audio/wav', 'audio/midi', 'image/png'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/scores/{score}/revisions/{revision}/{format}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_score_revisions(self, score, **kwargs):
        """
        List the revisions
        When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to list all of them, sorted by last modification.  Depending the plan of the account, this list can be trunked to the few last revisions. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_revisions(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: list[ScoreRevision]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_score_revisions_with_http_info(score, **kwargs)
        else:
            (data) = self.get_score_revisions_with_http_info(score, **kwargs)
            return data

    def get_score_revisions_with_http_info(self, score, **kwargs):
        """
        List the revisions
        When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to list all of them, sorted by last modification.  Depending the plan of the account, this list can be trunked to the few last revisions. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_score_revisions_with_http_info(score, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: list[ScoreRevision]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_score_revisions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `get_score_revisions`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/revisions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ScoreRevision]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_user_scores(self, user, **kwargs):
        """
        List user's scores
        Get the list of scores owned by the User 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_scores(user, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user: Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user.  (required)
        :param str parent: Filter the score forked from the score id `parent`
        :return: list[ScoreDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_scores_with_http_info(user, **kwargs)
        else:
            (data) = self.get_user_scores_with_http_info(user, **kwargs)
            return data

    def get_user_scores_with_http_info(self, user, **kwargs):
        """
        List user's scores
        Get the list of scores owned by the User 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_scores_with_http_info(user, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user: Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user.  (required)
        :param str parent: Filter the score forked from the score id `parent`
        :return: list[ScoreDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user', 'parent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_scores" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in params) or (params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `get_user_scores`")


        collection_formats = {}

        path_params = {}
        if 'user' in params:
            path_params['user'] = params['user']

        query_params = {}
        if 'parent' in params:
            query_params['parent'] = params['parent']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/users/{user}/scores', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ScoreDetails]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def mark_score_comment_resolved(self, score, comment, **kwargs):
        """
        Mark the comment as resolved
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_score_comment_resolved(score, comment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str comment: Unique identifier of a sheet music comment  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.mark_score_comment_resolved_with_http_info(score, comment, **kwargs)
        else:
            (data) = self.mark_score_comment_resolved_with_http_info(score, comment, **kwargs)
            return data

    def mark_score_comment_resolved_with_http_info(self, score, comment, **kwargs):
        """
        Mark the comment as resolved
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_score_comment_resolved_with_http_info(score, comment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str comment: Unique identifier of a sheet music comment  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'comment', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mark_score_comment_resolved" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `mark_score_comment_resolved`")
        # verify the required parameter 'comment' is set
        if ('comment' not in params) or (params['comment'] is None):
            raise ValueError("Missing the required parameter `comment` when calling `mark_score_comment_resolved`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']
        if 'comment' in params:
            path_params['comment'] = params['comment']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/comments/{comment}/resolved', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def mark_score_comment_unresolved(self, score, comment, **kwargs):
        """
        Mark the comment as unresolved
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_score_comment_unresolved(score, comment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str comment: Unique identifier of a sheet music comment  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.mark_score_comment_unresolved_with_http_info(score, comment, **kwargs)
        else:
            (data) = self.mark_score_comment_unresolved_with_http_info(score, comment, **kwargs)
            return data

    def mark_score_comment_unresolved_with_http_info(self, score, comment, **kwargs):
        """
        Mark the comment as unresolved
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_score_comment_unresolved_with_http_info(score, comment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str comment: Unique identifier of a sheet music comment  (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'comment', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mark_score_comment_unresolved" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `mark_score_comment_unresolved`")
        # verify the required parameter 'comment' is set
        if ('comment' not in params) or (params['comment'] is None):
            raise ValueError("Missing the required parameter `comment` when calling `mark_score_comment_unresolved`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']
        if 'comment' in params:
            path_params['comment'] = params['comment']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/comments/{comment}/resolved', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_score_comment(self, score, body, **kwargs):
        """
        Post a new comment
        Post a document or a contextualized comment on a document.  Please note that this method includes an anti-spam system for public scores. We don't guarantee that your comments will be accepted and displayed to end-user. Comments are be blocked by returning a `403` HTTP error and hidden from other users when the `spam` property is `true`. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_score_comment(score, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreCommentCreation body: (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreComment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_score_comment_with_http_info(score, body, **kwargs)
        else:
            (data) = self.post_score_comment_with_http_info(score, body, **kwargs)
            return data

    def post_score_comment_with_http_info(self, score, body, **kwargs):
        """
        Post a new comment
        Post a document or a contextualized comment on a document.  Please note that this method includes an anti-spam system for public scores. We don't guarantee that your comments will be accepted and displayed to end-user. Comments are be blocked by returning a `403` HTTP error and hidden from other users when the `spam` property is `true`. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_score_comment_with_http_info(score, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param ScoreCommentCreation body: (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreComment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'body', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_score_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `post_score_comment`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_score_comment`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/comments', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreComment',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def remove_score_collaborator(self, score, collaborator, **kwargs):
        """
        Delete a collaborator
        Remove the specified collaborator from the score 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_score_collaborator(score, collaborator, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str collaborator: Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_score_collaborator_with_http_info(score, collaborator, **kwargs)
        else:
            (data) = self.remove_score_collaborator_with_http_info(score, collaborator, **kwargs)
            return data

    def remove_score_collaborator_with_http_info(self, score, collaborator, **kwargs):
        """
        Delete a collaborator
        Remove the specified collaborator from the score 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_score_collaborator_with_http_info(score, collaborator, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str collaborator: Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'collaborator']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_score_collaborator" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `remove_score_collaborator`")
        # verify the required parameter 'collaborator' is set
        if ('collaborator' not in params) or (params['collaborator'] is None):
            raise ValueError("Missing the required parameter `collaborator` when calling `remove_score_collaborator`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']
        if 'collaborator' in params:
            path_params['collaborator'] = params['collaborator']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/collaborators/{collaborator}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_score_comment(self, score, comment, body, **kwargs):
        """
        Update an existing comment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_score_comment(score, comment, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str comment: Unique identifier of a sheet music comment  (required)
        :param ScoreCommentUpdate body: (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreComment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_score_comment_with_http_info(score, comment, body, **kwargs)
        else:
            (data) = self.update_score_comment_with_http_info(score, comment, body, **kwargs)
            return data

    def update_score_comment_with_http_info(self, score, comment, body, **kwargs):
        """
        Update an existing comment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_score_comment_with_http_info(score, comment, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`).  (required)
        :param str comment: Unique identifier of a sheet music comment  (required)
        :param ScoreCommentUpdate body: (required)
        :param str sharing_key: This sharing key must be specified to access to a score with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
        :return: ScoreComment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['score', 'comment', 'body', 'sharing_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_score_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'score' is set
        if ('score' not in params) or (params['score'] is None):
            raise ValueError("Missing the required parameter `score` when calling `update_score_comment`")
        # verify the required parameter 'comment' is set
        if ('comment' not in params) or (params['comment'] is None):
            raise ValueError("Missing the required parameter `comment` when calling `update_score_comment`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_score_comment`")


        collection_formats = {}

        path_params = {}
        if 'score' in params:
            path_params['score'] = params['score']
        if 'comment' in params:
            path_params['comment'] = params['comment']

        query_params = {}
        if 'sharing_key' in params:
            query_params['sharingKey'] = params['sharing_key']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/scores/{score}/comments/{comment}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ScoreComment',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
