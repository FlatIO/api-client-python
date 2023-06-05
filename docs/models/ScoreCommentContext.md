# flat_api.model.score_comment_context.ScoreCommentContext

The context of the comment (for inline/contextualized comments). A context will include all the information related to the location of the comment (i.e. score parts, range of measure, time position). 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The context of the comment (for inline/contextualized comments). A context will include all the information related to the location of the comment (i.e. score parts, range of measure, time position).  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[measureUuids](#measureUuids)** | list, tuple,  | tuple,  | The list of measure UUIds | 
**partUuid** | str,  | str,  | The unique identifier (UUID) of the score part | 
**stopDpq** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**startTimePos** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**startDpq** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**stopTimePos** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**staffIdx** | decimal.Decimal, int, float,  | decimal.Decimal,  | (Deprecated, use &#x60;staffUuid&#x60;) The identififer of the staff | [optional] 
**staffUuid** | str,  | str,  | The unique identififer (UUID) of the staff | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# measureUuids

The list of measure UUIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of measure UUIds | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

