# flat_api.model.organization_invitation.OrganizationInvitation

Details of an invitation to join an organization

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details of an invitation to join an organization | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The invitation unique identifier | [optional] 
**organization** | str,  | str,  | The unique identifier of the Organization owning this class | [optional] 
**organizationRole** | [**OrganizationRoles**](OrganizationRoles.md) | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**customCode** | str,  | str,  | Enrollment code to use when joining this organization | [optional] 
**email** | str,  | str,  | The email address this invitation was sent to | [optional] 
**invitedBy** | str,  | str,  | The unique identifier of the User who created this invitation | [optional] 
**usedBy** | str,  | str,  | The unique identifier of the User who used this invitation | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

