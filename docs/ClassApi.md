# flat_api.ClassApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_class**](ClassApi.md#activate_class) | **POST** /classes/{class}/activate | Activate the class
[**add_class_user**](ClassApi.md#add_class_user) | **PUT** /classes/{class}/users/{user} | Add a user to the class
[**archive_assignment**](ClassApi.md#archive_assignment) | **POST** /classes/{class}/assignments/{assignment}/archive | Archive the assignment
[**archive_class**](ClassApi.md#archive_class) | **POST** /classes/{class}/archive | Archive the class
[**copy_assignment**](ClassApi.md#copy_assignment) | **POST** /classes/{class}/assignments/{assignment}/copy | Copy an assignment
[**create_class**](ClassApi.md#create_class) | **POST** /classes | Create a new class
[**create_class_assignment**](ClassApi.md#create_class_assignment) | **POST** /classes/{class}/assignments | Assignment creation
[**create_submission**](ClassApi.md#create_submission) | **PUT** /classes/{class}/assignments/{assignment}/submissions | Create or edit a submission
[**create_test_student_account**](ClassApi.md#create_test_student_account) | **POST** /classes/{class}/testStudent | Create a test student account
[**delete_class_user**](ClassApi.md#delete_class_user) | **DELETE** /classes/{class}/users/{user} | Remove a user from the class
[**delete_submission**](ClassApi.md#delete_submission) | **DELETE** /classes/{class}/assignments/{assignment}/submissions/{submission} | Reset a submission
[**delete_submission_comment**](ClassApi.md#delete_submission_comment) | **DELETE** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Delete a feedback comment to a submission
[**edit_submission**](ClassApi.md#edit_submission) | **PUT** /classes/{class}/assignments/{assignment}/submissions/{submission} | Edit a submission
[**enroll_class**](ClassApi.md#enroll_class) | **POST** /classes/enroll/{enrollmentCode} | Join a class
[**export_submissions_reviews_as_csv**](ClassApi.md#export_submissions_reviews_as_csv) | **GET** /classes/{class}/assignments/{assignment}/submissions/csv | CSV Grades exports
[**export_submissions_reviews_as_excel**](ClassApi.md#export_submissions_reviews_as_excel) | **GET** /classes/{class}/assignments/{assignment}/submissions/excel | Excel Grades exports
[**get_class**](ClassApi.md#get_class) | **GET** /classes/{class} | Get the details of a single class
[**get_score_submissions**](ClassApi.md#get_score_submissions) | **GET** /scores/{score}/submissions | List submissions related to the score
[**get_submission**](ClassApi.md#get_submission) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission} | Get a student submission
[**get_submission_comments**](ClassApi.md#get_submission_comments) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | List the feedback comments of a submission
[**get_submission_history**](ClassApi.md#get_submission_history) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission}/history | Get the history of the submission
[**get_submissions**](ClassApi.md#get_submissions) | **GET** /classes/{class}/assignments/{assignment}/submissions | List the students&#39; submissions
[**list_assignments**](ClassApi.md#list_assignments) | **GET** /classes/{class}/assignments | Assignments listing
[**list_class_student_submissions**](ClassApi.md#list_class_student_submissions) | **GET** /classes/{class}/students/{user}/submissions | List the submissions for a student
[**list_classes**](ClassApi.md#list_classes) | **GET** /classes | List the classes available for the current user
[**post_submission_comment**](ClassApi.md#post_submission_comment) | **POST** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | Add a feedback comment to a submission
[**unarchive_assignment**](ClassApi.md#unarchive_assignment) | **DELETE** /classes/{class}/assignments/{assignment}/archive | Unarchive the assignment.
[**unarchive_class**](ClassApi.md#unarchive_class) | **DELETE** /classes/{class}/archive | Unarchive the class
[**update_class**](ClassApi.md#update_class) | **PUT** /classes/{class} | Update the class
[**update_submission_comment**](ClassApi.md#update_submission_comment) | **PUT** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Update a feedback comment to a submission


# **activate_class**
> ClassDetails activate_class(_class)

Activate the class

Mark the class as `active`. This is mainly used for classes synchronized from Clever that are initially with an `inactive` state and hidden in the UI. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class

    # example passing only required values which don't have defaults set
    try:
        # Activate the class
        api_response = api_instance.activate_class(_class)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->activate_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The class details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_class_user**
> add_class_user(_class, user)

Add a user to the class

This method can be used by a teacher of the class to enroll another Flat user into the class.  Only users that are part of your Organization can be enrolled in a class of this same Organization.  When enrolling a user in the class, Flat will automatically add this user to the corresponding Class group, based on this role in the Organization. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    user = "user_example" # str | Unique identifier of the user

    # example passing only required values which don't have defaults set
    try:
        # Add a user to the class
        api_instance.add_class_user(_class, user)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->add_class_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **user** | **str**| Unique identifier of the user |

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
**204** | The user has been added to the class |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_assignment**
> Assignment archive_assignment(_class, assignment)

Archive the assignment

Archive the assignment 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment

    # example passing only required values which don't have defaults set
    try:
        # Archive the assignment
        api_response = api_instance.archive_assignment(_class, assignment)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->archive_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The assignment details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_class**
> ClassDetails archive_class(_class)

Archive the class

Mark the class as `archived`. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class

    # example passing only required values which don't have defaults set
    try:
        # Archive the class
        api_response = api_instance.archive_class(_class)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->archive_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The class details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_assignment**
> AssignmentCopyResponse copy_assignment(_class, assignment, body)

Copy an assignment

Copy an assignment to a specified class or the resource library  For class assignments: - If the original assignment has a due date in the past, this new assignment will be created without a due date. - If the class is synchronized with an external app (e.g. Google Classroom), the copied assignment will also be posted on the external app. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    body = AssignmentCopy(
        classroom="classroom_example",
        assignment="assignment_example",
        scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        library_parent="library_parent_example",
    ) # AssignmentCopy | 

    # example passing only required values which don't have defaults set
    try:
        # Copy an assignment
        api_response = api_instance.copy_assignment(_class, assignment, body)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->copy_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **body** | [**AssignmentCopy**](AssignmentCopy.md)|  |

### Return type

[**AssignmentCopyResponse**](AssignmentCopyResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new created assignment |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_class**
> ClassDetails create_class(body)

Create a new class

Classrooms on Flat allow you to create activities with assignments and post content to a specific group.  When creating a class, Flat automatically creates two groups: one for the teachers of the course, one for the students. The creator of this class is automatically added to the teachers group.  If the classsroom is synchronized with another application like Google Classroom, some of the meta information will automatically be updated.  You can add users to this class using `PUT /classes/{class}/users/{user}`, they will automatically added to the group based on their role on Flat. Users can also enroll themselves to this class using `POST /classes/enroll/{enrollmentCode}` and the `enrollmentCode` returned in the `ClassDetails` response. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    body = ClassCreation(
        name="name_example",
        section="section_example",
        level=ClassGradeLevel("elementary"),
        skills_focused=EduSkillsFocused([
            "notation",
        ]),
        size=0,
    ) # ClassCreation | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new class
        api_response = api_instance.create_class(body)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->create_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClassCreation**](ClassCreation.md)|  |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new class details |  -  |
**402** | Account overquota |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_class_assignment**
> Assignment create_class_assignment(_class)

Assignment creation

Use this method as a teacher to create and post a new assignment to a class.  If the class is synchronized with Google Classroom, the assignment will be automatically posted to your Classroom course. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
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
            ),
        ],
        nb_playback_authorized=3.14,
        toolset="toolset_example",
        cover_file="cover_file_example",
        cover="cover_example",
        max_points=0,
        release_grades="auto",
        shuffle_exercises=True,
        state="draft",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        google_classroom=ClassAssignmentUpdateGoogleClassroom(
            topic_id="topic_id_example",
        ),
        microsoft_graph=ClassAssignmentUpdateMicrosoftGraph(
            categories=[
                "categories_example",
            ],
        ),
        assignee_mode="everyone",
        assigned_students=[
            "assigned_students_example",
        ],
    ) # ClassAssignmentUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Assignment creation
        api_response = api_instance.create_class_assignment(_class)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->create_class_assignment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Assignment creation
        api_response = api_instance.create_class_assignment(_class, body=body)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->create_class_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **body** | [**ClassAssignmentUpdate**](ClassAssignmentUpdate.md)|  | [optional]

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
**200** | The assignment has been created |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_submission**
> AssignmentSubmission create_submission(_class, assignment, body)

Create or edit a submission

Use this method as a student to create, update and submit a submission related to an assignment. Students can only set `attachments` and `submit`. Teachers can use `PUT /classes/{class}/assignments/{assignment}/submissions/{submission}` to update a submission by id. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
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
            ),
        ],
        submit=True,
        draft_grade=0,
        grade=0,
        exercises_ids=[
            "exercises_ids_example",
        ],
        _return=True,
        comments=AssignmentSubmissionUpdateComments(
            total=3.14,
            unread=3.14,
        ),
    ) # AssignmentSubmissionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Create or edit a submission
        api_response = api_instance.create_submission(_class, assignment, body)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->create_submission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **body** | [**AssignmentSubmissionUpdate**](AssignmentSubmissionUpdate.md)|  |

### Return type

[**AssignmentSubmission**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The submission |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_student_account**
> UserDetails create_test_student_account(_class)

Create a test student account

Test students account can be created by teachers an admin and be used to experiment the assignments.  - They are automatically added to the class. - They can be reset using this API endpoint (a new account will be created and the previous one scheduled for deletion). - These accounts don't use a user license. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    reset = True # bool | If true, the testing account will be re-created.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a test student account
        api_response = api_instance.create_test_student_account(_class)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->create_test_student_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a test student account
        api_response = api_instance.create_test_student_account(_class, reset=reset)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->create_test_student_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **reset** | **bool**| If true, the testing account will be re-created.  | [optional]

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test account created |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_class_user**
> delete_class_user(_class, user)

Remove a user from the class

This method can be used by a teacher to remove a user from the class, or by a student to leave the classroom.  Warning: Removing a user from the class will remove the associated resources, including the submissions and feedback related to these submissions. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    user = "user_example" # str | Unique identifier of the user

    # example passing only required values which don't have defaults set
    try:
        # Remove a user from the class
        api_instance.delete_class_user(_class, user)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->delete_class_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **user** | **str**| Unique identifier of the user |

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
**204** | The user has been removed from the class |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_submission**
> AssignmentSubmission delete_submission(_class, assignment, submission)

Reset a submission

Use this method as a teacher to reset a submission and allow student to start over the assignment 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    submission = "submission_example" # str | Unique identifier of the submission

    # example passing only required values which don't have defaults set
    try:
        # Reset a submission
        api_response = api_instance.delete_submission(_class, assignment, submission)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->delete_submission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **submission** | **str**| Unique identifier of the submission |

### Return type

[**AssignmentSubmission**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The submission object once reset |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_submission_comment**
> delete_submission_comment(_class, assignment, submission, comment)

Delete a feedback comment to a submission

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    submission = "submission_example" # str | Unique identifier of the submission
    comment = "comment_example" # str | Unique identifier of the comment

    # example passing only required values which don't have defaults set
    try:
        # Delete a feedback comment to a submission
        api_instance.delete_submission_comment(_class, assignment, submission, comment)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->delete_submission_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **submission** | **str**| Unique identifier of the submission |
 **comment** | **str**| Unique identifier of the comment |

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
**204** | The comment has been deleted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_submission**
> AssignmentSubmission edit_submission(_class, assignment, submission, body)

Edit a submission

Use this method as a teacher to update the different submission and give feedback. Teachers can only set `return`, `draftGrade` and `grade` 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    submission = "submission_example" # str | Unique identifier of the submission
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
            ),
        ],
        submit=True,
        draft_grade=0,
        grade=0,
        exercises_ids=[
            "exercises_ids_example",
        ],
        _return=True,
        comments=AssignmentSubmissionUpdateComments(
            total=3.14,
            unread=3.14,
        ),
    ) # AssignmentSubmissionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Edit a submission
        api_response = api_instance.edit_submission(_class, assignment, submission, body)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->edit_submission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **submission** | **str**| Unique identifier of the submission |
 **body** | [**AssignmentSubmissionUpdate**](AssignmentSubmissionUpdate.md)|  |

### Return type

[**AssignmentSubmission**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The submission |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_class**
> ClassDetails enroll_class(enrollment_code)

Join a class

Use this method to join a class using an enrollment code given one of the teacher of this class. This code is also available in the `ClassDetails` returned to the teachers when creating the class or listing / fetching a specific class.  Flat will automatically add the user to the corresponding class group based on this role in the organization. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    enrollment_code = "enrollmentCode_example" # str | The enrollment code, available to the teacher in `ClassDetails` 

    # example passing only required values which don't have defaults set
    try:
        # Join a class
        api_response = api_instance.enroll_class(enrollment_code)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->enroll_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_code** | **str**| The enrollment code, available to the teacher in &#x60;ClassDetails&#x60;  |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new class details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_submissions_reviews_as_csv**
> file_type export_submissions_reviews_as_csv(_class, assignment)

CSV Grades exports

Export list of submissions grades to a CSV file

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment

    # example passing only required values which don't have defaults set
    try:
        # CSV Grades exports
        api_response = api_instance.export_submissions_reviews_as_csv(_class, assignment)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->export_submissions_reviews_as_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |

### Return type

**file_type**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of submissions |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_submissions_reviews_as_excel**
> file_type export_submissions_reviews_as_excel(_class, assignment)

Excel Grades exports

Export list of submissions grades to an Excel file

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment

    # example passing only required values which don't have defaults set
    try:
        # Excel Grades exports
        api_response = api_instance.export_submissions_reviews_as_excel(_class, assignment)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->export_submissions_reviews_as_excel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |

### Return type

**file_type**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of submissions |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_class**
> ClassDetails get_class(_class)

Get the details of a single class

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a single class
        api_response = api_instance.get_class(_class)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->get_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new class details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_submissions**
> [AssignmentSubmission] get_score_submissions(score)

List submissions related to the score

This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    score = "score_example" # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 

    # example passing only required values which don't have defaults set
    try:
        # List submissions related to the score
        api_response = api_instance.get_score_submissions(score)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->get_score_submissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  |

### Return type

[**[AssignmentSubmission]**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of submissions |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission**
> AssignmentSubmission get_submission(_class, assignment, submission)

Get a student submission

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    submission = "submission_example" # str | Unique identifier of the submission

    # example passing only required values which don't have defaults set
    try:
        # Get a student submission
        api_response = api_instance.get_submission(_class, assignment, submission)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->get_submission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **submission** | **str**| Unique identifier of the submission |

### Return type

[**AssignmentSubmission**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A submission |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission_comments**
> [AssignmentSubmissionComment] get_submission_comments(_class, assignment, submission)

List the feedback comments of a submission

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    submission = "submission_example" # str | Unique identifier of the submission

    # example passing only required values which don't have defaults set
    try:
        # List the feedback comments of a submission
        api_response = api_instance.get_submission_comments(_class, assignment, submission)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->get_submission_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **submission** | **str**| Unique identifier of the submission |

### Return type

[**[AssignmentSubmissionComment]**](AssignmentSubmissionComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The comments of the score |  -  |
**403** | Not granted to access to this submission |  -  |
**404** | Submission not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission_history**
> [AssignmentSubmissionHistory] get_submission_history(_class, assignment, submission)

Get the history of the submission

For teachers only. Returns a detailed history of the submission. This currently includes state and grade histories. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    submission = "submission_example" # str | Unique identifier of the submission

    # example passing only required values which don't have defaults set
    try:
        # Get the history of the submission
        api_response = api_instance.get_submission_history(_class, assignment, submission)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->get_submission_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **submission** | **str**| Unique identifier of the submission |

### Return type

[**[AssignmentSubmissionHistory]**](AssignmentSubmissionHistory.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The history of the submission |  -  |
**403** | Not granted to access to this submission |  -  |
**404** | Submission not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submissions**
> [AssignmentSubmission] get_submissions(_class, assignment)

List the students' submissions

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment

    # example passing only required values which don't have defaults set
    try:
        # List the students' submissions
        api_response = api_instance.get_submissions(_class, assignment)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->get_submissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |

### Return type

[**[AssignmentSubmission]**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The submissions |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> [ClassAssignment] list_assignments(_class)

Assignments listing

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class

    # example passing only required values which don't have defaults set
    try:
        # Assignments listing
        api_response = api_instance.list_assignments(_class)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->list_assignments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |

### Return type

[**[ClassAssignment]**](ClassAssignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assignments for the class |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_class_student_submissions**
> [AssignmentSubmission] list_class_student_submissions(_class, user)

List the submissions for a student

Use this method as a teacher to list all the assignment submissions sent by a student of the class 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    user = "user_example" # str | Unique identifier of the user

    # example passing only required values which don't have defaults set
    try:
        # List the submissions for a student
        api_response = api_instance.list_class_student_submissions(_class, user)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->list_class_student_submissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **user** | **str**| Unique identifier of the user |

### Return type

[**[AssignmentSubmission]**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of submissions |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_classes**
> [ClassDetails] list_classes()

List the classes available for the current user

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    state = "active" # str | Filter the classes by state (optional) if omitted the server will use the default value of "active"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the classes available for the current user
        api_response = api_instance.list_classes(state=state)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->list_classes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Filter the classes by state | [optional] if omitted the server will use the default value of "active"

### Return type

[**[ClassDetails]**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of classes |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submission_comment**
> AssignmentSubmissionComment post_submission_comment(_class, assignment, submission, assignment_submission_comment_creation)

Add a feedback comment to a submission

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    submission = "submission_example" # str | Unique identifier of the submission
    assignment_submission_comment_creation = AssignmentSubmissionCommentCreation(
        comment="comment_example",
    ) # AssignmentSubmissionCommentCreation | 

    # example passing only required values which don't have defaults set
    try:
        # Add a feedback comment to a submission
        api_response = api_instance.post_submission_comment(_class, assignment, submission, assignment_submission_comment_creation)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->post_submission_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **submission** | **str**| Unique identifier of the submission |
 **assignment_submission_comment_creation** | [**AssignmentSubmissionCommentCreation**](AssignmentSubmissionCommentCreation.md)|  |

### Return type

[**AssignmentSubmissionComment**](AssignmentSubmissionComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The comment |  -  |
**403** | Not granted to access to this submission |  -  |
**404** | Submission not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_assignment**
> Assignment unarchive_assignment(_class, assignment)

Unarchive the assignment.

Mark the assignment as `active`. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment

    # example passing only required values which don't have defaults set
    try:
        # Unarchive the assignment.
        api_response = api_instance.unarchive_assignment(_class, assignment)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->unarchive_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The assignment details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_class**
> ClassDetails unarchive_class(_class)

Unarchive the class

Mark the class as `active`. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class

    # example passing only required values which don't have defaults set
    try:
        # Unarchive the class
        api_response = api_instance.unarchive_class(_class)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->unarchive_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The class details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_class**
> ClassDetails update_class(_class)

Update the class

Update the meta information of the class 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    body = ClassUpdate(
        name="name_example",
        section="section_example",
        level=ClassGradeLevel("elementary"),
        skills_focused=EduSkillsFocused([
            "notation",
        ]),
        size=0,
    ) # ClassUpdate | Details of the Class (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the class
        api_response = api_instance.update_class(_class)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->update_class: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the class
        api_response = api_instance.update_class(_class, body=body)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->update_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **body** | [**ClassUpdate**](ClassUpdate.md)| Details of the Class | [optional]

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new class details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_submission_comment**
> AssignmentSubmissionComment update_submission_comment(_class, assignment, submission, comment, assignment_submission_comment_creation)

Update a feedback comment to a submission

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import class_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_api.ClassApi(api_client)
    _class = "class_example" # str | Unique identifier of the class
    assignment = "assignment_example" # str | Unique identifier of the assignment
    submission = "submission_example" # str | Unique identifier of the submission
    comment = "comment_example" # str | Unique identifier of the comment
    assignment_submission_comment_creation = AssignmentSubmissionCommentCreation(
        comment="comment_example",
    ) # AssignmentSubmissionCommentCreation | 

    # example passing only required values which don't have defaults set
    try:
        # Update a feedback comment to a submission
        api_response = api_instance.update_submission_comment(_class, assignment, submission, comment, assignment_submission_comment_creation)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ClassApi->update_submission_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class |
 **assignment** | **str**| Unique identifier of the assignment |
 **submission** | **str**| Unique identifier of the submission |
 **comment** | **str**| Unique identifier of the comment |
 **assignment_submission_comment_creation** | [**AssignmentSubmissionCommentCreation**](AssignmentSubmissionCommentCreation.md)|  |

### Return type

[**AssignmentSubmissionComment**](AssignmentSubmissionComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The comment |  -  |
**403** | Not granted to access to this submission |  -  |
**404** | Submission not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

