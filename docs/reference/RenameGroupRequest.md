# RenameGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name for the group | 

## Example

```python
from flat_api.models.rename_group_request import RenameGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenameGroupRequest from a JSON string
rename_group_request_instance = RenameGroupRequest.from_json(json)
# print the JSON string representation of the object
print(RenameGroupRequest.to_json())

# convert the object into a dict
rename_group_request_dict = rename_group_request_instance.to_dict()
# create an instance of RenameGroupRequest from a dict
rename_group_request_from_dict = RenameGroupRequest.from_dict(rename_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


