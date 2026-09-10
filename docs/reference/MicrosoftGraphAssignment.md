# MicrosoftGraphAssignment

A Microsoft Teams assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the assignment assigned by Microsoft Teams | [optional] 
**state** | **str** | State of the assignment on Microsoft Teams.  * &#x60;draft&#x60;: Assignment is in draft mode * &#x60;scheduled&#x60;: Assignment is scheduled to be published at a future date * &#x60;published&#x60;: Assignment has been published to students * &#x60;assigned&#x60;: Assignment has been assigned (legacy status) * &#x60;inactive&#x60;: Assignment is inactive  | [optional] 
**alternate_link** | **str** | Absolute link to this assignment in the Microsoft Teams web UI | [optional] 
**assign_date_time** | **datetime** | The date when the assignment will become active on Microsoft Teams.  If set to a future date, the assignment will have status &#x60;scheduled&#x60; and won&#39;t be visible to students until this date.  | [optional] 
**categories** | **List[str]** | List of categories where this assignment is published under | [optional] 
**assign_to_type** | **str** | Recipient configuration for this assignment on Microsoft Teams.  * &#x60;class&#x60;: Assignment is visible to all students in the class * &#x60;individual&#x60;: Assignment is visible only to specific assigned students  | [optional] 
**assigned_students_ms_ids** | **List[str]** | When assignToType is &#39;individual&#39;, array of Microsoft Azure user IDs of students assigned to this assignment. These are the students who can see and submit to this assignment on Teams.  | [optional] 

## Example

```python
from flat_api.models.microsoft_graph_assignment import MicrosoftGraphAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftGraphAssignment from a JSON string
microsoft_graph_assignment_instance = MicrosoftGraphAssignment.from_json(json)
# print the JSON string representation of the object
print(MicrosoftGraphAssignment.to_json())

# convert the object into a dict
microsoft_graph_assignment_dict = microsoft_graph_assignment_instance.to_dict()
# create an instance of MicrosoftGraphAssignment from a dict
microsoft_graph_assignment_from_dict = MicrosoftGraphAssignment.from_dict(microsoft_graph_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


