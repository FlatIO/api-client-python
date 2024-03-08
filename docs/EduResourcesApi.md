# flat_api.EduResourcesApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_edu_resource**](EduResourcesApi.md#copy_edu_resource) | **POST** /eduResources/{resource}/copy | Copy an education resource to a Resource Library
[**copy_edu_resource_to_demo_class**](EduResourcesApi.md#copy_edu_resource_to_demo_class) | **POST** /eduResources/{resource}/copyToDemoClass | Copy an education assignment to a teacher demo class
[**create_edu_resource**](EduResourcesApi.md#create_edu_resource) | **POST** /eduResources | Create a new education resource
[**create_edu_resource_lti_link**](EduResourcesApi.md#create_edu_resource_lti_link) | **POST** /eduResources/{resource}/createLtiLink | Create an LTI link for an education resource
[**delete_edu_resource**](EduResourcesApi.md#delete_edu_resource) | **DELETE** /eduResources/{resource} | Delete an education resource
[**get_edu_resource**](EduResourcesApi.md#get_edu_resource) | **GET** /eduResources/{resource} | Get an education resource
[**list_edu_libraries**](EduResourcesApi.md#list_edu_libraries) | **GET** /eduResources/libraries | List the education libraries
[**list_edu_resources**](EduResourcesApi.md#list_edu_resources) | **GET** /eduResources | List education resources in a library or folder
[**move_edu_resource**](EduResourcesApi.md#move_edu_resource) | **POST** /eduResources/{resource}/move | Move an education resource
[**update_edu_resource**](EduResourcesApi.md#update_edu_resource) | **PUT** /eduResources/{resource} | Update an education resource metadata
[**update_edu_resource_assignment**](EduResourcesApi.md#update_edu_resource_assignment) | **PUT** /eduResources/{resource}/assignment | Update an education resource assignment
[**use_edu_resource_in_class**](EduResourcesApi.md#use_edu_resource_in_class) | **POST** /eduResources/{resource}/useInClass | Use an education resource in a class


# **copy_edu_resource**
> EduResource copy_edu_resource(resource, edu_resource_copy)

Copy an education resource to a Resource Library

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.edu_resource import EduResource
from flat_api.models.edu_resource_copy import EduResourceCopy
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource
    edu_resource_copy = flat_api.EduResourceCopy() # EduResourceCopy | 

    try:
        # Copy an education resource to a Resource Library
        api_response = api_instance.copy_edu_resource(resource, edu_resource_copy)
        print("The response of EduResourcesApi->copy_edu_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->copy_edu_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 
 **edu_resource_copy** | [**EduResourceCopy**](EduResourceCopy.md)|  | 

### Return type

[**EduResource**](EduResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched resource |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_edu_resource_to_demo_class**
> ClassAssignment copy_edu_resource_to_demo_class(resource)

Copy an education assignment to a teacher demo class

Once a resource library can be published to a class (`Assignment.capabilities.canPublishInClass = true`), this endpoint can be used for the feature \"View as student\".  It will ensure the teacher has a demo class, then copy the assignment to the demo class. You can then use `POST /classes/{class}/testStudent` to create a testing student account in the demo class. 

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.class_assignment import ClassAssignment
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource

    try:
        # Copy an education assignment to a teacher demo class
        api_response = api_instance.copy_edu_resource_to_demo_class(resource)
        print("The response of EduResourcesApi->copy_edu_resource_to_demo_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->copy_edu_resource_to_demo_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 

### Return type

[**ClassAssignment**](ClassAssignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assignment copied to the demo class |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_edu_resource**
> EduResource create_edu_resource(edu_resource_creation)

Create a new education resource

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.edu_resource import EduResource
from flat_api.models.edu_resource_creation import EduResourceCreation
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    edu_resource_creation = flat_api.EduResourceCreation() # EduResourceCreation | 

    try:
        # Create a new education resource
        api_response = api_instance.create_edu_resource(edu_resource_creation)
        print("The response of EduResourcesApi->create_edu_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->create_edu_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edu_resource_creation** | [**EduResourceCreation**](EduResourceCreation.md)|  | 

### Return type

[**EduResource**](EduResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched resource |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_edu_resource_lti_link**
> EduResourceLtiLink create_edu_resource_lti_link(resource)

Create an LTI link for an education resource

This endpoint will return an LTI link that can be used to launch Flat for Education. The link, in a context from a class, will ensure the assignment has been copied in the class. 

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.edu_resource_lti_link import EduResourceLtiLink
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource

    try:
        # Create an LTI link for an education resource
        api_response = api_instance.create_edu_resource_lti_link(resource)
        print("The response of EduResourcesApi->create_edu_resource_lti_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->create_edu_resource_lti_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 

### Return type

[**EduResourceLtiLink**](EduResourceLtiLink.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created LTI Link |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_edu_resource**
> delete_edu_resource(resource)

Delete an education resource

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource

    try:
        # Delete an education resource
        api_instance.delete_edu_resource(resource)
    except Exception as e:
        print("Exception when calling EduResourcesApi->delete_edu_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edu_resource**
> EduResource get_edu_resource(resource)

Get an education resource

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.edu_resource import EduResource
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource

    try:
        # Get an education resource
        api_response = api_instance.get_edu_resource(resource)
        print("The response of EduResourcesApi->get_edu_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->get_edu_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 

### Return type

[**EduResource**](EduResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched resource |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edu_libraries**
> List[EduLibrary] list_edu_libraries()

List the education libraries

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.edu_library import EduLibrary
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)

    try:
        # List the education libraries
        api_response = api_instance.list_edu_libraries()
        print("The response of EduResourcesApi->list_edu_libraries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->list_edu_libraries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EduLibrary]**](EduLibrary.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched resource |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edu_resources**
> List[EduResource] list_edu_resources(parent=parent, type=type, sort=sort, direction=direction, limit=limit, next=next, previous=previous)

List education resources in a library or folder

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.edu_resource import EduResource
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    parent = 'root' # str | List the resources contained in this `parent` library or folder  (optional) (default to 'root')
    type = 'type_example' # str | Filter the returned resources by type  (optional)
    sort = 'creationDate' # str | Sort (optional) (default to 'creationDate')
    direction = 'direction_example' # str | Sort direction (optional)
    limit = 25 # int | This is the maximum number of resources that may be returned (optional) (default to 25)
    next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)

    try:
        # List education resources in a library or folder
        api_response = api_instance.list_edu_resources(parent=parent, type=type, sort=sort, direction=direction, limit=limit, next=next, previous=previous)
        print("The response of EduResourcesApi->list_edu_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->list_edu_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| List the resources contained in this &#x60;parent&#x60; library or folder  | [optional] [default to &#39;root&#39;]
 **type** | **str**| Filter the returned resources by type  | [optional] 
 **sort** | **str**| Sort | [optional] [default to &#39;creationDate&#39;]
 **direction** | **str**| Sort direction | [optional] 
 **limit** | **int**| This is the maximum number of resources that may be returned | [optional] [default to 25]
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 

### Return type

[**List[EduResource]**](EduResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_edu_resource**
> EduResource move_edu_resource(resource, edu_resource_move)

Move an education resource

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.edu_resource import EduResource
from flat_api.models.edu_resource_move import EduResourceMove
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource
    edu_resource_move = flat_api.EduResourceMove() # EduResourceMove | 

    try:
        # Move an education resource
        api_response = api_instance.move_edu_resource(resource, edu_resource_move)
        print("The response of EduResourcesApi->move_edu_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->move_edu_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 
 **edu_resource_move** | [**EduResourceMove**](EduResourceMove.md)|  | 

### Return type

[**EduResource**](EduResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched resource |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_edu_resource**
> EduResource update_edu_resource(resource, edu_resource_update)

Update an education resource metadata

Update any resources metadata (e.g. title).  Use this method to rename education resources folders or assignments. 

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.edu_resource import EduResource
from flat_api.models.edu_resource_update import EduResourceUpdate
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource
    edu_resource_update = flat_api.EduResourceUpdate() # EduResourceUpdate | 

    try:
        # Update an education resource metadata
        api_response = api_instance.update_edu_resource(resource, edu_resource_update)
        print("The response of EduResourcesApi->update_edu_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->update_edu_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 
 **edu_resource_update** | [**EduResourceUpdate**](EduResourceUpdate.md)|  | 

### Return type

[**EduResource**](EduResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched resource |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_edu_resource_assignment**
> Assignment update_edu_resource_assignment(resource, assignment_update)

Update an education resource assignment

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.assignment import Assignment
from flat_api.models.assignment_update import AssignmentUpdate
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource
    assignment_update = flat_api.AssignmentUpdate() # AssignmentUpdate | 

    try:
        # Update an education resource assignment
        api_response = api_instance.update_edu_resource_assignment(resource, assignment_update)
        print("The response of EduResourcesApi->update_edu_resource_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->update_edu_resource_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 
 **assignment_update** | [**AssignmentUpdate**](AssignmentUpdate.md)|  | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched resource |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **use_edu_resource_in_class**
> ClassAssignment use_edu_resource_in_class(resource, edu_resource_use_in_class)

Use an education resource in a class

This endpoint will copy a resource and the underlying resources. The assignment will be created as a draft that can be completed with other options before publishing (e.g. due date, publication date for scheduling, etc.). 

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.class_assignment import ClassAssignment
from flat_api.models.edu_resource_use_in_class import EduResourceUseInClass
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.EduResourcesApi(api_client)
    resource = 'resource_example' # str | Unique identifier of the resource
    edu_resource_use_in_class = flat_api.EduResourceUseInClass() # EduResourceUseInClass | 

    try:
        # Use an education resource in a class
        api_response = api_instance.use_edu_resource_in_class(resource, edu_resource_use_in_class)
        print("The response of EduResourcesApi->use_edu_resource_in_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EduResourcesApi->use_edu_resource_in_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Unique identifier of the resource | 
 **edu_resource_use_in_class** | [**EduResourceUseInClass**](EduResourceUseInClass.md)|  | 

### Return type

[**ClassAssignment**](ClassAssignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assignment copied to the chosen class |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

