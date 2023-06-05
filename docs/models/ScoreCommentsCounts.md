# flat_api.model.score_comments_counts.ScoreCommentsCounts

A computed version of the total, unique, weekly and monthly number of comments added on the documents (this doesn't include inline comments). 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A computed version of the total, unique, weekly and monthly number of comments added on the documents (this doesn&#x27;t include inline comments).  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total number of comments added to the score | [optional] 
**unique** | decimal.Decimal, int, float,  | decimal.Decimal,  | The unique (1/user) number of comments added to the score | [optional] 
**weekly** | decimal.Decimal, int, float,  | decimal.Decimal,  | The weekly unique number of comments added to the score | [optional] 
**monthly** | decimal.Decimal, int, float,  | decimal.Decimal,  | The monthly unique number of comments added to the score | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

