<a id="__pageTop"></a>
# flat_api.apis.tags.task_api.TaskApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](#get_task) | **get** /tasks/{task} | Get a task details

# **get_task**
<a id="get_task"></a>
> Task get_task(task)

Get a task details

This method can be used to follow a task progression, for example while a score is being exported. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import task_api
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.task import Task
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
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'task': "task_example",
    }
    try:
        # Get a task details
        api_response = api_instance.get_task(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling TaskApi->get_task: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
task | TaskSchema | | 

# TaskSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_task.ApiResponseFor200) | Task details
default | [ApiResponseForDefault](#get_task.ApiResponseForDefault) | Error

#### get_task.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Task**](../../models/Task.md) |  | 


#### get_task.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

