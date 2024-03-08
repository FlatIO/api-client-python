# ClassDetailsIssues

Detected issues for this class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync** | [**List[ClassDetailsIssuesSyncInner]**](ClassDetailsIssuesSyncInner.md) | Synchronization issues for the class | [optional] 

## Example

```python
from flat_api.models.class_details_issues import ClassDetailsIssues

# TODO update the JSON string below
json = "{}"
# create an instance of ClassDetailsIssues from a JSON string
class_details_issues_instance = ClassDetailsIssues.from_json(json)
# print the JSON string representation of the object
print ClassDetailsIssues.to_json()

# convert the object into a dict
class_details_issues_dict = class_details_issues_instance.to_dict()
# create an instance of ClassDetailsIssues from a dict
class_details_issues_form_dict = class_details_issues.from_dict(class_details_issues_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


