# flat_api.model.assignment_submission_comment.AssignmentSubmissionComment

Feedback comment added to an assignment submission

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Feedback comment added to an assignment submission | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The comment unique identifier | [optional] 
**user** | str,  | str,  | The author unique identifier | [optional] 
**submission** | str,  | str,  | The submission unique identifier | [optional] 
**date** | str, datetime,  | str,  | The date when the comment was posted | [optional] value must conform to RFC-3339 date-time
**modificationDate** | str, datetime,  | str,  | The date of the last comment modification | [optional] value must conform to RFC-3339 date-time
**comment** | str,  | str,  | The comment text | [optional] 
**unread** | bool,  | BoolClass,  | True if the comment is unread by the current user | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

