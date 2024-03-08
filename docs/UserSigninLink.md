# UserSigninLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to use to sign in to this account | [optional] 
**expiration_date** | **datetime** | Date when the link expires | [optional] 

## Example

```python
from flat_api.models.user_signin_link import UserSigninLink

# TODO update the JSON string below
json = "{}"
# create an instance of UserSigninLink from a JSON string
user_signin_link_instance = UserSigninLink.from_json(json)
# print the JSON string representation of the object
print UserSigninLink.to_json()

# convert the object into a dict
user_signin_link_dict = user_signin_link_instance.to_dict()
# create an instance of UserSigninLink from a dict
user_signin_link_form_dict = user_signin_link.from_dict(user_signin_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


