# flat_api.model.assignment_copy.AssignmentCopy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**classroom** | str,  | str,  | The destination classroom where the assignment will be copied | [optional] 
**assignment** | str,  | str,  | An optional destination assignment where the original assignement will be copied. Must be a draft. | [optional] 
**scheduledDate** | str, datetime,  | str,  | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class. Alternatively the existing &#x60;scheduledDate&#x60; from the copied assignment will be used.  | [optional] value must conform to RFC-3339 date-time
**libraryParent** | str,  | str,  | Identifier of the parent resource where the new one will created, e.g. a folder id or &#x60;root&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

