# flat_api.model.assignment.Assignment

Assignment details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Assignment details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attachments](#attachments)** | list, tuple,  | tuple,  |  | 
**[capabilities](#capabilities)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Capabilities the current user has on this assignment. Each capability corresponds to a fine-grained action that a user may take. | 
**id** | str,  | str,  | Unique identifier of the assignment | 
**title** | str,  | str,  | Title of the assignment | 
**type** | [**AssignmentType**](AssignmentType.md) | [**AssignmentType**](AssignmentType.md) |  | 
**description** | str,  | str,  | Description and content of the assignment | [optional] 
**cover** | str,  | str,  | The URL of the cover to display | [optional] 
**coverFile** | str,  | str,  | The id of the cover to display | [optional] 
**useDedicatedAttachments** | bool,  | BoolClass,  | For all assignments created after 02/2023, all the underlying resources must be dedicated and stored in the assignment. This boolean indicates that this assignment only supports dedicated attachments.  | [optional] 
**maxPoints** | decimal.Decimal, int, float,  | decimal.Decimal,  | If set, the grading will be enabled for the assignement  | [optional] 
**releaseGrades** | str,  | str,  | For worksheets, how grading will work for the assignment: - If set to &#x60;auto&#x60;, the grades will be automatically released when the student submits the submissions - If set to &#x60;manual&#x60;, the grades will only be set as &#x60;draftGrade&#x60; and will be released when the teacher returns the submissions  | [optional] must be one of ["auto", "manual", ] 
**shuffleExercises** | bool,  | BoolClass,  | Mixing worksheets exercises for each student | [optional] 
**toolset** | str,  | str,  | The id of the associated toolset | [optional] 
**nbPlaybackAuthorized** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of playback authorized on the scores of the assignment. | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

