# Group

A group of users

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the group | [optional] 
**name** | **str** | The display name of the group | [optional] 
**type** | **str** | The type of the group: * &#x60;generic&#x60;: A group created by a Flat user * &#x60;classTeachers&#x60;: A group created automaticaly by Flat that contains   the teachers of a class * &#x60;classStudents&#x60;: A group created automaticaly by Flat that contains   the studnets of a class  | [optional] 
**users_count** | **float** | The number of users in this group | [optional] 
**read_only** | **bool** | &#x60;True&#x60; if the group is set in read-only  | [optional] 
**organization** | **str** | If the group is related to an organization, this field will contain the unique identifier of the organization  | [optional] 
**creation_date** | **datetime** | The creation date of the group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

