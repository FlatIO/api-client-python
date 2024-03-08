# AssignmentSubmissionPlaybackInner

Playback used by student in this submission (used to limit the playback for the assignment)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** | The score unique identifier | 
**nb_play_attempt** | **float** | The number of playback used by the student | 

## Example

```python
from flat_api.models.assignment_submission_playback_inner import AssignmentSubmissionPlaybackInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentSubmissionPlaybackInner from a JSON string
assignment_submission_playback_inner_instance = AssignmentSubmissionPlaybackInner.from_json(json)
# print the JSON string representation of the object
print AssignmentSubmissionPlaybackInner.to_json()

# convert the object into a dict
assignment_submission_playback_inner_dict = assignment_submission_playback_inner_instance.to_dict()
# create an instance of AssignmentSubmissionPlaybackInner from a dict
assignment_submission_playback_inner_form_dict = assignment_submission_playback_inner.from_dict(assignment_submission_playback_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


