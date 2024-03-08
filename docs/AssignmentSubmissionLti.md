# AssignmentSubmissionLti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sourcedid** | **str** | The sourcedid of the LTI submission when using LTI Outcomes | 

## Example

```python
from flat_api.models.assignment_submission_lti import AssignmentSubmissionLti

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentSubmissionLti from a JSON string
assignment_submission_lti_instance = AssignmentSubmissionLti.from_json(json)
# print the JSON string representation of the object
print AssignmentSubmissionLti.to_json()

# convert the object into a dict
assignment_submission_lti_dict = assignment_submission_lti_instance.to_dict()
# create an instance of AssignmentSubmissionLti from a dict
assignment_submission_lti_form_dict = assignment_submission_lti.from_dict(assignment_submission_lti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


