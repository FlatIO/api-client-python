# AssignmentSubmissionLti

If set, this submission has a linked LTI 1.3 AGS or LTI 1.1 Outcomes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade_service** | **str** | The kind of grading service available for this submission:  - &#x60;ags2p0&#x60;: LTI 1.3 Assignment and Grade Services 2.0 - &#x60;outcomes1p1&#x60;: LTI 1.1 Outcomes 1.1  | 
**sourcedid** | **str** | The sourcedid of the LTI submission when using LTI Outcomes | [optional] 

## Example

```python
from flat_api.models.assignment_submission_lti import AssignmentSubmissionLti

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentSubmissionLti from a JSON string
assignment_submission_lti_instance = AssignmentSubmissionLti.from_json(json)
# print the JSON string representation of the object
print(AssignmentSubmissionLti.to_json())

# convert the object into a dict
assignment_submission_lti_dict = assignment_submission_lti_instance.to_dict()
# create an instance of AssignmentSubmissionLti from a dict
assignment_submission_lti_from_dict = AssignmentSubmissionLti.from_dict(assignment_submission_lti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


