# GroupDetails

The details of a group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the group | 
**name** | **str** | The displayable name of the group | 
**type** | [**GroupType**](GroupType.md) |  | 
**organization** | **str** | The unique identifier of the Organization owning the group | [optional] 
**classroom** | **str** | The unique identifier of the classroom owning the group. Only available for groups of type &#39;classromStudentsSubGroup&#39; or &#39;assignmentStudentsSubGroup&#39; | [optional] 
**assignment** | **str** | The unique identifier of the assignment owning the group. Only available for groups of type &#39;assignmentStudentsSubGroup&#39;. | [optional] 
**parent** | **str** | The unique identifier of the parent class group. Only available for groups of type &#39;assignmentStudentsSubGroup&#39;. May be null if the parent class group was deleted. | [optional] 
**creation_date** | **datetime** | The date when the group was create | 
**users_count** | **float** | The number of students in this group | 
**read_only** | **bool** | &#x60;true&#x60; if the properties and members of this group are in in read-only  | 
**tags** | **List[str]** | Tags for categorizing groups.  * &#x60;edu:testing-students&#x60;: Marks this group as containing test student accounts  | 

## Example

```python
from flat_api.models.group_details import GroupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDetails from a JSON string
group_details_instance = GroupDetails.from_json(json)
# print the JSON string representation of the object
print(GroupDetails.to_json())

# convert the object into a dict
group_details_dict = group_details_instance.to_dict()
# create an instance of GroupDetails from a dict
group_details_from_dict = GroupDetails.from_dict(group_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


