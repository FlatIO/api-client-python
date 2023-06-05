# Task

An asynchronous task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the task | [optional] 
**type** | **str** | Type of the task (e.g. audio-export) | [optional] 
**state** | **str** | State of the Task | [optional] 
**format** | **str** | For files processing, the file format (e.g. &#x60;mp3&#x60;, &#x60;wav&#x60;) | [optional] 
**score** | **str** | The score unique identifier for tasks related to scores | [optional] 
**progress** | [**TaskProgress**](TaskProgress.md) |  | [optional] 
**creation_date** | **datetime** | The creation date of the task | [optional] 
**modification_date** | **datetime** | The last modification date of the task | [optional] 
**done_date** | **datetime** | The date when the task has been completed | [optional] 
**result** | [**TaskResult**](TaskResult.md) |  | [optional] 
**error_history** | **[str]** | If any errors happened when processing this task, the list of errors identifiers | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


