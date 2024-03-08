# EduResource

A Flat for Education resource contained in a resources library

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource unique identifier | 
**creator** | **str** | The User identifier of the resource creator | [optional] 
**type** | [**EduResourceType**](EduResourceType.md) |  | 
**privacy** | [**EduResourcePrivacy**](EduResourcePrivacy.md) |  | [optional] 
**tags** | **List[str]** | Specific attributes for the resource (e.g. sample resources with custom design) | [optional] 
**parent** | **str** | Identifier of the parent resource, e.g. a folder or root | [optional] 
**title** | **str** | Title of the resource | 
**creation_date** | **datetime** | The date when the resource was created | [optional] 
**update_date** | **datetime** | The date when the resource was updated | [optional] 
**resource** | [**EduResourceResource**](EduResourceResource.md) |  | [optional] 
**capabilities** | [**EduResourceCapabilities**](EduResourceCapabilities.md) |  | 

## Example

```python
from flat_api.models.edu_resource import EduResource

# TODO update the JSON string below
json = "{}"
# create an instance of EduResource from a JSON string
edu_resource_instance = EduResource.from_json(json)
# print the JSON string representation of the object
print EduResource.to_json()

# convert the object into a dict
edu_resource_dict = edu_resource_instance.to_dict()
# create an instance of EduResource from a dict
edu_resource_form_dict = edu_resource.from_dict(edu_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


