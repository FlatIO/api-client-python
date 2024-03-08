# TaskExportOptions

Options for the requested export 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts** | **List[str]** | A list of parts to specifically export | [optional] 

## Example

```python
from flat_api.models.task_export_options import TaskExportOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TaskExportOptions from a JSON string
task_export_options_instance = TaskExportOptions.from_json(json)
# print the JSON string representation of the object
print TaskExportOptions.to_json()

# convert the object into a dict
task_export_options_dict = task_export_options_instance.to_dict()
# create an instance of TaskExportOptions from a dict
task_export_options_form_dict = task_export_options.from_dict(task_export_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


