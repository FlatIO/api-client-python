# EduResource

A Flat for Education resource contained in a resources library

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource unique identifier | 
**type** | [**EduResourceType**](EduResourceType.md) |  | 
**title** | **str** | Title of the resource | 
**capabilities** | [**EduResourceCapabilities**](EduResourceCapabilities.md) |  | 
**creator** | **str** | The User identifier of the resource creator | [optional] 
**privacy** | [**EduResourcePrivacy**](EduResourcePrivacy.md) |  | [optional] 
**tags** | **[str]** | Specific attributes for the resource (e.g. sample resources with custom design) | [optional] 
**parent** | **str** | Identifier of the parent resource, e.g. a folder or root | [optional] 
**creation_date** | **datetime** | The date when the resource was created | [optional] 
**update_date** | **datetime** | The date when the resource was updated | [optional] 
**resource** | [**EduResourceResource**](EduResourceResource.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


