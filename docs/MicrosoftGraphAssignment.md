# MicrosoftGraphAssignment

A Microsoft Teams asignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the assignement assigned by Microsoft Teams | [optional] 
**state** | **str** | State of the assignment | [optional] 
**alternate_link** | **str** | Absolute link to this assignement in the Microsoft Teams web UI | [optional] 
**categories** | **List[str]** | List of categories where this assignment is published under | [optional] 

## Example

```python
from flat_api.models.microsoft_graph_assignment import MicrosoftGraphAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftGraphAssignment from a JSON string
microsoft_graph_assignment_instance = MicrosoftGraphAssignment.from_json(json)
# print the JSON string representation of the object
print MicrosoftGraphAssignment.to_json()

# convert the object into a dict
microsoft_graph_assignment_dict = microsoft_graph_assignment_instance.to_dict()
# create an instance of MicrosoftGraphAssignment from a dict
microsoft_graph_assignment_form_dict = microsoft_graph_assignment.from_dict(microsoft_graph_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


