# UserPublicSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user unique identifier | 
**type** | **str** | The type of user account | 
**product** | [**TutteoProduct**](TutteoProduct.md) |  | 
**username** | **str** | The user name (unique for the organization) | 
**printable_name** | **str** | The name that can be directly printed (name, firstname &amp; lastname, or username) | [optional] 
**firstname** | **str** | Firstname of the user (for education users) | [optional] 
**lastname** | **str** | Lastname of the user (for education users) | [optional] 
**name** | **str** | A displayable name for the user (for consumer users) | [optional] 
**picture** | **str** | The URL of the picture to display | 
**badges** | **List[str]** | List of badges for the user profile:  - &#x60;power&#x60; - &#x60;staff&#x60; - &#x60;composerOfTheMonth&#x60; - &#x60;ambassador&#x60; - &#x60;challenge&#x60;  | [optional] 
**organization** | **str** | Organization ID (for Edu users only) | [optional] 
**organization_role** | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**class_role** | [**ClassRoles**](ClassRoles.md) |  | [optional] 
**html_url** | **str** | Link to user profile (for Indiv. users only) | [optional] 

## Example

```python
from flat_api.models.user_public_summary import UserPublicSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UserPublicSummary from a JSON string
user_public_summary_instance = UserPublicSummary.from_json(json)
# print the JSON string representation of the object
print UserPublicSummary.to_json()

# convert the object into a dict
user_public_summary_dict = user_public_summary_instance.to_dict()
# create an instance of UserPublicSummary from a dict
user_public_summary_form_dict = user_public_summary.from_dict(user_public_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


