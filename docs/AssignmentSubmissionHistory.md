# AssignmentSubmissionHistory

History item of the submission

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **datetime** | The date when the submission was changed | [optional] 
**users** | **[str]** | The user(s) unique identifier(s) who made the change | [optional] 
**source** | **str** | The source of the change if the change was made by a third-party software | [optional] 
**state** | [**AssignmentSubmissionHistoryState**](AssignmentSubmissionHistoryState.md) |  | [optional] 
**draft_grade** | **float** | The numerator of the grade at this time in the submission grade history | [optional] 
**grade** | **float** | The numerator of the grade at this time in the submission grade history | [optional] 
**max_points** | **float** | The denominator of the grade at this time in the submission grade history | [optional] 
**comment** | **str** | The comment that is made to this submission | [optional] 
**due_date** | **datetime** | The due date of this assignment | [optional] 
**attachment** | [**AssignmentSubmissionHistoryAttachment**](AssignmentSubmissionHistoryAttachment.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


