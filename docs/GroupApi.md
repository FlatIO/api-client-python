# flat_api.GroupApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group_scores**](GroupApi.md#get_group_scores) | **GET** /groups/{group}/scores | List group&#39;s scores


# **get_group_scores**
> list[ScoreDetails] get_group_scores(group, parent=parent)

List group's scores

Get the list of scores shared with a group. 

### Example 
```python
from __future__ import print_statement
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flat_api.GroupApi()
group = 'group_example' # str | Unique identifier of the group
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
 **group** | **str**| Unique identifier of the group | 
 **parent** | **str**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] 

### Return type

[**list[ScoreDetails]**](ScoreDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

