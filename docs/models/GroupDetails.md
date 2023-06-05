# flat_api.model.group_details.GroupDetails

The details of a group

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The details of a group | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier of the group | [optional] 
**name** | str,  | str,  | The displayable name of the group | [optional] 
**type** | [**GroupType**](GroupType.md) | [**GroupType**](GroupType.md) |  | [optional] 
**organization** | str,  | str,  | The unique identifier of the Organization owning the group | [optional] 
**creationDate** | str, datetime,  | str,  | The date when the group was create | [optional] value must conform to RFC-3339 date-time
**usersCount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of students in this group | [optional] 
**readOnly** | bool,  | BoolClass,  | &#x60;true&#x60; if the properties and members of this group are in in read-only  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

