# flat_api.ClassApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_class**](ClassApi.md#activate_class) | **POST** /classes/{class}/activate | Activate the class
[**add_class_user**](ClassApi.md#add_class_user) | **PUT** /classes/{class}/users/{user} | Add a user to the class
[**archive_class**](ClassApi.md#archive_class) | **POST** /classes/{class}/archive | Archive the class
[**copy_assignment**](ClassApi.md#copy_assignment) | **POST** /classes/{class}/assignments/{assignment}/copy | Copy an assignment
[**create_assignment**](ClassApi.md#create_assignment) | **POST** /classes/{class}/assignments | Assignment creation
[**create_class**](ClassApi.md#create_class) | **POST** /classes | Create a new class
[**create_submission**](ClassApi.md#create_submission) | **PUT** /classes/{class}/assignments/{assignment}/submissions | Create or edit a submission
[**delete_class_user**](ClassApi.md#delete_class_user) | **DELETE** /classes/{class}/users/{user} | Remove a user from the class
[**edit_submission**](ClassApi.md#edit_submission) | **PUT** /classes/{class}/assignments/{assignment}/submissions/{submission} | Edit a submission
[**enroll_class**](ClassApi.md#enroll_class) | **POST** /classes/enroll/{enrollmentCode} | Join a class
[**get_class**](ClassApi.md#get_class) | **GET** /classes/{class} | Get the details of a single class
[**get_score_submissions**](ClassApi.md#get_score_submissions) | **GET** /scores/{score}/submissions | List submissions related to the score
[**get_submission**](ClassApi.md#get_submission) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission} | Get a student submission
[**get_submissions**](ClassApi.md#get_submissions) | **GET** /classes/{class}/assignments/{assignment}/submissions | List the students&#39; submissions
[**list_assignments**](ClassApi.md#list_assignments) | **GET** /classes/{class}/assignments | Assignments listing
[**list_class_student_submissions**](ClassApi.md#list_class_student_submissions) | **GET** /classes/{class}/students/{user}/submissions | List the submissions for a student
[**list_classes**](ClassApi.md#list_classes) | **GET** /classes | List the classes available for the current user
[**unarchive_class**](ClassApi.md#unarchive_class) | **DELETE** /classes/{class}/archive | Unarchive the class
[**update_class**](ClassApi.md#update_class) | **PUT** /classes/{class} | Update the class


# **activate_class**
> ClassDetails activate_class(_class)

Activate the class

Mark the class as `active`. This is mainly used for classes synchronized from Clever that are initially with an `inactive` state and hidden in the UI. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class

try:
    # Activate the class
    api_response = api_instance.activate_class(_class)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_class_user**
> add_class_user(_class, user)

Add a user to the class

This method can be used by a teacher of the class to enroll another Flat user into the class.  Only users that are part of your Organization can be enrolled in a class of this same Organization.  When enrolling a user in the class, Flat will automatically add this user to the corresponding Class group, based on this role in the Organization. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
user = 'user_example' # str | Unique identifier of the user

try:
    # Add a user to the class
    api_instance.add_class_user(_class, user)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_class**
> ClassDetails archive_class(_class)

Archive the class

Mark the class as `archived`. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class

try:
    # Archive the class
    api_response = api_instance.archive_class(_class)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_assignment**
> Assignment copy_assignment(_class, assignment, body)

Copy an assignment

Copy an assignment to a specified class.  If the original assignment has a due date in the past, this new assingment will be created without a due date.  If the new class is synchronized with an external app (e.g. Google Classroom), the copied assignment will also be posted on the external app. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
assignment = 'assignment_example' # str | Unique identifier of the assignment
body = flat_api.AssignmentCopy() # AssignmentCopy | 

try:
    # Copy an assignment
    api_response = api_instance.copy_assignment(_class, assignment, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassApi->copy_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class | 
 **assignment** | **str**| Unique identifier of the assignment | 
 **body** | [**AssignmentCopy**](AssignmentCopy.md)|  | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_assignment**
> Assignment create_assignment(_class, body=body)

Assignment creation

Use this method as a teacher to create and post a new assignment to a class.  If the class is synchronized with Google Classroom, the assignment will be automatically posted to your Classroom course. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
body = flat_api.AssignmentCreation() # AssignmentCreation |  (optional)

try:
    # Assignment creation
    api_response = api_instance.create_assignment(_class, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassApi->create_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class | 
 **body** | [**AssignmentCreation**](AssignmentCreation.md)|  | [optional] 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_class**
> ClassDetails create_class(body)

Create a new class

Classrooms on Flat allow you to create activities with assignments and post content to a specific group.  When creating a class, Flat automatically creates two groups: one for the teachers of the course, one for the students. The creator of this class is automatically added to the teachers group.  If the classsroom is synchronized with another application like Google Classroom, some of the meta information will automatically be updated.  You can add users to this class using `POST /classes/{class}/users/{user}`, they will automatically added to the group based on their role on Flat. Users can also enroll themselves to this class using `POST /classes/enroll/{enrollmentCode}` and the `enrollmentCode` returned in the `ClassDetails` response. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
body = flat_api.ClassCreation() # ClassCreation | 

try:
    # Create a new class
    api_response = api_instance.create_class(body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_submission**
> AssignmentSubmission create_submission(_class, assignment, body)

Create or edit a submission

Use this method as a student to create, update and submit a submission related to an assignment. Students can only set `attachments`, `studentComment` and `submit`.  Teachers can use `PUT /classes/{class}/assignments/{assignment}/submissions/{submission}` to update a submission by id. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
assignment = 'assignment_example' # str | Unique identifier of the assignment
body = flat_api.AssignmentSubmissionUpdate() # AssignmentSubmissionUpdate | 

try:
    # Create or edit a submission
    api_response = api_instance.create_submission(_class, assignment, body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_class_user**
> delete_class_user(_class, user)

Remove a user from the class

This method can be used by a teacher to remove a user from the class, or by a student to leave the classroom.  Warning: Removing a user from the class will remove the associated resources, including the submissions and feedback related to these submissions. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
user = 'user_example' # str | Unique identifier of the user

try:
    # Remove a user from the class
    api_instance.delete_class_user(_class, user)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_submission**
> AssignmentSubmission edit_submission(_class, assignment, submission, body)

Edit a submission

Use this method as a teacher to update the different submission and give feedback. Teachers can only set `returnFeedback` 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
assignment = 'assignment_example' # str | Unique identifier of the assignment
submission = 'submission_example' # str | Unique identifier of the submission
body = flat_api.AssignmentSubmissionUpdate() # AssignmentSubmissionUpdate | 

try:
    # Edit a submission
    api_response = api_instance.edit_submission(_class, assignment, submission, body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_class**
> ClassDetails enroll_class(enrollment_code)

Join a class

Use this method to join a class using an enrollment code given one of the teacher of this class. This code is also available in the `ClassDetails` returned to the teachers when creating the class or listing / fetching a specific class.  Flat will automatically add the user to the corresponding class group based on this role in the organization. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
enrollment_code = 'enrollment_code_example' # str | The enrollment code, available to the teacher in `ClassDetails` 

try:
    # Join a class
    api_response = api_instance.enroll_class(enrollment_code)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_class**
> ClassDetails get_class(_class)

Get the details of a single class

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class

try:
    # Get the details of a single class
    api_response = api_instance.get_class(_class)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_submissions**
> list[AssignmentSubmission] get_score_submissions(score)

List submissions related to the score

This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 

try:
    # List submissions related to the score
    api_response = api_instance.get_score_submissions(score)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassApi->get_score_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 

### Return type

[**list[AssignmentSubmission]**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission**
> AssignmentSubmission get_submission(_class, assignment, submission)

Get a student submission

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
assignment = 'assignment_example' # str | Unique identifier of the assignment
submission = 'submission_example' # str | Unique identifier of the submission

try:
    # Get a student submission
    api_response = api_instance.get_submission(_class, assignment, submission)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submissions**
> list[AssignmentSubmission] get_submissions(_class, assignment)

List the students' submissions

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
assignment = 'assignment_example' # str | Unique identifier of the assignment

try:
    # List the students' submissions
    api_response = api_instance.get_submissions(_class, assignment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassApi->get_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class | 
 **assignment** | **str**| Unique identifier of the assignment | 

### Return type

[**list[AssignmentSubmission]**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> list[Assignment] list_assignments(_class)

Assignments listing

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class

try:
    # Assignments listing
    api_response = api_instance.list_assignments(_class)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassApi->list_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class | 

### Return type

[**list[Assignment]**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_class_student_submissions**
> list[AssignmentSubmission] list_class_student_submissions(_class, user)

List the submissions for a student

Use this method as a teacher to list all the assignment submissions sent by a student of the class 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
user = 'user_example' # str | Unique identifier of the user

try:
    # List the submissions for a student
    api_response = api_instance.list_class_student_submissions(_class, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassApi->list_class_student_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_class** | **str**| Unique identifier of the class | 
 **user** | **str**| Unique identifier of the user | 

### Return type

[**list[AssignmentSubmission]**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_classes**
> list[ClassDetails] list_classes(state=state)

List the classes available for the current user

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
state = 'active' # str | Filter the classes by state (optional) (default to active)

try:
    # List the classes available for the current user
    api_response = api_instance.list_classes(state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassApi->list_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Filter the classes by state | [optional] [default to active]

### Return type

[**list[ClassDetails]**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_class**
> ClassDetails unarchive_class(_class)

Unarchive the class

Mark the class as `active`. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class

try:
    # Unarchive the class
    api_response = api_instance.unarchive_class(_class)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_class**
> ClassDetails update_class(_class, body=body)

Update the class

Update the meta information of the class 

### Example
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
api_instance = flat_api.ClassApi(flat_api.ApiClient(configuration))
_class = '_class_example' # str | Unique identifier of the class
body = flat_api.ClassUpdate() # ClassUpdate | Details of the Class (optional)

try:
    # Update the class
    api_response = api_instance.update_class(_class, body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

