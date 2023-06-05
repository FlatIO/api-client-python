# flat_api.model.score_track.ScoreTrack

An audio track for a score

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An audio track for a score | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier of the score track | [optional] 
**title** | str,  | str,  | Title of the track | [optional] 
**score** | str,  | str,  | The unique identifier of the score | [optional] 
**creator** | str,  | str,  | The unique identifier of the track creator | [optional] 
**creationDate** | str, datetime,  | str,  | The creation date of the track | [optional] value must conform to RFC-3339 date-time
**modificationDate** | str, datetime,  | str,  | The modification date of the track | [optional] value must conform to RFC-3339 date-time
**default** | bool,  | BoolClass,  | True if the track should be used as default audio source | [optional] 
**state** | [**ScoreTrackState**](ScoreTrackState.md) | [**ScoreTrackState**](ScoreTrackState.md) |  | [optional] 
**type** | [**ScoreTrackType**](ScoreTrackType.md) | [**ScoreTrackType**](ScoreTrackType.md) |  | [optional] 
**url** | str,  | str,  | The URL of the track | [optional] 
**mediaId** | str,  | str,  | The unique identifier of the track when hosted on an external service. For example, if the url is &#x60;https://www.youtube.com/watch?v&#x3D;dQw4w9WgXcQ&#x60;, &#x60;mediaId&#x60; will be &#x60;dQw4w9WgXcQ&#x60;  | [optional] 
**[synchronizationPoints](#synchronizationPoints)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# synchronizationPoints

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ScoreTrackPoint**](ScoreTrackPoint.md) | [**ScoreTrackPoint**](ScoreTrackPoint.md) | [**ScoreTrackPoint**](ScoreTrackPoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

