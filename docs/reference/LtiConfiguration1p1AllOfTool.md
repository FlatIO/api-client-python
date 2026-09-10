# LtiConfiguration1p1AllOfTool

Platform/tool product information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Product family code (e.g., canvas, moodle, schoology) | [optional] 
**version** | **str** | Platform version string | [optional] 
**instance_name** | **str** | Instance display name | [optional] 
**instance_guid** | **str** | Unique instance identifier | [optional] 
**instance_contact** | **str** | Contact email or handle for the instance | [optional] 
**instance_domain** | **str** | Instance root domain | [optional] 

## Example

```python
from flat_api.models.lti_configuration1p1_all_of_tool import LtiConfiguration1p1AllOfTool

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfiguration1p1AllOfTool from a JSON string
lti_configuration1p1_all_of_tool_instance = LtiConfiguration1p1AllOfTool.from_json(json)
# print the JSON string representation of the object
print(LtiConfiguration1p1AllOfTool.to_json())

# convert the object into a dict
lti_configuration1p1_all_of_tool_dict = lti_configuration1p1_all_of_tool_instance.to_dict()
# create an instance of LtiConfiguration1p1AllOfTool from a dict
lti_configuration1p1_all_of_tool_from_dict = LtiConfiguration1p1AllOfTool.from_dict(lti_configuration1p1_all_of_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


