# UserDetailsAdmin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user unique identifier | [optional] 
**username** | **str** | The user name (unique for the organization) | [optional] 
**name** | **str** | A displayable name for the user | [optional] 
**printable_name** | **str** | The name that can be directly printed (name or username) | [optional] 
**picture** | **str** | User pictue | [optional] 
**is_power_user** | **bool** | User license status. &#39;True&#39; if user is an individual Power user | [optional] 
**organization** | **str** | Organization ID (for Edu users only) | [optional] 
**organization_role** | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**class_role** | [**ClassRoles**](ClassRoles.md) |  | [optional] 
**html_url** | **str** | Link to user profile (for Indiv. users only) | [optional] 
**email** | **str** | Email of the user | [optional] 
**last_activity_date** | **datetime** | Date of the last user activity | [optional] 
**license** | [**UserDetailsAdminLicense**](UserDetailsAdminLicense.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


