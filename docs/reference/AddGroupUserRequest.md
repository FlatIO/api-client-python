# AddGroupUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | ID of the student to add | 

## Example

```python
from flat_api.models.add_group_user_request import AddGroupUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroupUserRequest from a JSON string
add_group_user_request_instance = AddGroupUserRequest.from_json(json)
# print the JSON string representation of the object
print(AddGroupUserRequest.to_json())

# convert the object into a dict
add_group_user_request_dict = add_group_user_request_instance.to_dict()
# create an instance of AddGroupUserRequest from a dict
add_group_user_request_from_dict = AddGroupUserRequest.from_dict(add_group_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


