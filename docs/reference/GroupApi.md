# flat_api.GroupApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_user**](GroupApi.md#add_group_user) | **POST** /groups/{group}/users | Add a student to a group
[**create_group**](GroupApi.md#create_group) | **POST** /groups | Create a new group
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /groups/{group} | Delete a group
[**get_group_details**](GroupApi.md#get_group_details) | **GET** /groups/{group} | Get group information
[**get_group_scores**](GroupApi.md#get_group_scores) | **GET** /groups/{group}/scores | List group&#39;s scores
[**list_group_users**](GroupApi.md#list_group_users) | **GET** /groups/{group}/users | List group&#39;s users
[**list_groups**](GroupApi.md#list_groups) | **GET** /groups | List groups
[**remove_group_user**](GroupApi.md#remove_group_user) | **DELETE** /groups/{group}/users/{user} | Remove a student from a class group
[**rename_group**](GroupApi.md#rename_group) | **PUT** /groups/{group} | Rename a group


# **add_group_user**
> AddGroupUser200Response add_group_user(group, add_group_user_request)

Add a student to a group

Add a student to the specified group (must be in the same class)

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.add_group_user200_response import AddGroupUser200Response
from flat_api.models.add_group_user_request import AddGroupUserRequest
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
    api_instance = flat_api.GroupApi(api_client)
    group = 'group_example' # str | Unique identifier of a Flat group 
    add_group_user_request = flat_api.AddGroupUserRequest() # AddGroupUserRequest | 

    try:
        # Add a student to a group
        api_response = api_instance.add_group_user(group, add_group_user_request)
        print("The response of GroupApi->add_group_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->add_group_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 
 **add_group_user_request** | [**AddGroupUserRequest**](AddGroupUserRequest.md)|  | 

### Return type

[**AddGroupUser200Response**](AddGroupUser200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Membership created |  -  |
**400** | Bad Request - Invalid user ID or user not enrolled in class |  -  |
**403** | Forbidden - Insufficient permissions or invalid group type |  -  |
**404** | Not Found - Group not found or user not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> GroupDetails create_group(group_creation)

Create a new group

Create a group of the given type, tied to a classroom, optionally with initial members.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.group_creation import GroupCreation
from flat_api.models.group_details import GroupDetails
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
    api_instance = flat_api.GroupApi(api_client)
    group_creation = flat_api.GroupCreation() # GroupCreation | 

    try:
        # Create a new group
        api_response = api_instance.create_group(group_creation)
        print("The response of GroupApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_creation** | [**GroupCreation**](GroupCreation.md)|  | 

### Return type

[**GroupDetails**](GroupDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new group |  -  |
**400** | Bad Request - Invalid type or missing required parameters |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**409** | Conflict - Group name already exists |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group)

Delete a group

Delete a group. Only available to teachers of the classroom.

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
    api_instance = flat_api.GroupApi(api_client)
    group = 'group_example' # str | Unique identifier of a Flat group 

    try:
        # Delete a group
        api_instance.delete_group(group)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 

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
**204** | Group deleted |  -  |
**403** | Forbidden - Insufficient permissions or invalid group type |  -  |
**404** | Not Found - Group not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_details**
> GroupDetails get_group_details(group)

Get group information

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.group_details import GroupDetails
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
    api_instance = flat_api.GroupApi(api_client)
    group = 'group_example' # str | Unique identifier of a Flat group 

    try:
        # Get group information
        api_response = api_instance.get_group_details(group)
        print("The response of GroupApi->get_group_details:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group details |  -  |
**404** | Not Found - Group not found or insufficient permissions |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_scores**
> List[ScoreDetails] get_group_scores(group, parent=parent)

List group's scores

Get the list of scores shared with a group.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_details import ScoreDetails
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
    api_instance = flat_api.GroupApi(api_client)
    group = 'group_example' # str | Unique identifier of a Flat group 
    parent = 'parent_example' # str | Filter the score forked from the score id `parent` (optional)

    try:
        # List group's scores
        api_response = api_instance.get_group_scores(group, parent=parent)
        print("The response of GroupApi->get_group_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 
 **parent** | **str**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] 

### Return type

[**List[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group&#39;s scores |  -  |
**404** | Not Found - Group not found or user not member of group |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_users**
> List[UserPublic] list_group_users(group, source=source)

List group's users

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.user_public import UserPublic
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
    api_instance = flat_api.GroupApi(api_client)
    group = 'group_example' # str | Unique identifier of a Flat group 
    source = 'source_example' # str | Filter the users by their source  (optional)

    try:
        # List group's users
        api_response = api_instance.list_group_users(group, source=source)
        print("The response of GroupApi->list_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_group_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 
 **source** | **str**| Filter the users by their source  | [optional] 

### Return type

[**List[UserPublic]**](UserPublic.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of users member of the group |  -  |
**404** | Not Found - Group not found or insufficient permissions |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> List[GroupDetails] list_groups(type, classroom=classroom, assignment=assignment)

List groups

List all groups of a given type, filtered by either a classroom or an assignment.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.group_details import GroupDetails
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
    api_instance = flat_api.GroupApi(api_client)
    type = 'type_example' # str | 
    classroom = 'classroom_example' # str | Classroom ID to filter by (optional)
    assignment = 'assignment_example' # str | Assignment ID to filter by (optional)

    try:
        # List groups
        api_response = api_instance.list_groups(type, classroom=classroom, assignment=assignment)
        print("The response of GroupApi->list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **classroom** | **str**| Classroom ID to filter by | [optional] 
 **assignment** | **str**| Assignment ID to filter by | [optional] 

### Return type

[**List[GroupDetails]**](GroupDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups |  -  |
**400** | Bad Request - Invalid type or missing required parameters |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**404** | Not Found - Classroom or assignment not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_user**
> remove_group_user(group, user)

Remove a student from a class group

Remove a student from a class group

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
    api_instance = flat_api.GroupApi(api_client)
    group = 'group_example' # str | Unique identifier of a Flat group 
    user = 'user_example' # str | User ID

    try:
        # Remove a student from a class group
        api_instance.remove_group_user(group, user)
    except Exception as e:
        print("Exception when calling GroupApi->remove_group_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 
 **user** | **str**| User ID | 

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
**204** | Membership removed |  -  |
**403** | Forbidden - Insufficient permissions or invalid group type |  -  |
**404** | Not Found - Group not found or user not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_group**
> GroupDetails rename_group(group, rename_group_request)

Rename a group

Rename a sub-group. Only available for class student groups.

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.group_details import GroupDetails
from flat_api.models.rename_group_request import RenameGroupRequest
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
    api_instance = flat_api.GroupApi(api_client)
    group = 'group_example' # str | Unique identifier of a Flat group 
    rename_group_request = flat_api.RenameGroupRequest() # RenameGroupRequest | 

    try:
        # Rename a group
        api_response = api_instance.rename_group(group, rename_group_request)
        print("The response of GroupApi->rename_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->rename_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 
 **rename_group_request** | [**RenameGroupRequest**](RenameGroupRequest.md)|  | 

### Return type

[**GroupDetails**](GroupDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated group |  -  |
**400** | Bad Request - Invalid group ID or missing name |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**404** | Not Found - Group not found |  -  |
**409** | Conflict - Group name already exists |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

