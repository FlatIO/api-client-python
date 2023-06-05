# flat_api.model.assignment_submission.AssignmentSubmission

Assignment Submission

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Assignment Submission | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**creator** | str,  | str,  | The User identifier of the student who created the submission | 
**[attachments](#attachments)** | list, tuple,  | tuple,  |  | 
**assignment** | str,  | str,  | Unique identifier of the assignment | 
**classroom** | str,  | str,  | Unique identifier of the classroom where the assignment was posted  | 
**id** | str,  | str,  | Unique identifier of the submission | 
**state** | [**AssignmentSubmissionState**](AssignmentSubmissionState.md) | [**AssignmentSubmissionState**](AssignmentSubmissionState.md) |  | 
**creationDate** | str,  | str,  | The date when the submission was created | [optional] 
**submissionDate** | str,  | str,  | The date when the student submitted their work | [optional] 
**returnDate** | str,  | str,  | The date when the teacher returned the work | [optional] 
**returnCreator** | str,  | str,  | The User unique identifier of the teacher who returned the submission  | [optional] 
**grade** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Optional grade. If unset, no grade was set. | [optional] 
**draftGrade** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Optional grade. If unset, no grade was set. This value is only visible by the teacher, and we will be set to &#x60;grade&#x60; once the teacher returns the submission | [optional] 
**maxPoints** | decimal.Decimal, int, float,  | decimal.Decimal,  | Optional max points for the grade. If set, a corresponding &#x60;draftGrade&#x60; or &#x60;grade&#x60; will be set. | [optional] 
**[exercisesIds](#exercisesIds)** | list, tuple, None,  | tuple, NoneClass,  | The ids of exercises when they need to be in a specific order | [optional] 
**googleClassroom** | [**GoogleClassroomSubmission**](GoogleClassroomSubmission.md) | [**GoogleClassroomSubmission**](GoogleClassroomSubmission.md) |  | [optional] 
**microsoftGraph** | [**MicrosoftGraphSubmission**](MicrosoftGraphSubmission.md) | [**MicrosoftGraphSubmission**](MicrosoftGraphSubmission.md) |  | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

