# ScoreTrack

An audio track for a score
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the score track | [optional] 
**title** | **str** | Title of the track | [optional] 
**score** | **str** | The unique identifier of the score | [optional] 
**creator** | **str** | The unique identifier of the track creator | [optional] 
**creation_date** | **datetime** | The creation date of the track | [optional] 
**modification_date** | **datetime** | The modification date of the track | [optional] 
**default** | **bool** | True if the track should be used as default audio source | [optional] 
**state** | [**ScoreTrackState**](ScoreTrackState.md) |  | [optional] 
**type** | [**ScoreTrackType**](ScoreTrackType.md) |  | [optional] 
**url** | **str** | The URL of the track | [optional] 
**media_id** | **str** | The unique identifier of the track when hosted on an external service. For example, if the url is &#x60;https://www.youtube.com/watch?v&#x3D;dQw4w9WgXcQ&#x60;, &#x60;mediaId&#x60; will be &#x60;dQw4w9WgXcQ&#x60;  | [optional] 
**synchronization_points** | [**list[ScoreTrackPoint]**](ScoreTrackPoint.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


