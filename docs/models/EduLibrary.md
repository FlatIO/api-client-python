# flat_api.model.edu_library.EduLibrary

A Flat for Education Library

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Flat for Education Library | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of the library.  This one can be used to list the underlying resources using &#x60;GET /v2/eduResources?parent&#x3D;{library-id}&#x60;  | [optional] 
**name** | str,  | str,  | Name of the lirbary | [optional] 
**type** | str,  | str,  | Type of the library | [optional] must be one of ["myResources", "flatEduSamples", ] 
**visibility** | str,  | str,  | Visibility of the library | [optional] must be one of ["private", "organization", "public", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

