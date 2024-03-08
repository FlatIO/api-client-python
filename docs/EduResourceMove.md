# EduResourceMove

Move an education resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | Unique identifier of the destination of the folder where to move this resource. This can also be &#x60;root&#x60; to move the resource at the root of the user resource library.  | 

## Example

```python
from flat_api.models.edu_resource_move import EduResourceMove

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceMove from a JSON string
edu_resource_move_instance = EduResourceMove.from_json(json)
# print the JSON string representation of the object
print EduResourceMove.to_json()

# convert the object into a dict
edu_resource_move_dict = edu_resource_move_instance.to_dict()
# create an instance of EduResourceMove from a dict
edu_resource_move_form_dict = edu_resource_move.from_dict(edu_resource_move_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


