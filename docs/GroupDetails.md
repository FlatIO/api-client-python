# GroupDetails

The details of a group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the group | [optional] 
**name** | **str** | The displayable name of the group | [optional] 
**type** | [**GroupType**](GroupType.md) |  | [optional] 
**organization** | **str** | The unique identifier of the Organization owning the group | [optional] 
**creation_date** | **datetime** | The date when the group was create | [optional] 
**users_count** | **float** | The number of students in this group | [optional] 
**read_only** | **bool** | &#x60;true&#x60; if the properties and members of this group are in in read-only  | [optional] 

## Example

```python
from flat_api.models.group_details import GroupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDetails from a JSON string
group_details_instance = GroupDetails.from_json(json)
# print the JSON string representation of the object
print GroupDetails.to_json()

# convert the object into a dict
group_details_dict = group_details_instance.to_dict()
# create an instance of GroupDetails from a dict
group_details_form_dict = group_details.from_dict(group_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


