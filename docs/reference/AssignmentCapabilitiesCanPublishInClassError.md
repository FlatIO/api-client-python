# AssignmentCapabilitiesCanPublishInClassError

If `canPublishInClass` and `canEdit` are false, the issue why this assignment cannot be published in a class 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A corresponding code for this error | 
**message** | **str** | A printable and localized message for this error | 

## Example

```python
from flat_api.models.assignment_capabilities_can_publish_in_class_error import AssignmentCapabilitiesCanPublishInClassError

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentCapabilitiesCanPublishInClassError from a JSON string
assignment_capabilities_can_publish_in_class_error_instance = AssignmentCapabilitiesCanPublishInClassError.from_json(json)
# print the JSON string representation of the object
print(AssignmentCapabilitiesCanPublishInClassError.to_json())

# convert the object into a dict
assignment_capabilities_can_publish_in_class_error_dict = assignment_capabilities_can_publish_in_class_error_instance.to_dict()
# create an instance of AssignmentCapabilitiesCanPublishInClassError from a dict
assignment_capabilities_can_publish_in_class_error_from_dict = AssignmentCapabilitiesCanPublishInClassError.from_dict(assignment_capabilities_can_publish_in_class_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


