# ClassAssignmentLti

An LTI assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource ID in the LMS | [optional] 

## Example

```python
from flat_api.models.class_assignment_lti import ClassAssignmentLti

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAssignmentLti from a JSON string
class_assignment_lti_instance = ClassAssignmentLti.from_json(json)
# print the JSON string representation of the object
print ClassAssignmentLti.to_json()

# convert the object into a dict
class_assignment_lti_dict = class_assignment_lti_instance.to_dict()
# create an instance of ClassAssignmentLti from a dict
class_assignment_lti_form_dict = class_assignment_lti.from_dict(class_assignment_lti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


