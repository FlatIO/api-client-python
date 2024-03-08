# EduResourceCapabilities

Capabilities available for this resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_edit** | **bool** | Whether the current user can modify this resource  | [optional] 
**can_add_resources** | **bool** | Whether the current user can add resources within this resource (e.g. &#x60;assignment&#x60; inside a &#x60;folder&#x60;)  | [optional] 
**can_add_folders** | **bool** | Whether the current user can add folders within this resource (e.g. &#x60;folder&#x60; inside &#x60;root&#x60;)  | [optional] 

## Example

```python
from flat_api.models.edu_resource_capabilities import EduResourceCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceCapabilities from a JSON string
edu_resource_capabilities_instance = EduResourceCapabilities.from_json(json)
# print the JSON string representation of the object
print EduResourceCapabilities.to_json()

# convert the object into a dict
edu_resource_capabilities_dict = edu_resource_capabilities_instance.to_dict()
# create an instance of EduResourceCapabilities from a dict
edu_resource_capabilities_form_dict = edu_resource_capabilities.from_dict(edu_resource_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


