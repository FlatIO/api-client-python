# EduResource

A Flat for Education resource contained in a resources library

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource unique identifier | 
**creator** | **str** | The User identifier of the resource creator | [optional] 
**type** | [**EduResourceType**](EduResourceType.md) |  | 
**privacy** | [**EduResourcePrivacy**](EduResourcePrivacy.md) |  | [optional] [default to EduResourcePrivacy.PRIVATE]
**tags** | **List[str]** | Specific attributes for the resource (e.g. sample resources with custom design) | [optional] 
**parent** | **str** | Identifier of the parent resource, e.g. a folder or root | [optional] 
**title** | **str** | Title of the resource | 
**sharing_description** | **str** | Sharing description of this resource | [optional] 
**sharing_description_html** | **str** | HTML version of sharing description with rich text formatting.  Supports safe HTML tags: p, br, strong, b, em, i, u, a.  | [optional] 
**creation_date** | **datetime** | The date when the resource was created | [optional] 
**update_date** | **datetime** | The date when the resource was updated | [optional] 
**resource** | [**EduResourceResource**](EduResourceResource.md) |  | [optional] 
**capabilities** | [**EduResourceCapabilities**](EduResourceCapabilities.md) |  | 
**subjects** | [**List[TeachingTheme]**](TeachingTheme.md) | The subjects of this resource, or the subjects of the resources included in the folder | [optional] 
**grades** | [**List[Grade]**](Grade.md) | The grades of this resource, or the grades of the resources included in the folder. | [optional] 

## Example

```python
from flat_api.models.edu_resource import EduResource

# TODO update the JSON string below
json = "{}"
# create an instance of EduResource from a JSON string
edu_resource_instance = EduResource.from_json(json)
# print the JSON string representation of the object
print(EduResource.to_json())

# convert the object into a dict
edu_resource_dict = edu_resource_instance.to_dict()
# create an instance of EduResource from a dict
edu_resource_from_dict = EduResource.from_dict(edu_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


