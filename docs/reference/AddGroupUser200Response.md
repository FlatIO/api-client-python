# AddGroupUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User ID that was added | [optional] 

## Example

```python
from flat_api.models.add_group_user200_response import AddGroupUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroupUser200Response from a JSON string
add_group_user200_response_instance = AddGroupUser200Response.from_json(json)
# print the JSON string representation of the object
print(AddGroupUser200Response.to_json())

# convert the object into a dict
add_group_user200_response_dict = add_group_user200_response_instance.to_dict()
# create an instance of AddGroupUser200Response from a dict
add_group_user200_response_from_dict = AddGroupUser200Response.from_dict(add_group_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


