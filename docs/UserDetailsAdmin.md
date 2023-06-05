# UserDetailsAdmin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user unique identifier | [optional] 
**type** | **str** | The type of user account | [optional] 
**username** | **str** | The user name (unique for the organization) | [optional] 
**printable_name** | **str** | The name that can be directly printed (name, firstname &amp; lastname, or username) | [optional] 
**firstname** | **str** | Firstname of the user (for education users) | [optional] 
**lastname** | **str** | Lastname of the user (for education users) | [optional] 
**name** | **str** | A displayable name for the user (for consumer users) | [optional] 
**picture** | **str, none_type** | The URL of the picture to display | [optional] 
**badges** | **[str]** | List of badges for the user profile | [optional] 
**organization** | **str** | Organization ID (for Edu users only) | [optional] 
**organization_role** | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**class_role** | [**ClassRoles**](ClassRoles.md) |  | [optional] 
**html_url** | **str** | Link to user profile (for Indiv. users only) | [optional] 
**email** | **str** | Email of the user | [optional] 
**last_activity_date** | **datetime** | Date of the last user activity | [optional] 
**license** | [**UserDetailsAdminLicense**](UserDetailsAdminLicense.md) |  | [optional] 
**groups** | **[str]** | For Flat for Education accounts, list of Group identifiers the user is part of. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


