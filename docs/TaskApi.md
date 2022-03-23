# flat_api.TaskApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TaskApi.md#get_task) | **GET** /tasks/{task} | Get a task details


# **get_task**
> Task get_task(task)

Get a task details

This method can be used to follow a task progression, for example while a score is being exported. 

### Example

* OAuth Authentication (OAuth2): 
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.TaskApi(flat_api.ApiClient(configuration))
task = 'task_example' # str | Unique identifier for the task

try:
    # Get a task details
    api_response = api_instance.get_task(task)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | **str**| Unique identifier for the task | 

### Return type

[**Task**](Task.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
