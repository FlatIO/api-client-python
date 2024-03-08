# ClassCreation

Creation of a classroom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new class | 
**section** | **str** | The section of the new class | [optional] 
**level** | [**ClassGradeLevel**](ClassGradeLevel.md) |  | [optional] 
**skills_focused** | **List[str]** | Specific skills that will be focused in classroom | [optional] 
**size** | **float** | Number of students in the classroom | [optional] 

## Example

```python
from flat_api.models.class_creation import ClassCreation

# TODO update the JSON string below
json = "{}"
# create an instance of ClassCreation from a JSON string
class_creation_instance = ClassCreation.from_json(json)
# print the JSON string representation of the object
print ClassCreation.to_json()

# convert the object into a dict
class_creation_dict = class_creation_instance.to_dict()
# create an instance of ClassCreation from a dict
class_creation_form_dict = class_creation.from_dict(class_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


