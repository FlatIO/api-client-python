# AssignmentGroup

A group assigned to an assignment for shared writing assignments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the group | 
**name** | **str** | The display name of the group | 
**parent** | **str** | The unique identifier of the parent class group. Only available for groups of type &#39;assignmentStudentsSubGroup&#39;. May be null if the parent class group was deleted. | [optional] 
**members** | **List[str]** | Array of user IDs that are members of this group | 

## Example

```python
from flat_api.models.assignment_group import AssignmentGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentGroup from a JSON string
assignment_group_instance = AssignmentGroup.from_json(json)
# print the JSON string representation of the object
print(AssignmentGroup.to_json())

# convert the object into a dict
assignment_group_dict = assignment_group_instance.to_dict()
# create an instance of AssignmentGroup from a dict
assignment_group_from_dict = AssignmentGroup.from_dict(assignment_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


