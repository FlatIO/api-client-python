# flat_api.UserApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ger_user_likes**](UserApi.md#ger_user_likes) | **GET** /users/{user}/likes | List liked scores
[**get_user**](UserApi.md#get_user) | **GET** /users/{user} | Get a public user profile
[**get_user_scores**](UserApi.md#get_user_scores) | **GET** /users/{user}/scores | List user&#39;s scores


# **ger_user_likes**
> [ScoreDetails] ger_user_likes(user)

List liked scores

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import user_api
from flat_api.model.score_details import ScoreDetails
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user = "user_example" # str | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
    ids = True # bool | Return only the identifiers of the scores (optional)

    # example passing only required values which don't have defaults set
    try:
        # List liked scores
        api_response = api_instance.ger_user_likes(user)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling UserApi->ger_user_likes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List liked scores
        api_response = api_instance.ger_user_likes(user, ids=ids)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling UserApi->ger_user_likes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  |
 **ids** | **bool**| Return only the identifiers of the scores | [optional]

### Return type

[**[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of liked scores |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserPublic get_user(user)

Get a public user profile

Get a profile of a Flat or Flat for Education User. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import user_api
from flat_api.model.user_public import UserPublic
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user = "user_example" # str | This route parameter is the unique identifier of the user. You can specify an email instead of an unique identifier. If you are executing this request authenticated, you can use `me` as a value instead of the current User unique identifier to work on the current authenticated user. 

    # example passing only required values which don't have defaults set
    try:
        # Get a public user profile
        api_response = api_instance.get_user(user)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| This route parameter is the unique identifier of the user. You can specify an email instead of an unique identifier. If you are executing this request authenticated, you can use &#x60;me&#x60; as a value instead of the current User unique identifier to work on the current authenticated user.  |

### Return type

[**UserPublic**](UserPublic.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user public details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_scores**
> [ScoreDetails] get_user_scores(user)

List user's scores

Get the list of public scores owned by a User.  **DEPRECATED**: Please note that the current behavior will be deprecrated on **2019-01-01**. This method will no longer list private and shared scores, but only public scores of a Flat account. If you want to access to private scores, please use the [Collections API](#tag/Collection) instead. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import user_api
from flat_api.model.score_details import ScoreDetails
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user = "user_example" # str | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
    parent = "parent_example" # str | Filter the score forked from the score id `parent` (optional)

    # example passing only required values which don't have defaults set
    try:
        # List user's scores
        api_response = api_instance.get_user_scores(user)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling UserApi->get_user_scores: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List user's scores
        api_response = api_instance.get_user_scores(user, parent=parent)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling UserApi->get_user_scores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  |
 **parent** | **str**| Filter the score forked from the score id &#x60;parent&#x60; | [optional]

### Return type

[**[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user scores |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
