# flat_api.model.score_fork.ScoreFork

Options to fork the score

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Options to fork the score | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection** | None, str,  | NoneClass, str,  | Unique identifier of a collection where the score will be copied. If no collection identifier is provided, the score will be stored in the &#x60;root&#x60; directory. If null is provided, the score won&#x27;t be added to any collections  | [optional] if omitted the server will use the default value of "root"
**keepOriginalTitle** | bool,  | BoolClass,  | Option to keep the original title of the score (i.e. don&#x27;t prepend it with \&quot;Copy of \&quot;, or add the student name in assignment usage).  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

