# flat_api.model.class_assignment.ClassAssignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of the assignment | [optional] 
**type** | [**AssignmentType**](AssignmentType.md) | [**AssignmentType**](AssignmentType.md) |  | [optional] 
**[capabilities](#capabilities)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Capabilities the current user has on this assignment. Each capability corresponds to a fine-grained action that a user may take. | [optional] 
**title** | str,  | str,  | Title of the assignment | [optional] 
**description** | str,  | str,  | Description and content of the assignment | [optional] 
**cover** | str,  | str,  | The URL of the cover to display | [optional] 
**coverFile** | str,  | str,  | The id of the cover to display | [optional] 
**[attachments](#attachments)** | list, tuple,  | tuple,  |  | [optional] 
**useDedicatedAttachments** | bool,  | BoolClass,  | For all assignments created after 02/2023, all the underlying resources must be dedicated and stored in the assignment. This boolean indicates that this assignment only supports dedicated attachments.  | [optional] 
**maxPoints** | decimal.Decimal, int, float,  | decimal.Decimal,  | If set, the grading will be enabled for the assignement  | [optional] 
**releaseGrades** | str,  | str,  | For worksheets, how grading will work for the assignment: - If set to &#x60;auto&#x60;, the grades will be automatically released when the student submits the submissions - If set to &#x60;manual&#x60;, the grades will only be set as &#x60;draftGrade&#x60; and will be released when the teacher returns the submissions  | [optional] must be one of ["auto", "manual", ] 
**shuffleExercises** | bool,  | BoolClass,  | Mixing worksheets exercises for each student | [optional] 
**toolset** | str,  | str,  | The id of the associated toolset | [optional] 
**nbPlaybackAuthorized** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of playback authorized on the scores of the assignment. | [optional] 
**creator** | str,  | str,  | The User unique identifier of the creator of this assignment  | [optional] 
**state** | str,  | str,  | State of the assignment | [optional] must be one of ["draft", "active", "archived", ] 
**classroom** | str,  | str,  | The unique identifier of the class where this assignment was posted | [optional] 
**creationDate** | str, datetime,  | str,  | The creation date of this assignment | [optional] value must conform to RFC-3339 date-time
**scheduledDate** | str, datetime,  | str,  | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  | [optional] value must conform to RFC-3339 date-time
**dueDate** | str, datetime,  | str,  | The due date of this assignment, late submissions will be marked as paste due.  | [optional] value must conform to RFC-3339 date-time
**assigneeMode** | str,  | str,  | Possible modes of assigning assignments | [optional] must be one of ["everyone", "selected", ] 
**[assignedStudents](#assignedStudents)** | list, tuple,  | tuple,  | Identifiers for the students that have access to the assignment | [optional] 
**[submissions](#submissions)** | list, tuple,  | tuple,  |  | [optional] 
**googleClassroom** | [**GoogleClassroomCoursework**](GoogleClassroomCoursework.md) | [**GoogleClassroomCoursework**](GoogleClassroomCoursework.md) |  | [optional] 
**microsoftGraph** | [**MicrosoftGraphAssignment**](MicrosoftGraphAssignment.md) | [**MicrosoftGraphAssignment**](MicrosoftGraphAssignment.md) |  | [optional] 
**[mfc](#mfc)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A MusicFirst Classroom assignment | [optional] 
**[canvas](#canvas)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A Canvas LMS assignment | [optional] 
**[lti](#lti)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An LTI assignment | [optional] 
**issue** | str,  | str,  | Detected issue for this assignment | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# capabilities

Capabilities the current user has on this assignment. Each capability corresponds to a fine-grained action that a user may take.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Capabilities the current user has on this assignment. Each capability corresponds to a fine-grained action that a user may take. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**canArchive** | bool,  | BoolClass,  | Whether the current user can archive the assignment  | 
**canPublishInClass** | bool,  | BoolClass,  | Whether this assignment can be published in a class  | 
**canUnarchive** | bool,  | BoolClass,  | Whether the current user can unarchive the assignment  | 
**canEdit** | bool,  | BoolClass,  | Whether the current user can edit the assignment  | 
**[canPublishInClassError](#canPublishInClassError)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | If &#x60;canPublishInClass&#x60; and &#x60;canEdit&#x60; are false, the issue why this assignment cannot be published in a class  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# canPublishInClassError

If `canPublishInClass` and `canEdit` are false, the issue why this assignment cannot be published in a class 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | If &#x60;canPublishInClass&#x60; and &#x60;canEdit&#x60; are false, the issue why this assignment cannot be published in a class  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | A corresponding code for this error | 
**message** | str,  | str,  | A printable and localized message for this error | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MediaAttachment**](MediaAttachment.md) | [**MediaAttachment**](MediaAttachment.md) | [**MediaAttachment**](MediaAttachment.md) |  | 

# assignedStudents

Identifiers for the students that have access to the assignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers for the students that have access to the assignment | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# submissions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AssignmentSubmission**](AssignmentSubmission.md) | [**AssignmentSubmission**](AssignmentSubmission.md) | [**AssignmentSubmission**](AssignmentSubmission.md) |  | 

# mfc

A MusicFirst Classroom assignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A MusicFirst Classroom assignment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of the course on MusicFirst Task | [optional] 
**alternateLink** | str,  | str,  | Link to MusicFirst Classroom task | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# canvas

A Canvas LMS assignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Canvas LMS assignment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of the course on Canvas assignment | [optional] 
**alternateLink** | str,  | str,  | Link to Canvas assignment | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lti

An LTI assignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An LTI assignment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Resource ID in the LMS | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

