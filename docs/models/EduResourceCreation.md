# flat_api.model.edu_resource_creation.EduResourceCreation

Creation of an education resource

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Creation of an education resource | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | Title of the resource | 
**type** | [**EduResourceType**](EduResourceType.md) | [**EduResourceType**](EduResourceType.md) |  | 
**parent** | str,  | str,  | Identifier of the parent resource where the new one will created, e.g. a folder id or &#x60;root&#x60; | [optional] if omitted the server will use the default value of "root"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

