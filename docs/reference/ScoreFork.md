# ScoreFork

Options to fork the score

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** | Unique identifier of a collection where the score will be copied.  If no collection identifier is provided, a virtual collection is used, or &#x60;null&#x60; is provided, the score won&#39;t be added to any collection and will only be visible in the &#x60;allScores&#x60; virtual collection.  | [optional] 
**google_drive_disabled** | **bool** | If set to &#x60;true&#x60;, the API won&#39;t create the score on Google Drive  | [optional] [default to False]
**keep_original_title** | **bool** | Option to keep the original title of the score (i.e. don&#39;t prepend it with \&quot;Copy of \&quot;, or add the student name in assignment usage).  | [optional] 

## Example

```python
from flat_api.models.score_fork import ScoreFork

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreFork from a JSON string
score_fork_instance = ScoreFork.from_json(json)
# print the JSON string representation of the object
print(ScoreFork.to_json())

# convert the object into a dict
score_fork_dict = score_fork_instance.to_dict()
# create an instance of ScoreFork from a dict
score_fork_from_dict = ScoreFork.from_dict(score_fork_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


