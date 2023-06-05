# flat_api.model.microsoft_graph_assignment.MicrosoftGraphAssignment

A Microsoft Teams asignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Microsoft Teams asignment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Identifier of the assignement assigned by Microsoft Teams | [optional] 
**state** | str,  | str,  | State of the assignment | [optional] 
**alternateLink** | str,  | str,  | Absolute link to this assignement in the Microsoft Teams web UI | [optional] 
**[categories](#categories)** | list, tuple,  | tuple,  | List of categories where this assignment is published under | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# categories

List of categories where this assignment is published under

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of categories where this assignment is published under | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | A Microsoft Teams assignment category ID | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

