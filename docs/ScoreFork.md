# ScoreFork

Options to fork the score

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str, none_type** | Unique identifier of a collection where the score will be copied. If no collection identifier is provided, the score will be stored in the &#x60;root&#x60; directory. If null is provided, the score won&#39;t be added to any collections  | [optional]  if omitted the server will use the default value of "root"
**keep_original_title** | **bool** | Option to keep the original title of the score (i.e. don&#39;t prepend it with \&quot;Copy of \&quot;, or add the student name in assignment usage).  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


