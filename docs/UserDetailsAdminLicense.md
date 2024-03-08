# UserDetailsAdminLicense

Current active license of the user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the current license | [optional] 
**expiration_date** | **datetime** | Date when the license expires | [optional] 
**source** | [**LicenseSources**](LicenseSources.md) |  | [optional] 
**mode** | [**LicenseMode**](LicenseMode.md) |  | [optional] 
**active** | **bool** | ID of the current license | [optional] 

## Example

```python
from flat_api.models.user_details_admin_license import UserDetailsAdminLicense

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailsAdminLicense from a JSON string
user_details_admin_license_instance = UserDetailsAdminLicense.from_json(json)
# print the JSON string representation of the object
print UserDetailsAdminLicense.to_json()

# convert the object into a dict
user_details_admin_license_dict = user_details_admin_license_instance.to_dict()
# create an instance of UserDetailsAdminLicense from a dict
user_details_admin_license_form_dict = user_details_admin_license.from_dict(user_details_admin_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


