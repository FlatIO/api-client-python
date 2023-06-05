# flat_api.model.task.Task

An asynchronous task

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An asynchronous task | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of the task | [optional] 
**type** | str,  | str,  | Type of the task (e.g. audio-export) | [optional] 
**state** | str,  | str,  | State of the Task | [optional] must be one of ["created", "doing", "done", "canceled", "error", ] 
**format** | str,  | str,  | For files processing, the file format (e.g. &#x60;mp3&#x60;, &#x60;wav&#x60;) | [optional] 
**score** | str,  | str,  | The score unique identifier for tasks related to scores | [optional] 
**[progress](#progress)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Details about the task progression | [optional] 
**creationDate** | str, datetime,  | str,  | The creation date of the task | [optional] value must conform to RFC-3339 date-time
**modificationDate** | str, datetime,  | str,  | The last modification date of the task | [optional] value must conform to RFC-3339 date-time
**doneDate** | str, datetime,  | str,  | The date when the task has been completed | [optional] value must conform to RFC-3339 date-time
**[result](#result)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Optional result information about this task | [optional] 
**[errorHistory](#errorHistory)** | list, tuple,  | tuple,  | If any errors happened when processing this task, the list of errors identifiers | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# progress

Details about the task progression

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details about the task progression | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**percent** | decimal.Decimal, int, float,  | decimal.Decimal,  | Percent of the task progression | [optional] 
**text** | str,  | str,  | Text details of the task progress | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# result

Optional result information about this task

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Optional result information about this task | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**url** | str,  | str,  | URL returned by the task worker | [optional] 
**error** | str,  | str,  | Error returned by task worker | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errorHistory

If any errors happened when processing this task, the list of errors identifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | If any errors happened when processing this task, the list of errors identifiers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

