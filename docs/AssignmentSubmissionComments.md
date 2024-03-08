# AssignmentSubmissionComments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | The total number of comments added to the submission | [optional] 
**unread** | **float** | The number of unread comments for the current user | [optional] 

## Example

```python
from flat_api.models.assignment_submission_comments import AssignmentSubmissionComments

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentSubmissionComments from a JSON string
assignment_submission_comments_instance = AssignmentSubmissionComments.from_json(json)
# print the JSON string representation of the object
print AssignmentSubmissionComments.to_json()

# convert the object into a dict
assignment_submission_comments_dict = assignment_submission_comments_instance.to_dict()
# create an instance of AssignmentSubmissionComments from a dict
assignment_submission_comments_form_dict = assignment_submission_comments.from_dict(assignment_submission_comments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


