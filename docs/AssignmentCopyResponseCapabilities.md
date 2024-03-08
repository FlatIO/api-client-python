# AssignmentCopyResponseCapabilities

Capabilities the current user has on this assignment. Each capability corresponds to a fine-grained action that a user may take.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_edit** | **bool** | Whether the current user can edit the assignment  | 
**can_publish_in_class** | **bool** | Whether this assignment can be published in a class  | 
**can_publish_in_class_error** | [**AssignmentCopyResponseCapabilitiesCanPublishInClassError**](AssignmentCopyResponseCapabilitiesCanPublishInClassError.md) |  | [optional] 
**can_archive** | **bool** | Whether the current user can archive the assignment  | 
**can_unarchive** | **bool** | Whether the current user can unarchive the assignment  | 

## Example

```python
from flat_api.models.assignment_copy_response_capabilities import AssignmentCopyResponseCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentCopyResponseCapabilities from a JSON string
assignment_copy_response_capabilities_instance = AssignmentCopyResponseCapabilities.from_json(json)
# print the JSON string representation of the object
print AssignmentCopyResponseCapabilities.to_json()

# convert the object into a dict
assignment_copy_response_capabilities_dict = assignment_copy_response_capabilities_instance.to_dict()
# create an instance of AssignmentCopyResponseCapabilities from a dict
assignment_copy_response_capabilities_form_dict = assignment_copy_response_capabilities.from_dict(assignment_copy_response_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


