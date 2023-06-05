# ScoreCommentContext

The context of the comment (for inline/contextualized comments). A context will include all the information related to the location of the comment (i.e. score parts, range of measure, time position). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_uuid** | **str** | The unique identifier (UUID) of the score part | 
**measure_uuids** | **[str]** | The list of measure UUIds | 
**start_time_pos** | **float** |  | 
**stop_time_pos** | **float** |  | 
**start_dpq** | **float** |  | 
**stop_dpq** | **float** |  | 
**staff_idx** | **float** | (Deprecated, use &#x60;staffUuid&#x60;) The identififer of the staff | [optional] 
**staff_uuid** | **str** | The unique identififer (UUID) of the staff | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


