# EduResourceFolder

Education resources folder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the folder | [optional] 
**assignments_types** | [**List[AssignmentType]**](AssignmentType.md) | The assignment type of the resources that are included in the folder, | [optional] 
**resources_count** | **float** | The number of resources inside the folder | [optional] 

## Example

```python
from flat_api.models.edu_resource_folder import EduResourceFolder

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceFolder from a JSON string
edu_resource_folder_instance = EduResourceFolder.from_json(json)
# print the JSON string representation of the object
print(EduResourceFolder.to_json())

# convert the object into a dict
edu_resource_folder_dict = edu_resource_folder_instance.to_dict()
# create an instance of EduResourceFolder from a dict
edu_resource_folder_from_dict = EduResourceFolder.from_dict(edu_resource_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


