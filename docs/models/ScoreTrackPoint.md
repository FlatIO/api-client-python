# flat_api.model.score_track_point.ScoreTrackPoint

A track synchronization point

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A track synchronization point | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**time** | decimal.Decimal, int, float,  | decimal.Decimal,  | The corresponding time in seconds | 
**type** | str,  | str,  | The type of the synchronization point. If the type is &#x60;measure&#x60;, the measure uuid must be present in &#x60;measureUuid&#x60; | must be one of ["measure", "end", ] 
**measureUuid** | str, uuid.UUID,  | str,  | The measure unique identifier | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

