# LtiConfigurationCreate1p1

LTI 1.1 manual configuration creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | LTI 1.1 manual creation mode | 
**name** | **str** | Display name for LTI 1.1 credentials | [optional] 
**lms** | **str** | LMS identifier for LTI 1.1 credentials | [optional] 

## Example

```python
from flat_api.models.lti_configuration_create1p1 import LtiConfigurationCreate1p1

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationCreate1p1 from a JSON string
lti_configuration_create1p1_instance = LtiConfigurationCreate1p1.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationCreate1p1.to_json())

# convert the object into a dict
lti_configuration_create1p1_dict = lti_configuration_create1p1_instance.to_dict()
# create an instance of LtiConfigurationCreate1p1 from a dict
lti_configuration_create1p1_from_dict = LtiConfigurationCreate1p1.from_dict(lti_configuration_create1p1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


