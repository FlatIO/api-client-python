# AssignmentCapabilities

Capabilities the current user has on this assignment. Each capability corresponds to a fine-grained action that a user may take.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_edit** | **bool** | Whether the current user can edit the assignment  | 
**can_publish_in_class** | **bool** | Whether this assignment can be published in a class  | 
**can_publish_in_class_error** | [**AssignmentCapabilitiesCanPublishInClassError**](AssignmentCapabilitiesCanPublishInClassError.md) |  | [optional] 
**can_archive** | **bool** | Whether the current user can archive the assignment  | 
**can_unarchive** | **bool** | Whether the current user can unarchive the assignment  | 

## Example

```python
from flat_api.models.assignment_capabilities import AssignmentCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentCapabilities from a JSON string
assignment_capabilities_instance = AssignmentCapabilities.from_json(json)
# print the JSON string representation of the object
print(AssignmentCapabilities.to_json())

# convert the object into a dict
assignment_capabilities_dict = assignment_capabilities_instance.to_dict()
# create an instance of AssignmentCapabilities from a dict
assignment_capabilities_from_dict = AssignmentCapabilities.from_dict(assignment_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


