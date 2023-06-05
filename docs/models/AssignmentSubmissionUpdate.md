# flat_api.model.assignment_submission_update.AssignmentSubmissionUpdate

Assignment Submission creation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Assignment Submission creation | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attachments](#attachments)** | list, tuple,  | tuple,  |  | [optional] 
**submit** | bool,  | BoolClass,  | If &#x60;true&#x60;, the submission will be marked as done | [optional] 
**draftGrade** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Optional grade. If unset, no grade was set. This value is only visible by the teacher, and we will be set to &#x60;grade&#x60; once the teacher returns the submission | [optional] 
**grade** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Optional grade. If unset, no grade was set. | [optional] 
**[exercisesIds](#exercisesIds)** | list, tuple, None,  | tuple, NoneClass,  | The ids of exercises when they need to be in a specific order | [optional] 
**return** | bool,  | BoolClass,  | If &#x60;true&#x60;, the submission will be marked as done | [optional] 
**[comments](#comments)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
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

# exercisesIds

The ids of exercises when they need to be in a specific order

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The ids of exercises when they need to be in a specific order | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# comments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total number of comments added to the submission | [optional] 
**unread** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of unread comments for the current user | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

