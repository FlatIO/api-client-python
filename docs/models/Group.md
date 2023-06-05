# flat_api.model.group.Group

A group of users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A group of users | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier of the group | [optional] 
**name** | str,  | str,  | The display name of the group | [optional] 
**type** | str,  | str,  | The type of the group: * &#x60;generic&#x60;: A group created by a Flat user * &#x60;classTeachers&#x60;: A group created automaticaly by Flat that contains   the teachers of a class * &#x60;classStudents&#x60;: A group created automaticaly by Flat that contains   the studnets of a class  | [optional] must be one of ["generic", "classTeachers", "classStudents", ] 
**usersCount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of users in this group | [optional] 
**readOnly** | bool,  | BoolClass,  | &#x60;True&#x60; if the group is set in read-only  | [optional] 
**organization** | str,  | str,  | If the group is related to an organization, this field will contain the unique identifier of the organization  | [optional] 
**creationDate** | str, datetime,  | str,  | The creation date of the group | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

