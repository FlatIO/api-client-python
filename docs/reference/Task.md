# Task

An asynchronous task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the task | 
**type** | **str** | Type of the task: * &#x60;audio-export&#x60;: Exports a score to audio format (MP3, WAV) * &#x60;score-save&#x60;: Saves or updates a score document * &#x60;import-omr&#x60;: Processes a PDF through OMR (Optical Music Recognition) and imports it as a score  | [optional] 
**state** | **str** | State of the Task | 
**format** | **str** | For files processing, the file format (e.g. &#x60;mp3&#x60;, &#x60;wav&#x60;) | [optional] 
**score** | **str** | The score unique identifier for tasks related to scores | [optional] 
**revision** | **str** | The score revision identifier for tasks related to scores | [optional] 
**progress** | [**TaskProgress**](TaskProgress.md) |  | [optional] 
**creation_date** | **datetime** | The creation date of the task | [optional] 
**modification_date** | **datetime** | The last modification date of the task | [optional] 
**done_date** | **datetime** | The date when the task has been completed | [optional] 
**result** | [**TaskResult**](TaskResult.md) |  | [optional] 
**error_history** | **List[str]** | If any errors happened when processing this task, the list of errors identifiers | [optional] 
**is_cancellable** | **bool** | Whether the task can be canceled by the user. Only &#x60;true&#x60; when the task is in &#x60;created&#x60; state (waiting to be processed).  | [optional] [readonly] 
**children** | [**List[Task]**](Task.md) | Child tasks for hierarchical task structures (e.g., conversion subtasks) | [optional] 

## Example

```python
from flat_api.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


