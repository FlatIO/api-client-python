# TaskResult

Optional result information about this task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL returned by the task worker | [optional] 
**error** | **str** | Error returned by task worker | [optional] 

## Example

```python
from flat_api.models.task_result import TaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResult from a JSON string
task_result_instance = TaskResult.from_json(json)
# print the JSON string representation of the object
print TaskResult.to_json()

# convert the object into a dict
task_result_dict = task_result_instance.to_dict()
# create an instance of TaskResult from a dict
task_result_form_dict = task_result.from_dict(task_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


