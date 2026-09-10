# LtiConfigurationCreate1p3Dynamic

LTI 1.3 dynamic registration configuration creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | LTI 1.3 dynamic registration mode | 
**platform_info** | [**LtiConfigurationCreate1p3DynamicPlatformInfo**](LtiConfigurationCreate1p3DynamicPlatformInfo.md) |  | [optional] 
**locale** | **str** | Optional locale code for registration URL. Input values will be automatically normalized to a supported locale code. | [optional] 

## Example

```python
from flat_api.models.lti_configuration_create1p3_dynamic import LtiConfigurationCreate1p3Dynamic

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationCreate1p3Dynamic from a JSON string
lti_configuration_create1p3_dynamic_instance = LtiConfigurationCreate1p3Dynamic.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationCreate1p3Dynamic.to_json())

# convert the object into a dict
lti_configuration_create1p3_dynamic_dict = lti_configuration_create1p3_dynamic_instance.to_dict()
# create an instance of LtiConfigurationCreate1p3Dynamic from a dict
lti_configuration_create1p3_dynamic_from_dict = LtiConfigurationCreate1p3Dynamic.from_dict(lti_configuration_create1p3_dynamic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


