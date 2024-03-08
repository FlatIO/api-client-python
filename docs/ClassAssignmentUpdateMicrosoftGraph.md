# ClassAssignmentUpdateMicrosoftGraph

Microsoft Graph options for this assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | List of categories this assignment belongs to | [optional] 

## Example

```python
from flat_api.models.class_assignment_update_microsoft_graph import ClassAssignmentUpdateMicrosoftGraph

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAssignmentUpdateMicrosoftGraph from a JSON string
class_assignment_update_microsoft_graph_instance = ClassAssignmentUpdateMicrosoftGraph.from_json(json)
# print the JSON string representation of the object
print ClassAssignmentUpdateMicrosoftGraph.to_json()

# convert the object into a dict
class_assignment_update_microsoft_graph_dict = class_assignment_update_microsoft_graph_instance.to_dict()
# create an instance of ClassAssignmentUpdateMicrosoftGraph from a dict
class_assignment_update_microsoft_graph_form_dict = class_assignment_update_microsoft_graph.from_dict(class_assignment_update_microsoft_graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


