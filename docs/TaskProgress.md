# TaskProgress

Details about the task progression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **float** | Percent of the task progression | [optional] 
**text** | **str** | Text details of the task progress | [optional] 

## Example

```python
from flat_api.models.task_progress import TaskProgress

# TODO update the JSON string below
json = "{}"
# create an instance of TaskProgress from a JSON string
task_progress_instance = TaskProgress.from_json(json)
# print the JSON string representation of the object
print TaskProgress.to_json()

# convert the object into a dict
task_progress_dict = task_progress_instance.to_dict()
# create an instance of TaskProgress from a dict
task_progress_form_dict = task_progress.from_dict(task_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


