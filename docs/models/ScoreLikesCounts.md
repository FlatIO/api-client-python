# flat_api.model.score_likes_counts.ScoreLikesCounts

A computed version of the weekly, monthly and total of number of likes for a score 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A computed version of the weekly, monthly and total of number of likes for a score  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total number of likes of the score | [optional] 
**weekly** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of new likes during the last week | [optional] 
**monthly** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of new likes during the last month | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

