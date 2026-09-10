# EduResourceAssignmentCreation

Assignment-specific creation options. Only applicable when creating a resource with `type: assignment`. If `type` is not provided, defaults to `none`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AssignmentType**](AssignmentType.md) |  | [optional] 

## Example

```python
from flat_api.models.edu_resource_assignment_creation import EduResourceAssignmentCreation

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceAssignmentCreation from a JSON string
edu_resource_assignment_creation_instance = EduResourceAssignmentCreation.from_json(json)
# print the JSON string representation of the object
print(EduResourceAssignmentCreation.to_json())

# convert the object into a dict
edu_resource_assignment_creation_dict = edu_resource_assignment_creation_instance.to_dict()
# create an instance of EduResourceAssignmentCreation from a dict
edu_resource_assignment_creation_from_dict = EduResourceAssignmentCreation.from_dict(edu_resource_assignment_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


