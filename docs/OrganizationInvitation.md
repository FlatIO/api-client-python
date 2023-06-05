# OrganizationInvitation

Details of an invitation to join an organization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The invitation unique identifier | [optional] 
**organization** | **str** | The unique identifier of the Organization owning this class | [optional] 
**organization_role** | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**custom_code** | **str** | Enrollment code to use when joining this organization | [optional] 
**email** | **str** | The email address this invitation was sent to | [optional] 
**invited_by** | **str** | The unique identifier of the User who created this invitation | [optional] 
**used_by** | **str** | The unique identifier of the User who used this invitation | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


