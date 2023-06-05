# flat_api.model.score_track_creation.ScoreTrackCreation

Creation of a new track. This one must contain the URL of the track or the corresponding file 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Creation of a new track. This one must contain the URL of the track or the corresponding file  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | Title of the track | [optional] 
**default** | bool,  | BoolClass,  | True if the track should be used as default audio source | [optional] 
**state** | [**ScoreTrackState**](ScoreTrackState.md) | [**ScoreTrackState**](ScoreTrackState.md) |  | [optional] 
**url** | str,  | str,  | The URL of the track | [optional] 
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

