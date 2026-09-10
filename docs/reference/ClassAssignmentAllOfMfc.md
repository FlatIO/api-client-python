# ClassAssignmentAllOfMfc

A MusicFirst Classroom assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the course on MusicFirst Task | [optional] 
**alternate_link** | **str** | Link to MusicFirst Classroom task | [optional] 

## Example

```python
from flat_api.models.class_assignment_all_of_mfc import ClassAssignmentAllOfMfc

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAssignmentAllOfMfc from a JSON string
class_assignment_all_of_mfc_instance = ClassAssignmentAllOfMfc.from_json(json)
# print the JSON string representation of the object
print(ClassAssignmentAllOfMfc.to_json())

# convert the object into a dict
class_assignment_all_of_mfc_dict = class_assignment_all_of_mfc_instance.to_dict()
# create an instance of ClassAssignmentAllOfMfc from a dict
class_assignment_all_of_mfc_from_dict = ClassAssignmentAllOfMfc.from_dict(class_assignment_all_of_mfc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


