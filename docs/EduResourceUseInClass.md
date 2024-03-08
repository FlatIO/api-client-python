# EduResourceUseInClass

Use an education resource in class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classroom** | **str** | The destination classroom where the resource will be copied. | 
**assignment** | **str** | An optional destination assignment where the original assignement will be copied. Must be a draft. | [optional] 

## Example

```python
from flat_api.models.edu_resource_use_in_class import EduResourceUseInClass

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceUseInClass from a JSON string
edu_resource_use_in_class_instance = EduResourceUseInClass.from_json(json)
# print the JSON string representation of the object
print EduResourceUseInClass.to_json()

# convert the object into a dict
edu_resource_use_in_class_dict = edu_resource_use_in_class_instance.to_dict()
# create an instance of EduResourceUseInClass from a dict
edu_resource_use_in_class_form_dict = edu_resource_use_in_class.from_dict(edu_resource_use_in_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


