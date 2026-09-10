# AssignmentSubmissionPlayback

Playback used by a student for an assignment submission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** | The score unique identifier | 
**nb_play_attempt** | **float** | Number of times the score was played | 

## Example

```python
from flat_api.models.assignment_submission_playback import AssignmentSubmissionPlayback

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentSubmissionPlayback from a JSON string
assignment_submission_playback_instance = AssignmentSubmissionPlayback.from_json(json)
# print the JSON string representation of the object
print(AssignmentSubmissionPlayback.to_json())

# convert the object into a dict
assignment_submission_playback_dict = assignment_submission_playback_instance.to_dict()
# create an instance of AssignmentSubmissionPlayback from a dict
assignment_submission_playback_from_dict = AssignmentSubmissionPlayback.from_dict(assignment_submission_playback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


