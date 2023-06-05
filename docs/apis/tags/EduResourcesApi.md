<a id="__pageTop"></a>
# flat_api.apis.tags.edu_resources_api.EduResourcesApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_edu_resource**](#copy_edu_resource) | **post** /eduResources/{resource}/copy | Copy an education resource to a Resource Library
[**copy_edu_resource_to_demo_class**](#copy_edu_resource_to_demo_class) | **post** /eduResources/{resource}/copyToDemoClass | Copy an education assignment to a teacher demo class
[**create_edu_resource**](#create_edu_resource) | **post** /eduResources | Create a new education resource
[**delete_edu_resource**](#delete_edu_resource) | **delete** /eduResources/{resource} | Delete an education resource
[**get_edu_resource**](#get_edu_resource) | **get** /eduResources/{resource} | Get an education resource
[**list_edu_libraries**](#list_edu_libraries) | **get** /eduResources/libraries | List the education libraries
[**list_edu_resources**](#list_edu_resources) | **get** /eduResources | List education resources in a library or folder
[**move_edu_resource**](#move_edu_resource) | **post** /eduResources/{resource}/move | Move an education resource
[**update_edu_resource**](#update_edu_resource) | **put** /eduResources/{resource} | Update an education resource metadata
[**update_edu_resource_assignment**](#update_edu_resource_assignment) | **put** /eduResources/{resource}/assignment | Update an education resource assignment
[**use_edu_resource_in_class**](#use_edu_resource_in_class) | **post** /eduResources/{resource}/useInClass | Use an education resource in a class

# **copy_edu_resource**
<a id="copy_edu_resource"></a>
> EduResource copy_edu_resource(resourceedu_resource_copy)

Copy an education resource to a Resource Library

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.edu_resource_copy import EduResourceCopy
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.edu_resource import EduResource
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
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    body = EduResourceCopy(
        destination="destination_example",
    )
    try:
        # Copy an education resource to a Resource Library
        api_response = api_instance.copy_edu_resource(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->copy_edu_resource: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResourceCopy**](../../models/EduResourceCopy.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#copy_edu_resource.ApiResponseFor200) | Fetched resource
default | [ApiResponseForDefault](#copy_edu_resource.ApiResponseForDefault) | Error

#### copy_edu_resource.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResource**](../../models/EduResource.md) |  | 


#### copy_edu_resource.ApiResponseForDefault
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

# **copy_edu_resource_to_demo_class**
<a id="copy_edu_resource_to_demo_class"></a>
> ClassAssignment copy_edu_resource_to_demo_class(resource)

Copy an education assignment to a teacher demo class

Once a resource library can be published to a class (`Assignment.capabilities.canPublishInClass = true`), this endpoint can be used for the feature \"View as student\".  It will ensure the teacher has a demo class, then copy the assignment to the demo class. You can then use `POST /classes/{class}/testStudent` to create a testing student account in the demo class. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.class_assignment import ClassAssignment
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
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    try:
        # Copy an education assignment to a teacher demo class
        api_response = api_instance.copy_edu_resource_to_demo_class(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->copy_edu_resource_to_demo_class: %s\n" % e)
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
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#copy_edu_resource_to_demo_class.ApiResponseFor200) | Assignment copied to the demo class
default | [ApiResponseForDefault](#copy_edu_resource_to_demo_class.ApiResponseForDefault) | Error

#### copy_edu_resource_to_demo_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassAssignment**](../../models/ClassAssignment.md) |  | 


#### copy_edu_resource_to_demo_class.ApiResponseForDefault
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

# **create_edu_resource**
<a id="create_edu_resource"></a>
> EduResource create_edu_resource(edu_resource_creation)

Create a new education resource

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.edu_resource_creation import EduResourceCreation
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.edu_resource import EduResource
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
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    body = EduResourceCreation(
        type=EduResourceType("assignment"),
        title="title_example",
        parent="root",
    )
    try:
        # Create a new education resource
        api_response = api_instance.create_edu_resource(
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->create_edu_resource: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResourceCreation**](../../models/EduResourceCreation.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_edu_resource.ApiResponseFor200) | Fetched resource
default | [ApiResponseForDefault](#create_edu_resource.ApiResponseForDefault) | Error

#### create_edu_resource.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResource**](../../models/EduResource.md) |  | 


#### create_edu_resource.ApiResponseForDefault
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

# **delete_edu_resource**
<a id="delete_edu_resource"></a>
> delete_edu_resource(resource)

Delete an education resource

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
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
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    try:
        # Delete an education resource
        api_response = api_instance.delete_edu_resource(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->delete_edu_resource: %s\n" % e)
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
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_edu_resource.ApiResponseFor204) | Resource deleted
default | [ApiResponseForDefault](#delete_edu_resource.ApiResponseForDefault) | Error

#### delete_edu_resource.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_edu_resource.ApiResponseForDefault
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

# **get_edu_resource**
<a id="get_edu_resource"></a>
> EduResource get_edu_resource(resource)

Get an education resource

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.edu_resource import EduResource
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
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    try:
        # Get an education resource
        api_response = api_instance.get_edu_resource(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->get_edu_resource: %s\n" % e)
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
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_edu_resource.ApiResponseFor200) | Fetched resource
default | [ApiResponseForDefault](#get_edu_resource.ApiResponseForDefault) | Error

#### get_edu_resource.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResource**](../../models/EduResource.md) |  | 


#### get_edu_resource.ApiResponseForDefault
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

# **list_edu_libraries**
<a id="list_edu_libraries"></a>
> [EduLibrary] list_edu_libraries()

List the education libraries

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.edu_library import EduLibrary
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
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the education libraries
        api_response = api_instance.list_edu_libraries()
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->list_edu_libraries: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_edu_libraries.ApiResponseFor200) | Fetched resource
default | [ApiResponseForDefault](#list_edu_libraries.ApiResponseForDefault) | Error

#### list_edu_libraries.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

List of libraries to display

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of libraries to display | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EduLibrary**]({{complexTypePrefix}}EduLibrary.md) | [**EduLibrary**]({{complexTypePrefix}}EduLibrary.md) | [**EduLibrary**]({{complexTypePrefix}}EduLibrary.md) |  | 

#### list_edu_libraries.ApiResponseForDefault
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

# **list_edu_resources**
<a id="list_edu_resources"></a>
> [EduResource] list_edu_resources()

List education resources in a library or folder

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.edu_resource import EduResource
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
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only optional values
    query_params = {
        'parent': "root",
        'type': "assignment",
        'sort': "creationDate",
        'direction': "asc",
        'limit': 25,
        'next': "next_example",
        'previous': "previous_example",
    }
    try:
        # List education resources in a library or folder
        api_response = api_instance.list_edu_resources(
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->list_edu_resources: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
parent | ParentSchema | | optional
type | TypeSchema | | optional
sort | SortSchema | | optional
direction | DirectionSchema | | optional
limit | LimitSchema | | optional
next | NextSchema | | optional
previous | PreviousSchema | | optional


# ParentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "root"

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["assignment", "folder", ] 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["creationDate", "updateDate", "title", ] if omitted the server will use the default value of "creationDate"

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 25

# NextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PreviousSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_edu_resources.ApiResponseFor200) | List of resources
default | [ApiResponseForDefault](#list_edu_resources.ApiResponseForDefault) | Error

#### list_edu_resources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EduResource**]({{complexTypePrefix}}EduResource.md) | [**EduResource**]({{complexTypePrefix}}EduResource.md) | [**EduResource**]({{complexTypePrefix}}EduResource.md) |  | 

#### list_edu_resources.ApiResponseForDefault
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

# **move_edu_resource**
<a id="move_edu_resource"></a>
> EduResource move_edu_resource(resourceedu_resource_move)

Move an education resource

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.edu_resource_move import EduResourceMove
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.edu_resource import EduResource
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
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    body = EduResourceMove(
        destination="destination_example",
    )
    try:
        # Move an education resource
        api_response = api_instance.move_edu_resource(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->move_edu_resource: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResourceMove**](../../models/EduResourceMove.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#move_edu_resource.ApiResponseFor200) | Fetched resource
default | [ApiResponseForDefault](#move_edu_resource.ApiResponseForDefault) | Error

#### move_edu_resource.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResource**](../../models/EduResource.md) |  | 


#### move_edu_resource.ApiResponseForDefault
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

# **update_edu_resource**
<a id="update_edu_resource"></a>
> EduResource update_edu_resource(resourceedu_resource_update)

Update an education resource metadata

Update any resources metadata (e.g. title).  Use this method to rename education resources folders or assignments. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.edu_resource import EduResource
from flat_api.model.edu_resource_update import EduResourceUpdate
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
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    body = EduResourceUpdate(
        title="title_example",
    )
    try:
        # Update an education resource metadata
        api_response = api_instance.update_edu_resource(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->update_edu_resource: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResourceUpdate**](../../models/EduResourceUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_edu_resource.ApiResponseFor200) | Fetched resource
default | [ApiResponseForDefault](#update_edu_resource.ApiResponseForDefault) | Error

#### update_edu_resource.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResource**](../../models/EduResource.md) |  | 


#### update_edu_resource.ApiResponseForDefault
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

# **update_edu_resource_assignment**
<a id="update_edu_resource_assignment"></a>
> Assignment update_edu_resource_assignment(resourceassignment_update)

Update an education resource assignment

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.assignment_update import AssignmentUpdate
from flat_api.model.assignment import Assignment
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
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    body = AssignmentUpdate(
        type=AssignmentType("none"),
        title="title_example",
        description="description_example",
        attachments=[
            ClassAttachmentCreation(
                type="rich",
                score="score_example",
                worksheet="worksheet_example",
                sharing_mode=MediaScoreSharingMode("read"),
                lock_score_template=True,
                url="url_example",
                google_drive_file_id="google_drive_file_id_example",
            )
        ],
        nb_playback_authorized=3.14,
        toolset="toolset_example",
        cover_file="cover_file_example",
        cover="cover_example",
        max_points=0,
        release_grades="auto",
        shuffle_exercises=True,
    )
    try:
        # Update an education resource assignment
        api_response = api_instance.update_edu_resource_assignment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->update_edu_resource_assignment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignmentUpdate**](../../models/AssignmentUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_edu_resource_assignment.ApiResponseFor200) | Fetched resource
default | [ApiResponseForDefault](#update_edu_resource_assignment.ApiResponseForDefault) | Error

#### update_edu_resource_assignment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Assignment**](../../models/Assignment.md) |  | 


#### update_edu_resource_assignment.ApiResponseForDefault
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

# **use_edu_resource_in_class**
<a id="use_edu_resource_in_class"></a>
> ClassAssignment use_edu_resource_in_class(resourceedu_resource_use_in_class)

Use an education resource in a class

This endpoint will copy a resource and the underlying resources. The assignment will be created as a draft that can be completed with other options before publishing (e.g. due date, publication date for scheduling, etc.). 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import edu_resources_api
from flat_api.model.class_assignment import ClassAssignment
from flat_api.model.edu_resource_use_in_class import EduResourceUseInClass
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
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edu_resources_api.EduResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    body = EduResourceUseInClass(
        classroom="classroom_example",
        assignment="assignment_example",
    )
    try:
        # Use an education resource in a class
        api_response = api_instance.use_edu_resource_in_class(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling EduResourcesApi->use_edu_resource_in_class: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EduResourceUseInClass**](../../models/EduResourceUseInClass.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#use_edu_resource_in_class.ApiResponseFor200) | Assignment copied to the chosen class
default | [ApiResponseForDefault](#use_edu_resource_in_class.ApiResponseForDefault) | Error

#### use_edu_resource_in_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassAssignment**](../../models/ClassAssignment.md) |  | 


#### use_edu_resource_in_class.ApiResponseForDefault
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

