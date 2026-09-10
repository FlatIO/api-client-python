# EduResourceUpdate

Update of an education resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the resource | [optional] 
**sharing_description** | **str** | Sharing description of the resource | [optional] 
**sharing_description_html** | **str** | HTML version of sharing description with rich text formatting.  Supports safe HTML tags: p, br, strong, b, em, i, u, a.  | [optional] 
**privacy** | [**EduResourcePrivacy**](EduResourcePrivacy.md) |  | [optional] [default to EduResourcePrivacy.PRIVATE]
**subjects** | [**List[TeachingTheme]**](TeachingTheme.md) | The subjects of this resource, or the subjects of the resources included in the folder | [optional] 
**grades** | [**List[Grade]**](Grade.md) | The grades of this resource, or the grades of the resources included in the folder. | [optional] 

## Example

```python
from flat_api.models.edu_resource_update import EduResourceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceUpdate from a JSON string
edu_resource_update_instance = EduResourceUpdate.from_json(json)
# print the JSON string representation of the object
print(EduResourceUpdate.to_json())

# convert the object into a dict
edu_resource_update_dict = edu_resource_update_instance.to_dict()
# create an instance of EduResourceUpdate from a dict
edu_resource_update_from_dict = EduResourceUpdate.from_dict(edu_resource_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


