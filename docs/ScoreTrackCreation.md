# ScoreTrackCreation

Creation of a new track. This one must contain the URL of the track or the corresponding file 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the track | [optional] 
**default** | **bool** | True if the track should be used as default audio source | [optional] 
**state** | [**ScoreTrackState**](ScoreTrackState.md) |  | [optional] 
**purpose** | [**ScoreTrackPurpose**](ScoreTrackPurpose.md) |  | [optional] 
**url** | **str** | The URL of the track | [optional] 
**synchronization_points** | [**List[ScoreTrackPoint]**](ScoreTrackPoint.md) |  | [optional] 

## Example

```python
from flat_api.models.score_track_creation import ScoreTrackCreation

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreTrackCreation from a JSON string
score_track_creation_instance = ScoreTrackCreation.from_json(json)
# print the JSON string representation of the object
print ScoreTrackCreation.to_json()

# convert the object into a dict
score_track_creation_dict = score_track_creation_instance.to_dict()
# create an instance of ScoreTrackCreation from a dict
score_track_creation_form_dict = score_track_creation.from_dict(score_track_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


