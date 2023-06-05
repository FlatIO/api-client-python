# flat_api.model.score_modification.ScoreModification

Edit the score metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Edit the score metadata | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | The title of the score | [optional] 
**subtitle** | str,  | str,  | The subtitle of the score | [optional] 
**composer** | str,  | str,  | The composer of the score | [optional] 
**lyricist** | str,  | str,  | The lyricist of the score | [optional] 
**arranger** | str,  | str,  | The arranger of the score | [optional] 
**privacy** | [**ScorePrivacy**](ScorePrivacy.md) | [**ScorePrivacy**](ScorePrivacy.md) |  | [optional] 
**sharingKey** | str,  | str,  | When using the &#x60;privacy&#x60; mode &#x60;privateLink&#x60;, this property can be used to set a custom sharing key, otherwise a new key will be generated. | [optional] 
**description** | str,  | str,  | Description of the creation | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | Tags describing the score | [optional] 
**creationType** | [**ScoreCreationType**](ScoreCreationType.md) | [**ScoreCreationType**](ScoreCreationType.md) |  | [optional] 
**license** | [**ScoreLicense**](ScoreLicense.md) | [**ScoreLicense**](ScoreLicense.md) |  | [optional] 
**licenseText** | str,  | str,  | The rights info written on the score | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Tags describing the score

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tags describing the score | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

