# flat_api.GroupApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group_details**](GroupApi.md#get_group_details) | **GET** /groups/{group} | Get group information
[**get_group_scores**](GroupApi.md#get_group_scores) | **GET** /groups/{group}/scores | List group&#39;s scores
[**list_group_users**](GroupApi.md#list_group_users) | **GET** /groups/{group}/users | List group&#39;s users


# **get_group_details**
> GroupDetails get_group_details(group)

Get group information

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
api_instance = flat_api.GroupApi()
group = 'group_example' # str | Unique identifier of a Flat group 

try: 
    # Get group information
    api_response = api_instance.get_group_details(group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 

### Return type

[**GroupDetails**](GroupDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_scores**
> list[ScoreDetails] get_group_scores(group, parent=parent)

List group's scores

Get the list of scores shared with a group. 

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
api_instance = flat_api.GroupApi()
group = 'group_example' # str | Unique identifier of a Flat group 
parent = 'parent_example' # str | Filter the score forked from the score id `parent` (optional)

try: 
    # List group's scores
    api_response = api_instance.get_group_scores(group, parent=parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 
 **parent** | **str**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] 

### Return type

[**list[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_users**
> list[UserPublic] list_group_users(group)

List group's users

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
api_instance = flat_api.GroupApi()
group = 'group_example' # str | Unique identifier of a Flat group 

try: 
    # List group's users
    api_response = api_instance.list_group_users(group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 

### Return type

[**list[UserPublic]**](UserPublic.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

