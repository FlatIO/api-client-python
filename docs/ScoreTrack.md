# ScoreTrack

An audio track for a score

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the score track | 
**title** | **str** | Title of the track | [optional] 
**score** | **str** | The unique identifier of the score | 
**creator** | **str** | The unique identifier of the track creator | 
**creation_date** | **datetime** | The creation date of the track | 
**modification_date** | **datetime** | The modification date of the track | 
**default** | **bool** | True if the track should be used as default audio source | 
**state** | [**ScoreTrackState**](ScoreTrackState.md) |  | 
**type** | [**ScoreTrackType**](ScoreTrackType.md) |  | 
**purpose** | [**ScoreTrackPurpose**](ScoreTrackPurpose.md) |  | 
**url** | **str** | The URL of the track | [optional] 
**media_id** | **str** | The unique identifier of the track when hosted on an external service. For example, if the url is &#x60;https://www.youtube.com/watch?v&#x3D;dQw4w9WgXcQ&#x60;, &#x60;mediaId&#x60; will be &#x60;dQw4w9WgXcQ&#x60;  | [optional] 
**synchronization_points** | [**List[ScoreTrackPoint]**](ScoreTrackPoint.md) |  | [optional] 

## Example

```python
from flat_api.models.score_track import ScoreTrack

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreTrack from a JSON string
score_track_instance = ScoreTrack.from_json(json)
# print the JSON string representation of the object
print ScoreTrack.to_json()

# convert the object into a dict
score_track_dict = score_track_instance.to_dict()
# create an instance of ScoreTrack from a dict
score_track_form_dict = score_track.from_dict(score_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


