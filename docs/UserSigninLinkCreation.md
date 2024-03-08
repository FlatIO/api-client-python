# UserSigninLinkCreation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_path** | **str** | Path to redirect to after signin | [optional] [default to '/']

## Example

```python
from flat_api.models.user_signin_link_creation import UserSigninLinkCreation

# TODO update the JSON string below
json = "{}"
# create an instance of UserSigninLinkCreation from a JSON string
user_signin_link_creation_instance = UserSigninLinkCreation.from_json(json)
# print the JSON string representation of the object
print UserSigninLinkCreation.to_json()

# convert the object into a dict
user_signin_link_creation_dict = user_signin_link_creation_instance.to_dict()
# create an instance of UserSigninLinkCreation from a dict
user_signin_link_creation_form_dict = user_signin_link_creation.from_dict(user_signin_link_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


