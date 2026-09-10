# AssignmentCopyToResourceLibrary

Copy the assignment to the EDU Resource Library

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**library_parent** | **str** | Identifier of the parent resource where the new one will created, e.g. a folder id or &#x60;root&#x60; | 
**verify_if_not_already_in_resource_library** | **bool** | Option to check if the assignment is already in Resource Library | [optional] 

## Example

```python
from flat_api.models.assignment_copy_to_resource_library import AssignmentCopyToResourceLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentCopyToResourceLibrary from a JSON string
assignment_copy_to_resource_library_instance = AssignmentCopyToResourceLibrary.from_json(json)
# print the JSON string representation of the object
print(AssignmentCopyToResourceLibrary.to_json())

# convert the object into a dict
assignment_copy_to_resource_library_dict = assignment_copy_to_resource_library_instance.to_dict()
# create an instance of AssignmentCopyToResourceLibrary from a dict
assignment_copy_to_resource_library_from_dict = AssignmentCopyToResourceLibrary.from_dict(assignment_copy_to_resource_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


