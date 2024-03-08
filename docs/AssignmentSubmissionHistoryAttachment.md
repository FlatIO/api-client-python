# AssignmentSubmissionHistoryAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** | The score identifier that changed | [optional] 
**revision** | **str** | The revision identifier that changed | [optional] 
**title** | **str** | The title of the score that changed | [optional] 

## Example

```python
from flat_api.models.assignment_submission_history_attachment import AssignmentSubmissionHistoryAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentSubmissionHistoryAttachment from a JSON string
assignment_submission_history_attachment_instance = AssignmentSubmissionHistoryAttachment.from_json(json)
# print the JSON string representation of the object
print AssignmentSubmissionHistoryAttachment.to_json()

# convert the object into a dict
assignment_submission_history_attachment_dict = assignment_submission_history_attachment_instance.to_dict()
# create an instance of AssignmentSubmissionHistoryAttachment from a dict
assignment_submission_history_attachment_form_dict = assignment_submission_history_attachment.from_dict(assignment_submission_history_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


