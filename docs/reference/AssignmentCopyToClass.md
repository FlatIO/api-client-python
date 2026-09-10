# AssignmentCopyToClass

Copy the assignment to a class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classroom** | **str** | The destination classroom where the assignment will be copied | 
**assignment** | **str** | An optional destination assignment where the original assignement will be copied. Must be a draft. | [optional] 
**scheduled_date** | **datetime** | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class. Alternatively the existing &#x60;scheduledDate&#x60; from the copied assignment will be used.  | [optional] 

## Example

```python
from flat_api.models.assignment_copy_to_class import AssignmentCopyToClass

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentCopyToClass from a JSON string
assignment_copy_to_class_instance = AssignmentCopyToClass.from_json(json)
# print the JSON string representation of the object
print(AssignmentCopyToClass.to_json())

# convert the object into a dict
assignment_copy_to_class_dict = assignment_copy_to_class_instance.to_dict()
# create an instance of AssignmentCopyToClass from a dict
assignment_copy_to_class_from_dict = AssignmentCopyToClass.from_dict(assignment_copy_to_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


