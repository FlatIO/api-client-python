# EduResourceCopy

Copy an education resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | Unique identifier of the destination of the folder where to copy this resource. This can also be &#x60;root&#x60; to copy the resource at the root of the user resource library.  | 

## Example

```python
from flat_api.models.edu_resource_copy import EduResourceCopy

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceCopy from a JSON string
edu_resource_copy_instance = EduResourceCopy.from_json(json)
# print the JSON string representation of the object
print EduResourceCopy.to_json()

# convert the object into a dict
edu_resource_copy_dict = edu_resource_copy_instance.to_dict()
# create an instance of EduResourceCopy from a dict
edu_resource_copy_form_dict = edu_resource_copy.from_dict(edu_resource_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


