# UserAzureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oid** | **str** | User object identifier on Azure AD | [optional] 
**hd** | **str** | User tenant (domain name) | [optional] 
**preferred_username** | **str** | User Preferred Username (UPN), i.e. the main email of the user | [optional] 

## Example

```python
from flat_api.models.user_azure_details import UserAzureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserAzureDetails from a JSON string
user_azure_details_instance = UserAzureDetails.from_json(json)
# print the JSON string representation of the object
print UserAzureDetails.to_json()

# convert the object into a dict
user_azure_details_dict = user_azure_details_instance.to_dict()
# create an instance of UserAzureDetails from a dict
user_azure_details_form_dict = user_azure_details.from_dict(user_azure_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


