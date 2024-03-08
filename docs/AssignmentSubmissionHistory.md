# AssignmentSubmissionHistory

History item of the submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date when the submission was changed | 
**classroom** | **str** | The classroom unique identifier where the submission was changed | [optional] 
**assignment** | **str** | The assignment unique identifier where the submission was changed | [optional] 
**submission** | **str** | The submission unique identifier | [optional] 
**users** | **List[str]** | The user(s) unique identifier(s) who made the change | 
**source** | **str** | The source of the change if the change was made by a third-party software | [optional] 
**state** | [**AssignmentSubmissionHistoryState**](AssignmentSubmissionHistoryState.md) |  | [optional] 
**draft_grade** | **float** | The numerator of the grade at this time in the submission grade history | [optional] 
**grade** | **float** | The numerator of the grade at this time in the submission grade history | [optional] 
**max_points** | **float** | The denominator of the grade at this time in the submission grade history | [optional] 
**comment** | **str** | The comment that is made to this submission | [optional] 
**due_date** | **datetime** | The due date of this assignment | [optional] 
**attachment** | [**AssignmentSubmissionHistoryAttachment**](AssignmentSubmissionHistoryAttachment.md) |  | [optional] 

## Example

```python
from flat_api.models.assignment_submission_history import AssignmentSubmissionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentSubmissionHistory from a JSON string
assignment_submission_history_instance = AssignmentSubmissionHistory.from_json(json)
# print the JSON string representation of the object
print AssignmentSubmissionHistory.to_json()

# convert the object into a dict
assignment_submission_history_dict = assignment_submission_history_instance.to_dict()
# create an instance of AssignmentSubmissionHistory from a dict
assignment_submission_history_form_dict = assignment_submission_history.from_dict(assignment_submission_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


