# EduLibrary

A Flat for Education Library

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the library.  This one can be used to list the underlying resources using &#x60;GET /v2/eduResources?parent&#x3D;{library-id}&#x60;  | [optional] 
**name** | **str** | Name of the lirbary | [optional] 
**type** | **str** | Type of the library | [optional] 
**visibility** | **str** | Visibility of the library | [optional] 

## Example

```python
from flat_api.models.edu_library import EduLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of EduLibrary from a JSON string
edu_library_instance = EduLibrary.from_json(json)
# print the JSON string representation of the object
print EduLibrary.to_json()

# convert the object into a dict
edu_library_dict = edu_library_instance.to_dict()
# create an instance of EduLibrary from a dict
edu_library_form_dict = edu_library.from_dict(edu_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


