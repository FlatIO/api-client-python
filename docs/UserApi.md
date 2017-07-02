# flat_api.UserApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ger_user_likes**](UserApi.md#ger_user_likes) | **GET** /users/{user}/likes | List liked scores
[**get_user**](UserApi.md#get_user) | **GET** /users/{user} | Get a public user profile
[**get_user_scores**](UserApi.md#get_user_scores) | **GET** /users/{user}/scores | List user&#39;s scores


# **ger_user_likes**
> list[ScoreDetails] ger_user_likes(user, ids=ids)

List liked scores

### Example 
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
flat_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.UserApi()
user = 'user_example' # str | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
ids = true # bool | Return only the identifiers of the scores (optional)

try: 
    # List liked scores
    api_response = api_instance.ger_user_likes(user, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->ger_user_likes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | 
 **ids** | **bool**| Return only the identifiers of the scores | [optional] 

### Return type

[**list[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserPublic get_user(user)

Get a public user profile

Get a public profile of a Flat User. 

### Example 
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
flat_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.UserApi()
user = 'user_example' # str | This route parameter is the unique identifier of the user. You can specify an email instead of an unique identifier. If you are executing this request authenticated, you can use `me` as a value instead of the current User unique identifier to work on the current authenticated user. 

try: 
    # Get a public user profile
    api_response = api_instance.get_user(user)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_scores**
> list[ScoreDetails] get_user_scores(user, parent=parent)

List user's scores

Get the list of scores owned by the User 

### Example 
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
flat_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.UserApi()
user = 'user_example' # str | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
parent = 'parent_example' # str | Filter the score forked from the score id `parent` (optional)

try: 
    # List user's scores
    api_response = api_instance.get_user_scores(user, parent=parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | 
 **parent** | **str**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] 

### Return type

[**list[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

