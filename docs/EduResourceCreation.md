# EduResourceCreation

Creation of an education resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EduResourceType**](EduResourceType.md) |  | 
**title** | **str** | Title of the resource | 
**parent** | **str** | Identifier of the parent resource where the new one will created, e.g. a folder id or &#x60;root&#x60; | [optional] [default to 'root']

## Example

```python
from flat_api.models.edu_resource_creation import EduResourceCreation

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceCreation from a JSON string
edu_resource_creation_instance = EduResourceCreation.from_json(json)
# print the JSON string representation of the object
print EduResourceCreation.to_json()

# convert the object into a dict
edu_resource_creation_dict = edu_resource_creation_instance.to_dict()
# create an instance of EduResourceCreation from a dict
edu_resource_creation_form_dict = edu_resource_creation.from_dict(edu_resource_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


