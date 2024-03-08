# ScoreTrackUpdate

Update an existing track. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the track | [optional] 
**default** | **bool** | True if the track should be used as default audio source | [optional] 
**state** | [**ScoreTrackState**](ScoreTrackState.md) |  | [optional] 
**synchronization_points** | [**List[ScoreTrackPoint]**](ScoreTrackPoint.md) |  | [optional] 

## Example

```python
from flat_api.models.score_track_update import ScoreTrackUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreTrackUpdate from a JSON string
score_track_update_instance = ScoreTrackUpdate.from_json(json)
# print the JSON string representation of the object
print ScoreTrackUpdate.to_json()

# convert the object into a dict
score_track_update_dict = score_track_update_instance.to_dict()
# create an instance of ScoreTrackUpdate from a dict
score_track_update_form_dict = score_track_update.from_dict(score_track_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


