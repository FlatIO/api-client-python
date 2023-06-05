# flat_api.model.assignment_submission_history.AssignmentSubmissionHistory

History item of the submission

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | History item of the submission | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  | The date when the submission was changed | [optional] value must conform to RFC-3339 date-time
**[users](#users)** | list, tuple,  | tuple,  | The user(s) unique identifier(s) who made the change | [optional] 
**source** | str,  | str,  | The source of the change if the change was made by a third-party software | [optional] must be one of ["lti", "googleClassroom", "microsoftGraph", ] 
**state** | [**AssignmentSubmissionHistoryState**](AssignmentSubmissionHistoryState.md) | [**AssignmentSubmissionHistoryState**](AssignmentSubmissionHistoryState.md) |  | [optional] 
**draftGrade** | decimal.Decimal, int, float,  | decimal.Decimal,  | The numerator of the grade at this time in the submission grade history | [optional] 
**grade** | decimal.Decimal, int, float,  | decimal.Decimal,  | The numerator of the grade at this time in the submission grade history | [optional] 
**maxPoints** | decimal.Decimal, int, float,  | decimal.Decimal,  | The denominator of the grade at this time in the submission grade history | [optional] 
**comment** | str,  | str,  | The comment that is made to this submission | [optional] 
**dueDate** | str, datetime,  | str,  | The due date of this assignment | [optional] value must conform to RFC-3339 date-time
**[attachment](#attachment)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

The user(s) unique identifier(s) who made the change

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The user(s) unique identifier(s) who made the change | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# attachment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**score** | str,  | str,  | The score identifier that changed | [optional] 
**revision** | str,  | str,  | The revision identifier that changed | [optional] 
**title** | str,  | str,  | The title of the score that changed | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

