# UserAdminUpdate

User update as an organization admin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password of the account | [optional] 
**organization_role** | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**username** | **str** | Username of the account | [optional] 
**firstname** | **str** | First name of the user | [optional] 
**lastname** | **str** | Last name of the user | [optional] 
**email** | **str** | Email of the account | [optional] 

## Example

```python
from flat_api.models.user_admin_update import UserAdminUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminUpdate from a JSON string
user_admin_update_instance = UserAdminUpdate.from_json(json)
# print the JSON string representation of the object
print UserAdminUpdate.to_json()

# convert the object into a dict
user_admin_update_dict = user_admin_update_instance.to_dict()
# create an instance of UserAdminUpdate from a dict
user_admin_update_form_dict = user_admin_update.from_dict(user_admin_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


