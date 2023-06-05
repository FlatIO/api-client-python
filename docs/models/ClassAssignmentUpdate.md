# flat_api.model.class_assignment_update.ClassAssignmentUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | [**AssignmentType**](AssignmentType.md) | [**AssignmentType**](AssignmentType.md) |  | [optional] 
**title** | str,  | str,  | Title of the assignment | [optional] 
**description** | str,  | str,  | Description and content of the assignment | [optional] 
**[attachments](#attachments)** | list, tuple,  | tuple,  |  | [optional] 
**nbPlaybackAuthorized** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The number of playback authorized on the scores of the assignment. | [optional] 
**toolset** | None, str,  | NoneClass, str,  | The id of the toolset to apply to this assignment. The toolset will be copied to the assignment as a dedicated object to prevent unexpected changes when making modifications to the template toolset. This property can be set to null to delete the linked toolset and switch back to all the tools available for this assignment.  | [optional] 
**coverFile** | None, str,  | NoneClass, str,  | The id of the cover to display | [optional] 
**cover** | None, str,  | NoneClass, str,  | The URL of the cover to display | [optional] 
**maxPoints** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | If set, the grading will be enabled for the assignement with this value as the maximum of points  | [optional] 
**releaseGrades** | str,  | str,  | For worksheets, how grading will work for the assignment: - If set to &#x60;auto&#x60;, the grades will be automatically released when the student submits the submissions - If set to &#x60;manual&#x60;, the grades will only be set as &#x60;draftGrade&#x60; and will be released when the teacher returns the submissions  | [optional] must be one of ["auto", "manual", ] 
**shuffleExercises** | bool,  | BoolClass,  | Mixing worksheets exercises for each student | [optional] 
**state** | str,  | str,  | State of the assignment | [optional] must be one of ["draft", "active", ] 
**dueDate** | None, str, datetime,  | NoneClass, str,  | The due date of this assignment, late submissions will be marked as paste due. If not set, the assignment won&#x27;t have a due date.  | [optional] value must conform to RFC-3339 date-time
**scheduledDate** | None, str, datetime,  | NoneClass, str,  | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  | [optional] value must conform to RFC-3339 date-time
**[googleClassroom](#googleClassroom)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Google Classroom options for this assignment | [optional] 
**[microsoftGraph](#microsoftGraph)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Microsoft Graph options for this assignment | [optional] 
**assigneeMode** | str,  | str,  | Possible modes of assigning assignments | [optional] must be one of ["everyone", "selected", ] 
**[assignedStudents](#assignedStudents)** | list, tuple,  | tuple,  | Identifiers for the students that have access to the assignment | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClassAttachmentCreation**](ClassAttachmentCreation.md) | [**ClassAttachmentCreation**](ClassAttachmentCreation.md) | [**ClassAttachmentCreation**](ClassAttachmentCreation.md) |  | 

# googleClassroom

Google Classroom options for this assignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Google Classroom options for this assignment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**topicId** | None, str,  | NoneClass, str,  | Identifier of the topic where the assignment is created | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# microsoftGraph

Microsoft Graph options for this assignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Microsoft Graph options for this assignment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[categories](#categories)** | list, tuple, None,  | tuple, NoneClass,  | List of categories this assignment belongs to | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# categories

List of categories this assignment belongs to

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of categories this assignment belongs to | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

