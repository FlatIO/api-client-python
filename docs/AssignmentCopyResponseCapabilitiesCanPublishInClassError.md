# AssignmentCopyResponseCapabilitiesCanPublishInClassError

If `canPublishInClass` and `canEdit` are false, the issue why this assignment cannot be published in a class 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A corresponding code for this error | 
**message** | **str** | A printable and localized message for this error | 

## Example

```python
from flat_api.models.assignment_copy_response_capabilities_can_publish_in_class_error import AssignmentCopyResponseCapabilitiesCanPublishInClassError

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentCopyResponseCapabilitiesCanPublishInClassError from a JSON string
assignment_copy_response_capabilities_can_publish_in_class_error_instance = AssignmentCopyResponseCapabilitiesCanPublishInClassError.from_json(json)
# print the JSON string representation of the object
print AssignmentCopyResponseCapabilitiesCanPublishInClassError.to_json()

# convert the object into a dict
assignment_copy_response_capabilities_can_publish_in_class_error_dict = assignment_copy_response_capabilities_can_publish_in_class_error_instance.to_dict()
# create an instance of AssignmentCopyResponseCapabilitiesCanPublishInClassError from a dict
assignment_copy_response_capabilities_can_publish_in_class_error_form_dict = assignment_copy_response_capabilities_can_publish_in_class_error.from_dict(assignment_copy_response_capabilities_can_publish_in_class_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


