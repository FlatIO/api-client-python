# GroupCreation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of group (currently only classStudentsSubGroup is supported) | 
**classroom** | **str** | Classroom ID | 
**name** | **str** | Name of the group (optional - auto-generated if not provided).  **Special names:**  * &#x60;edu:testing-students&#x60;: Creates a group tagged for test student accounts. The display name will be localized (e.g., \&quot;Test Students\&quot;) and the group will be tagged with &#x60;edu:testing-students&#x60;.  | [optional] 
**members** | **List[str]** | Array of student IDs to add to the group | [optional] 

## Example

```python
from flat_api.models.group_creation import GroupCreation

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCreation from a JSON string
group_creation_instance = GroupCreation.from_json(json)
# print the JSON string representation of the object
print(GroupCreation.to_json())

# convert the object into a dict
group_creation_dict = group_creation_instance.to_dict()
# create an instance of GroupCreation from a dict
group_creation_from_dict = GroupCreation.from_dict(group_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


