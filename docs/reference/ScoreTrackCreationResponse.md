# ScoreTrackCreationResponse

Response for track creation including optional upload information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track** | [**ScoreTrack**](ScoreTrack.md) |  | 

## Example

```python
from flat_api.models.score_track_creation_response import ScoreTrackCreationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreTrackCreationResponse from a JSON string
score_track_creation_response_instance = ScoreTrackCreationResponse.from_json(json)
# print the JSON string representation of the object
print(ScoreTrackCreationResponse.to_json())

# convert the object into a dict
score_track_creation_response_dict = score_track_creation_response_instance.to_dict()
# create an instance of ScoreTrackCreationResponse from a dict
score_track_creation_response_from_dict = ScoreTrackCreationResponse.from_dict(score_track_creation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


