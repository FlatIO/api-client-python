# LtiConfigurationCreate1p3DynamicPlatformInfo

Optional platform information for dynamic registration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Platform display name | [optional] 
**url** | **str** | Optional platform homepage or admin URL for reference | [optional] 

## Example

```python
from flat_api.models.lti_configuration_create1p3_dynamic_platform_info import LtiConfigurationCreate1p3DynamicPlatformInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationCreate1p3DynamicPlatformInfo from a JSON string
lti_configuration_create1p3_dynamic_platform_info_instance = LtiConfigurationCreate1p3DynamicPlatformInfo.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationCreate1p3DynamicPlatformInfo.to_json())

# convert the object into a dict
lti_configuration_create1p3_dynamic_platform_info_dict = lti_configuration_create1p3_dynamic_platform_info_instance.to_dict()
# create an instance of LtiConfigurationCreate1p3DynamicPlatformInfo from a dict
lti_configuration_create1p3_dynamic_platform_info_from_dict = LtiConfigurationCreate1p3DynamicPlatformInfo.from_dict(lti_configuration_create1p3_dynamic_platform_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


