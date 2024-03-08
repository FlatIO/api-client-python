# ClassAssignmentUpdateGoogleClassroom

Google Classroom options for this assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_id** | **str** | Identifier of the topic where the assignment is created | [optional] 

## Example

```python
from flat_api.models.class_assignment_update_google_classroom import ClassAssignmentUpdateGoogleClassroom

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAssignmentUpdateGoogleClassroom from a JSON string
class_assignment_update_google_classroom_instance = ClassAssignmentUpdateGoogleClassroom.from_json(json)
# print the JSON string representation of the object
print ClassAssignmentUpdateGoogleClassroom.to_json()

# convert the object into a dict
class_assignment_update_google_classroom_dict = class_assignment_update_google_classroom_instance.to_dict()
# create an instance of ClassAssignmentUpdateGoogleClassroom from a dict
class_assignment_update_google_classroom_form_dict = class_assignment_update_google_classroom.from_dict(class_assignment_update_google_classroom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


