# ClassAssignmentAllOfCanvas

A Canvas LMS assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the course on Canvas assignment | [optional] 
**alternate_link** | **str** | Link to Canvas assignment | [optional] 

## Example

```python
from flat_api.models.class_assignment_all_of_canvas import ClassAssignmentAllOfCanvas

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAssignmentAllOfCanvas from a JSON string
class_assignment_all_of_canvas_instance = ClassAssignmentAllOfCanvas.from_json(json)
# print the JSON string representation of the object
print(ClassAssignmentAllOfCanvas.to_json())

# convert the object into a dict
class_assignment_all_of_canvas_dict = class_assignment_all_of_canvas_instance.to_dict()
# create an instance of ClassAssignmentAllOfCanvas from a dict
class_assignment_all_of_canvas_from_dict = ClassAssignmentAllOfCanvas.from_dict(class_assignment_all_of_canvas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


