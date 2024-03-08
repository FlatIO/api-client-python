# UserCreation

User creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username of the new account | 
**firstname** | **str** | First name of the user | [optional] 
**lastname** | **str** | Last name of the user | [optional] 
**email** | **str** | Email of the new account | [optional] 
**password** | **str** | Password of the new account | 
**locale** | [**FlatLocales**](FlatLocales.md) |  | [optional] 
**role** | **str** | Role of the new account | [optional] [default to 'user']

## Example

```python
from flat_api.models.user_creation import UserCreation

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreation from a JSON string
user_creation_instance = UserCreation.from_json(json)
# print the JSON string representation of the object
print UserCreation.to_json()

# convert the object into a dict
user_creation_dict = user_creation_instance.to_dict()
# create an instance of UserCreation from a dict
user_creation_form_dict = user_creation.from_dict(user_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


