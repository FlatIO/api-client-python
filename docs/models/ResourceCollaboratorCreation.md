# flat_api.model.resource_collaborator_creation.ResourceCollaboratorCreation

Add a collaborator to a resource.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Add a collaborator to a resource. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user** | str,  | str,  | The unique identifier of a Flat user | [optional] 
**group** | str,  | str,  | The unique identifier of a Flat group | [optional] 
**userEmail** | str,  | str,  | Fill this field to invite an individual user by email.  | [optional] 
**userToken** | str,  | str,  | Token received in an invitation to join the score.  | [optional] 
**aclRead** | bool,  | BoolClass,  | &#x60;True&#x60; if the related user can read the score. (probably true if the user has a permission on the document).  | [optional] if omitted the server will use the default value of True
**aclWrite** | bool,  | BoolClass,  | &#x60;True&#x60; if the related user can modify the score.  | [optional] if omitted the server will use the default value of False
**aclAdmin** | bool,  | BoolClass,  | &#x60;True&#x60; if the related user can can manage the current document, i.e. changing the document permissions and deleting the document  | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

