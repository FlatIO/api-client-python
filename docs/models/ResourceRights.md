# flat_api.model.resource_rights.ResourceRights

The rights of the current user on a score or collection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The rights of the current user on a score or collection | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**aclRead** | bool,  | BoolClass,  | &#x60;True&#x60; if the current user can read the current document  | [optional] if omitted the server will use the default value of False
**aclWrite** | bool,  | BoolClass,  | &#x60;True&#x60; if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [optional] if omitted the server will use the default value of False
**aclAdmin** | bool,  | BoolClass,  | &#x60;True&#x60; if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [optional] if omitted the server will use the default value of False
**isCollaborator** | bool,  | BoolClass,  | &#x60;True&#x60; if the current user is a collaborator of the current document (direct or via group).  | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

