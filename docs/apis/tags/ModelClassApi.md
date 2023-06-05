<a id="__pageTop"></a>
# flat_api.apis.tags.model_class_api.ModelClassApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_class**](#activate_class) | **post** /classes/{class}/activate | Activate the class
[**add_class_user**](#add_class_user) | **put** /classes/{class}/users/{user} | Add a user to the class
[**archive_assignment**](#archive_assignment) | **post** /classes/{class}/assignments/{assignment}/archive | Archive the assignment
[**archive_class**](#archive_class) | **post** /classes/{class}/archive | Archive the class
[**copy_assignment**](#copy_assignment) | **post** /classes/{class}/assignments/{assignment}/copy | Copy an assignment
[**create_class**](#create_class) | **post** /classes | Create a new class
[**create_class_assignment**](#create_class_assignment) | **post** /classes/{class}/assignments | Assignment creation
[**create_submission**](#create_submission) | **put** /classes/{class}/assignments/{assignment}/submissions | Create or edit a submission
[**create_test_student_account**](#create_test_student_account) | **post** /classes/{class}/testStudent | Create a test student account
[**delete_class_user**](#delete_class_user) | **delete** /classes/{class}/users/{user} | Remove a user from the class
[**delete_submission**](#delete_submission) | **delete** /classes/{class}/assignments/{assignment}/submissions/{submission} | Reset a submission
[**delete_submission_comment**](#delete_submission_comment) | **delete** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Delete a feedback comment to a submission
[**edit_submission**](#edit_submission) | **put** /classes/{class}/assignments/{assignment}/submissions/{submission} | Edit a submission
[**enroll_class**](#enroll_class) | **post** /classes/enroll/{enrollmentCode} | Join a class
[**export_submissions_reviews_as_csv**](#export_submissions_reviews_as_csv) | **get** /classes/{class}/assignments/{assignment}/submissions/csv | CSV Grades exports
[**export_submissions_reviews_as_excel**](#export_submissions_reviews_as_excel) | **get** /classes/{class}/assignments/{assignment}/submissions/excel | Excel Grades exports
[**get_class**](#get_class) | **get** /classes/{class} | Get the details of a single class
[**get_score_submissions**](#get_score_submissions) | **get** /scores/{score}/submissions | List submissions related to the score
[**get_submission**](#get_submission) | **get** /classes/{class}/assignments/{assignment}/submissions/{submission} | Get a student submission
[**get_submission_comments**](#get_submission_comments) | **get** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | List the feedback comments of a submission
[**get_submission_history**](#get_submission_history) | **get** /classes/{class}/assignments/{assignment}/submissions/{submission}/history | Get the history of the submission
[**get_submissions**](#get_submissions) | **get** /classes/{class}/assignments/{assignment}/submissions | List the students&#x27; submissions
[**list_assignments**](#list_assignments) | **get** /classes/{class}/assignments | Assignments listing
[**list_class_student_submissions**](#list_class_student_submissions) | **get** /classes/{class}/students/{user}/submissions | List the submissions for a student
[**list_classes**](#list_classes) | **get** /classes | List the classes available for the current user
[**post_submission_comment**](#post_submission_comment) | **post** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | Add a feedback comment to a submission
[**unarchive_assignment**](#unarchive_assignment) | **delete** /classes/{class}/assignments/{assignment}/archive | Unarchive the assignment.
[**unarchive_class**](#unarchive_class) | **delete** /classes/{class}/archive | Unarchive the class
[**update_class**](#update_class) | **put** /classes/{class} | Update the class
[**update_submission_comment**](#update_submission_comment) | **put** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Update a feedback comment to a submission

# **activate_class**
<a id="activate_class"></a>
> ClassDetails activate_class(_class)

Activate the class

Mark the class as `active`. This is mainly used for classes synchronized from Clever that are initially with an `inactive` state and hidden in the UI. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.class_details import ClassDetails
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
    }
    try:
        # Activate the class
        api_response = api_instance.activate_class(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->activate_class: %s\n" % e)
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
class | ModelClassSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#activate_class.ApiResponseFor200) | The class details
default | [ApiResponseForDefault](#activate_class.ApiResponseForDefault) | Error

#### activate_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassDetails**](../../models/ClassDetails.md) |  | 


#### activate_class.ApiResponseForDefault
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

# **add_class_user**
<a id="add_class_user"></a>
> add_class_user(_classuser)

Add a user to the class

This method can be used by a teacher of the class to enroll another Flat user into the class.  Only users that are part of your Organization can be enrolled in a class of this same Organization.  When enrolling a user in the class, Flat will automatically add this user to the corresponding Class group, based on this role in the Organization. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'user': "user_example",
    }
    try:
        # Add a user to the class
        api_response = api_instance.add_class_user(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->add_class_user: %s\n" % e)
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
class | ModelClassSchema | | 
user | UserSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#add_class_user.ApiResponseFor204) | The user has been added to the class
default | [ApiResponseForDefault](#add_class_user.ApiResponseForDefault) | Error

#### add_class_user.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### add_class_user.ApiResponseForDefault
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

# **archive_assignment**
<a id="archive_assignment"></a>
> Assignment archive_assignment(_classassignment)

Archive the assignment

Archive the assignment 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
    }
    try:
        # Archive the assignment
        api_response = api_instance.archive_assignment(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->archive_assignment: %s\n" % e)
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
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#archive_assignment.ApiResponseFor200) | The assignment details
default | [ApiResponseForDefault](#archive_assignment.ApiResponseForDefault) | Error

#### archive_assignment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Assignment**](../../models/Assignment.md) |  | 


#### archive_assignment.ApiResponseForDefault
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

# **archive_class**
<a id="archive_class"></a>
> ClassDetails archive_class(_class)

Archive the class

Mark the class as `archived`. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.class_details import ClassDetails
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
    }
    try:
        # Archive the class
        api_response = api_instance.archive_class(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->archive_class: %s\n" % e)
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
class | ModelClassSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#archive_class.ApiResponseFor200) | The class details
default | [ApiResponseForDefault](#archive_class.ApiResponseForDefault) | Error

#### archive_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassDetails**](../../models/ClassDetails.md) |  | 


#### archive_class.ApiResponseForDefault
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

# **copy_assignment**
<a id="copy_assignment"></a>
> AssignmentCopyResponse copy_assignment(_classassignmentbody)

Copy an assignment

Copy an assignment to a specified class or the resource library  For class assignments: - If the original assignment has a due date in the past, this new assignment will be created without a due date. - If the class is synchronized with an external app (e.g. Google Classroom), the copied assignment will also be posted on the external app. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_copy import AssignmentCopy
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.assignment_copy_response import AssignmentCopyResponse
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
    }
    body = AssignmentCopy(
        classroom="classroom_example",
        assignment="assignment_example",
        scheduled_date="1970-01-01T00:00:00.00Z",
        library_parent="library_parent_example",
    )
    try:
        # Copy an assignment
        api_response = api_instance.copy_assignment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->copy_assignment: %s\n" % e)
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
[**AssignmentCopy**](../../models/AssignmentCopy.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#copy_assignment.ApiResponseFor200) | The new created assignment
default | [ApiResponseForDefault](#copy_assignment.ApiResponseForDefault) | Error

#### copy_assignment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignmentCopyResponse**](../../models/AssignmentCopyResponse.md) |  | 


#### copy_assignment.ApiResponseForDefault
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

# **create_class**
<a id="create_class"></a>
> ClassDetails create_class(body)

Create a new class

Classrooms on Flat allow you to create activities with assignments and post content to a specific group.  When creating a class, Flat automatically creates two groups: one for the teachers of the course, one for the students. The creator of this class is automatically added to the teachers group.  If the classsroom is synchronized with another application like Google Classroom, some of the meta information will automatically be updated.  You can add users to this class using `PUT /classes/{class}/users/{user}`, they will automatically added to the group based on their role on Flat. Users can also enroll themselves to this class using `POST /classes/enroll/{enrollmentCode}` and the `enrollmentCode` returned in the `ClassDetails` response. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.class_details import ClassDetails
from flat_api.model.class_creation import ClassCreation
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    body = ClassCreation(
        name="name_example",
        section="section_example",
        level=ClassGradeLevel("elementary"),
        skills_focused=EduSkillsFocused([
            "notation"
        ]),
        size=0,
    )
    try:
        # Create a new class
        api_response = api_instance.create_class(
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->create_class: %s\n" % e)
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
[**ClassCreation**](../../models/ClassCreation.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_class.ApiResponseFor200) | The new class details
402 | [ApiResponseFor402](#create_class.ApiResponseFor402) | Account overquota
default | [ApiResponseForDefault](#create_class.ApiResponseForDefault) | Error

#### create_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassDetails**](../../models/ClassDetails.md) |  | 


#### create_class.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_class.ApiResponseForDefault
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

# **create_class_assignment**
<a id="create_class_assignment"></a>
> Assignment create_class_assignment(_class)

Assignment creation

Use this method as a teacher to create and post a new assignment to a class.  If the class is synchronized with Google Classroom, the assignment will be automatically posted to your Classroom course. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment import Assignment
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.class_assignment_update import ClassAssignmentUpdate
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
    }
    try:
        # Assignment creation
        api_response = api_instance.create_class_assignment(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->create_class_assignment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'class': "class_example",
    }
    body = ClassAssignmentUpdate(
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
        state="draft",
        due_date="1970-01-01T00:00:00.00Z",
        scheduled_date="1970-01-01T00:00:00.00Z",
        google_classroom=dict(
            topic_id="topic_id_example",
        ),
        microsoft_graph=dict(
            categories=[
                "categories_example"
            ],
        ),
        assignee_mode="everyone",
        assigned_students=[
            "assigned_students_example"
        ],
    )
    try:
        # Assignment creation
        api_response = api_instance.create_class_assignment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->create_class_assignment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
[**ClassAssignmentUpdate**](../../models/ClassAssignmentUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_class_assignment.ApiResponseFor200) | The assignment has been created
default | [ApiResponseForDefault](#create_class_assignment.ApiResponseForDefault) | Error

#### create_class_assignment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Assignment**](../../models/Assignment.md) |  | 


#### create_class_assignment.ApiResponseForDefault
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

# **create_submission**
<a id="create_submission"></a>
> AssignmentSubmission create_submission(_classassignmentbody)

Create or edit a submission

Use this method as a student to create, update and submit a submission related to an assignment. Students can only set `attachments` and `submit`. Teachers can use `PUT /classes/{class}/assignments/{assignment}/submissions/{submission}` to update a submission by id. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission import AssignmentSubmission
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.assignment_submission_update import AssignmentSubmissionUpdate
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
    }
    body = AssignmentSubmissionUpdate(
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
        submit=True,
        draft_grade=0,
        grade=0,
        exercises_ids=[
            "exercises_ids_example"
        ],
        _return=True,
        comments=dict(
            total=3.14,
            unread=3.14,
        ),
    )
    try:
        # Create or edit a submission
        api_response = api_instance.create_submission(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->create_submission: %s\n" % e)
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
[**AssignmentSubmissionUpdate**](../../models/AssignmentSubmissionUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_submission.ApiResponseFor200) | The submission
default | [ApiResponseForDefault](#create_submission.ApiResponseForDefault) | Error

#### create_submission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignmentSubmission**](../../models/AssignmentSubmission.md) |  | 


#### create_submission.ApiResponseForDefault
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

# **create_test_student_account**
<a id="create_test_student_account"></a>
> UserDetails create_test_student_account(_class)

Create a test student account

Test students account can be created by teachers an admin and be used to experiment the assignments.  - They are automatically added to the class. - They can be reset using this API endpoint (a new account will be created and the previous one scheduled for deletion). - These accounts don't use a user license. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.user_details import UserDetails
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
    }
    query_params = {
    }
    try:
        # Create a test student account
        api_response = api_instance.create_test_student_account(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->create_test_student_account: %s\n" % e)

    # example passing only optional values
    path_params = {
        'class': "class_example",
    }
    query_params = {
        'reset': True,
    }
    try:
        # Create a test student account
        api_response = api_instance.create_test_student_account(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->create_test_student_account: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reset | ResetSchema | | optional


# ResetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_test_student_account.ApiResponseFor200) | Test account created
default | [ApiResponseForDefault](#create_test_student_account.ApiResponseForDefault) | Error

#### create_test_student_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserDetails**](../../models/UserDetails.md) |  | 


#### create_test_student_account.ApiResponseForDefault
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

# **delete_class_user**
<a id="delete_class_user"></a>
> delete_class_user(_classuser)

Remove a user from the class

This method can be used by a teacher to remove a user from the class, or by a student to leave the classroom.  Warning: Removing a user from the class will remove the associated resources, including the submissions and feedback related to these submissions. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'user': "user_example",
    }
    try:
        # Remove a user from the class
        api_response = api_instance.delete_class_user(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->delete_class_user: %s\n" % e)
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
class | ModelClassSchema | | 
user | UserSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_class_user.ApiResponseFor204) | The user has been removed from the class
default | [ApiResponseForDefault](#delete_class_user.ApiResponseForDefault) | Error

#### delete_class_user.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_class_user.ApiResponseForDefault
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

# **delete_submission**
<a id="delete_submission"></a>
> AssignmentSubmission delete_submission(_classassignmentsubmission)

Reset a submission

Use this method as a teacher to reset a submission and allow student to start over the assignment 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission import AssignmentSubmission
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
        'submission': "submission_example",
    }
    try:
        # Reset a submission
        api_response = api_instance.delete_submission(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->delete_submission: %s\n" % e)
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
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 
submission | SubmissionSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubmissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_submission.ApiResponseFor200) | The submission object once reset
default | [ApiResponseForDefault](#delete_submission.ApiResponseForDefault) | Error

#### delete_submission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignmentSubmission**](../../models/AssignmentSubmission.md) |  | 


#### delete_submission.ApiResponseForDefault
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

# **delete_submission_comment**
<a id="delete_submission_comment"></a>
> delete_submission_comment(_classassignmentsubmissioncomment)

Delete a feedback comment to a submission

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
        'submission': "submission_example",
        'comment': "comment_example",
    }
    try:
        # Delete a feedback comment to a submission
        api_response = api_instance.delete_submission_comment(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->delete_submission_comment: %s\n" % e)
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
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 
submission | SubmissionSchema | | 
comment | CommentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubmissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CommentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_submission_comment.ApiResponseFor204) | The comment has been deleted
default | [ApiResponseForDefault](#delete_submission_comment.ApiResponseForDefault) | Error

#### delete_submission_comment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_submission_comment.ApiResponseForDefault
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

# **edit_submission**
<a id="edit_submission"></a>
> AssignmentSubmission edit_submission(_classassignmentsubmissionbody)

Edit a submission

Use this method as a teacher to update the different submission and give feedback. Teachers can only set `return`, `draftGrade` and `grade` 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission import AssignmentSubmission
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.assignment_submission_update import AssignmentSubmissionUpdate
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
        'submission': "submission_example",
    }
    body = AssignmentSubmissionUpdate(
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
        submit=True,
        draft_grade=0,
        grade=0,
        exercises_ids=[
            "exercises_ids_example"
        ],
        _return=True,
        comments=dict(
            total=3.14,
            unread=3.14,
        ),
    )
    try:
        # Edit a submission
        api_response = api_instance.edit_submission(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->edit_submission: %s\n" % e)
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
[**AssignmentSubmissionUpdate**](../../models/AssignmentSubmissionUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 
submission | SubmissionSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubmissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_submission.ApiResponseFor200) | The submission
default | [ApiResponseForDefault](#edit_submission.ApiResponseForDefault) | Error

#### edit_submission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignmentSubmission**](../../models/AssignmentSubmission.md) |  | 


#### edit_submission.ApiResponseForDefault
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

# **enroll_class**
<a id="enroll_class"></a>
> ClassDetails enroll_class(enrollment_code)

Join a class

Use this method to join a class using an enrollment code given one of the teacher of this class. This code is also available in the `ClassDetails` returned to the teachers when creating the class or listing / fetching a specific class.  Flat will automatically add the user to the corresponding class group based on this role in the organization. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.class_details import ClassDetails
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'enrollmentCode': "enrollmentCode_example",
    }
    try:
        # Join a class
        api_response = api_instance.enroll_class(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->enroll_class: %s\n" % e)
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
enrollmentCode | EnrollmentCodeSchema | | 

# EnrollmentCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#enroll_class.ApiResponseFor200) | The new class details
default | [ApiResponseForDefault](#enroll_class.ApiResponseForDefault) | Error

#### enroll_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassDetails**](../../models/ClassDetails.md) |  | 


#### enroll_class.ApiResponseForDefault
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

# **export_submissions_reviews_as_csv**
<a id="export_submissions_reviews_as_csv"></a>
> file_type export_submissions_reviews_as_csv(_classassignment)

CSV Grades exports

Export list of submissions grades to a CSV file

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
    }
    try:
        # CSV Grades exports
        api_response = api_instance.export_submissions_reviews_as_csv(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->export_submissions_reviews_as_csv: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/csv', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_submissions_reviews_as_csv.ApiResponseFor200) | List of submissions
default | [ApiResponseForDefault](#export_submissions_reviews_as_csv.ApiResponseForDefault) | Error

#### export_submissions_reviews_as_csv.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextCsv, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextCsv

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_submissions_reviews_as_csv.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextCsv, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextCsv
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_submissions_reviews_as_excel**
<a id="export_submissions_reviews_as_excel"></a>
> file_type export_submissions_reviews_as_excel(_classassignment)

Excel Grades exports

Export list of submissions grades to an Excel file

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
    }
    try:
        # Excel Grades exports
        api_response = api_instance.export_submissions_reviews_as_excel(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->export_submissions_reviews_as_excel: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_submissions_reviews_as_excel.ApiResponseFor200) | List of submissions
default | [ApiResponseForDefault](#export_submissions_reviews_as_excel.ApiResponseForDefault) | Error

#### export_submissions_reviews_as_excel.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndOpenxmlformatsOfficedocumentSpreadsheetmlSheet, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndOpenxmlformatsOfficedocumentSpreadsheetmlSheet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_submissions_reviews_as_excel.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationVndOpenxmlformatsOfficedocumentSpreadsheetmlSheet, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationVndOpenxmlformatsOfficedocumentSpreadsheetmlSheet
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_class**
<a id="get_class"></a>
> ClassDetails get_class(_class)

Get the details of a single class

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.class_details import ClassDetails
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
    }
    try:
        # Get the details of a single class
        api_response = api_instance.get_class(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->get_class: %s\n" % e)
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
class | ModelClassSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_class.ApiResponseFor200) | The new class details
default | [ApiResponseForDefault](#get_class.ApiResponseForDefault) | Error

#### get_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassDetails**](../../models/ClassDetails.md) |  | 


#### get_class.ApiResponseForDefault
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

# **get_score_submissions**
<a id="get_score_submissions"></a>
> [AssignmentSubmission] get_score_submissions(score)

List submissions related to the score

This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission import AssignmentSubmission
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    try:
        # List submissions related to the score
        api_response = api_instance.get_score_submissions(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->get_score_submissions: %s\n" % e)
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
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_submissions.ApiResponseFor200) | List of submissions
default | [ApiResponseForDefault](#get_score_submissions.ApiResponseForDefault) | Error

#### get_score_submissions.ApiResponseFor200
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
[**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) | [**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) | [**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) |  | 

#### get_score_submissions.ApiResponseForDefault
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

# **get_submission**
<a id="get_submission"></a>
> AssignmentSubmission get_submission(_classassignmentsubmission)

Get a student submission

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission import AssignmentSubmission
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
        'submission': "submission_example",
    }
    try:
        # Get a student submission
        api_response = api_instance.get_submission(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->get_submission: %s\n" % e)
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
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 
submission | SubmissionSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubmissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_submission.ApiResponseFor200) | A submission
default | [ApiResponseForDefault](#get_submission.ApiResponseForDefault) | Error

#### get_submission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignmentSubmission**](../../models/AssignmentSubmission.md) |  | 


#### get_submission.ApiResponseForDefault
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

# **get_submission_comments**
<a id="get_submission_comments"></a>
> [AssignmentSubmissionComment] get_submission_comments(_classassignmentsubmission)

List the feedback comments of a submission

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission_comment import AssignmentSubmissionComment
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
        'submission': "submission_example",
    }
    try:
        # List the feedback comments of a submission
        api_response = api_instance.get_submission_comments(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->get_submission_comments: %s\n" % e)
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
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 
submission | SubmissionSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubmissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_submission_comments.ApiResponseFor200) | The comments of the score
403 | [ApiResponseFor403](#get_submission_comments.ApiResponseFor403) | Not granted to access to this submission
404 | [ApiResponseFor404](#get_submission_comments.ApiResponseFor404) | Submission not found
default | [ApiResponseForDefault](#get_submission_comments.ApiResponseForDefault) | Error

#### get_submission_comments.ApiResponseFor200
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
[**AssignmentSubmissionComment**]({{complexTypePrefix}}AssignmentSubmissionComment.md) | [**AssignmentSubmissionComment**]({{complexTypePrefix}}AssignmentSubmissionComment.md) | [**AssignmentSubmissionComment**]({{complexTypePrefix}}AssignmentSubmissionComment.md) |  | 

#### get_submission_comments.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_submission_comments.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_submission_comments.ApiResponseForDefault
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

# **get_submission_history**
<a id="get_submission_history"></a>
> [AssignmentSubmissionHistory] get_submission_history(_classassignmentsubmission)

Get the history of the submission

For teachers only. Returns a detailed history of the submission. This currently includes state and grade histories. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission_history import AssignmentSubmissionHistory
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
        'submission': "submission_example",
    }
    try:
        # Get the history of the submission
        api_response = api_instance.get_submission_history(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->get_submission_history: %s\n" % e)
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
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 
submission | SubmissionSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubmissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_submission_history.ApiResponseFor200) | The history of the submission
403 | [ApiResponseFor403](#get_submission_history.ApiResponseFor403) | Not granted to access to this submission
404 | [ApiResponseFor404](#get_submission_history.ApiResponseFor404) | Submission not found
default | [ApiResponseForDefault](#get_submission_history.ApiResponseForDefault) | Error

#### get_submission_history.ApiResponseFor200
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
[**AssignmentSubmissionHistory**]({{complexTypePrefix}}AssignmentSubmissionHistory.md) | [**AssignmentSubmissionHistory**]({{complexTypePrefix}}AssignmentSubmissionHistory.md) | [**AssignmentSubmissionHistory**]({{complexTypePrefix}}AssignmentSubmissionHistory.md) |  | 

#### get_submission_history.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_submission_history.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_submission_history.ApiResponseForDefault
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

# **get_submissions**
<a id="get_submissions"></a>
> [AssignmentSubmission] get_submissions(_classassignment)

List the students' submissions

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission import AssignmentSubmission
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
    }
    try:
        # List the students' submissions
        api_response = api_instance.get_submissions(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->get_submissions: %s\n" % e)
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
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_submissions.ApiResponseFor200) | The submissions
default | [ApiResponseForDefault](#get_submissions.ApiResponseForDefault) | Error

#### get_submissions.ApiResponseFor200
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
[**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) | [**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) | [**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) |  | 

#### get_submissions.ApiResponseForDefault
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

# **list_assignments**
<a id="list_assignments"></a>
> [ClassAssignment] list_assignments(_class)

Assignments listing

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
    }
    try:
        # Assignments listing
        api_response = api_instance.list_assignments(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->list_assignments: %s\n" % e)
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
class | ModelClassSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_assignments.ApiResponseFor200) | List of assignments for the class
default | [ApiResponseForDefault](#list_assignments.ApiResponseForDefault) | Error

#### list_assignments.ApiResponseFor200
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
[**ClassAssignment**]({{complexTypePrefix}}ClassAssignment.md) | [**ClassAssignment**]({{complexTypePrefix}}ClassAssignment.md) | [**ClassAssignment**]({{complexTypePrefix}}ClassAssignment.md) |  | 

#### list_assignments.ApiResponseForDefault
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

# **list_class_student_submissions**
<a id="list_class_student_submissions"></a>
> [AssignmentSubmission] list_class_student_submissions(_classuser)

List the submissions for a student

Use this method as a teacher to list all the assignment submissions sent by a student of the class 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission import AssignmentSubmission
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'user': "user_example",
    }
    try:
        # List the submissions for a student
        api_response = api_instance.list_class_student_submissions(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->list_class_student_submissions: %s\n" % e)
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
class | ModelClassSchema | | 
user | UserSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_class_student_submissions.ApiResponseFor200) | The list of submissions
default | [ApiResponseForDefault](#list_class_student_submissions.ApiResponseForDefault) | Error

#### list_class_student_submissions.ApiResponseFor200
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
[**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) | [**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) | [**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) |  | 

#### list_class_student_submissions.ApiResponseForDefault
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

# **list_classes**
<a id="list_classes"></a>
> [ClassDetails] list_classes()

List the classes available for the current user

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.class_details import ClassDetails
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only optional values
    query_params = {
        'state': "active",
    }
    try:
        # List the classes available for the current user
        api_response = api_instance.list_classes(
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->list_classes: %s\n" % e)
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
state | StateSchema | | optional


# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["active", "inactive", "archived", ] if omitted the server will use the default value of "active"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_classes.ApiResponseFor200) | The list of classes
default | [ApiResponseForDefault](#list_classes.ApiResponseForDefault) | Error

#### list_classes.ApiResponseFor200
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
[**ClassDetails**]({{complexTypePrefix}}ClassDetails.md) | [**ClassDetails**]({{complexTypePrefix}}ClassDetails.md) | [**ClassDetails**]({{complexTypePrefix}}ClassDetails.md) |  | 

#### list_classes.ApiResponseForDefault
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

# **post_submission_comment**
<a id="post_submission_comment"></a>
> AssignmentSubmissionComment post_submission_comment(_classassignmentsubmissionassignment_submission_comment_creation)

Add a feedback comment to a submission

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission_comment_creation import AssignmentSubmissionCommentCreation
from flat_api.model.assignment_submission_comment import AssignmentSubmissionComment
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
        'submission': "submission_example",
    }
    body = AssignmentSubmissionCommentCreation(
        comment="comment_example",
    )
    try:
        # Add a feedback comment to a submission
        api_response = api_instance.post_submission_comment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->post_submission_comment: %s\n" % e)
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
[**AssignmentSubmissionCommentCreation**](../../models/AssignmentSubmissionCommentCreation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 
submission | SubmissionSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubmissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_submission_comment.ApiResponseFor200) | The comment
403 | [ApiResponseFor403](#post_submission_comment.ApiResponseFor403) | Not granted to access to this submission
404 | [ApiResponseFor404](#post_submission_comment.ApiResponseFor404) | Submission not found
default | [ApiResponseForDefault](#post_submission_comment.ApiResponseForDefault) | Error

#### post_submission_comment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignmentSubmissionComment**](../../models/AssignmentSubmissionComment.md) |  | 


#### post_submission_comment.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### post_submission_comment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### post_submission_comment.ApiResponseForDefault
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

# **unarchive_assignment**
<a id="unarchive_assignment"></a>
> Assignment unarchive_assignment(_classassignment)

Unarchive the assignment.

Mark the assignment as `active`. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
    }
    try:
        # Unarchive the assignment.
        api_response = api_instance.unarchive_assignment(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->unarchive_assignment: %s\n" % e)
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
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#unarchive_assignment.ApiResponseFor200) | The assignment details
default | [ApiResponseForDefault](#unarchive_assignment.ApiResponseForDefault) | Error

#### unarchive_assignment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Assignment**](../../models/Assignment.md) |  | 


#### unarchive_assignment.ApiResponseForDefault
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

# **unarchive_class**
<a id="unarchive_class"></a>
> ClassDetails unarchive_class(_class)

Unarchive the class

Mark the class as `active`. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.class_details import ClassDetails
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
    }
    try:
        # Unarchive the class
        api_response = api_instance.unarchive_class(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->unarchive_class: %s\n" % e)
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
class | ModelClassSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#unarchive_class.ApiResponseFor200) | The class details
default | [ApiResponseForDefault](#unarchive_class.ApiResponseForDefault) | Error

#### unarchive_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassDetails**](../../models/ClassDetails.md) |  | 


#### unarchive_class.ApiResponseForDefault
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

# **update_class**
<a id="update_class"></a>
> ClassDetails update_class(_class)

Update the class

Update the meta information of the class 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.class_details import ClassDetails
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.class_update import ClassUpdate
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
    }
    try:
        # Update the class
        api_response = api_instance.update_class(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->update_class: %s\n" % e)

    # example passing only optional values
    path_params = {
        'class': "class_example",
    }
    body = ClassUpdate(
        name="name_example",
        section="section_example",
        level=ClassGradeLevel("elementary"),
        skills_focused=EduSkillsFocused([
            "notation"
        ]),
        size=0,
    )
    try:
        # Update the class
        api_response = api_instance.update_class(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->update_class: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
[**ClassUpdate**](../../models/ClassUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_class.ApiResponseFor200) | The new class details
default | [ApiResponseForDefault](#update_class.ApiResponseForDefault) | Error

#### update_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassDetails**](../../models/ClassDetails.md) |  | 


#### update_class.ApiResponseForDefault
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

# **update_submission_comment**
<a id="update_submission_comment"></a>
> AssignmentSubmissionComment update_submission_comment(_classassignmentsubmissioncommentassignment_submission_comment_creation)

Update a feedback comment to a submission

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import model_class_api
from flat_api.model.assignment_submission_comment_creation import AssignmentSubmissionCommentCreation
from flat_api.model.assignment_submission_comment import AssignmentSubmissionComment
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
    api_instance = model_class_api.ModelClassApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'class': "class_example",
        'assignment': "assignment_example",
        'submission': "submission_example",
        'comment': "comment_example",
    }
    body = AssignmentSubmissionCommentCreation(
        comment="comment_example",
    )
    try:
        # Update a feedback comment to a submission
        api_response = api_instance.update_submission_comment(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ModelClassApi->update_submission_comment: %s\n" % e)
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
[**AssignmentSubmissionCommentCreation**](../../models/AssignmentSubmissionCommentCreation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
class | ModelClassSchema | | 
assignment | AssignmentSchema | | 
submission | SubmissionSchema | | 
comment | CommentSchema | | 

# ModelClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubmissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CommentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_submission_comment.ApiResponseFor200) | The comment
403 | [ApiResponseFor403](#update_submission_comment.ApiResponseFor403) | Not granted to access to this submission
404 | [ApiResponseFor404](#update_submission_comment.ApiResponseFor404) | Submission not found
default | [ApiResponseForDefault](#update_submission_comment.ApiResponseForDefault) | Error

#### update_submission_comment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignmentSubmissionComment**](../../models/AssignmentSubmissionComment.md) |  | 


#### update_submission_comment.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### update_submission_comment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### update_submission_comment.ApiResponseForDefault
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

