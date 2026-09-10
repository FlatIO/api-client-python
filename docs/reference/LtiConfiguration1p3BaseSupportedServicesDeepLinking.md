# LtiConfiguration1p3BaseSupportedServicesDeepLinking

Deep Linking support

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether Deep Linking claims were detected in launches from this platform | [optional] 
**version** | **str** | Deep Linking version supported (e.g., \&quot;2.0\&quot;) | [optional] 

## Example

```python
from flat_api.models.lti_configuration1p3_base_supported_services_deep_linking import LtiConfiguration1p3BaseSupportedServicesDeepLinking

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfiguration1p3BaseSupportedServicesDeepLinking from a JSON string
lti_configuration1p3_base_supported_services_deep_linking_instance = LtiConfiguration1p3BaseSupportedServicesDeepLinking.from_json(json)
# print the JSON string representation of the object
print(LtiConfiguration1p3BaseSupportedServicesDeepLinking.to_json())

# convert the object into a dict
lti_configuration1p3_base_supported_services_deep_linking_dict = lti_configuration1p3_base_supported_services_deep_linking_instance.to_dict()
# create an instance of LtiConfiguration1p3BaseSupportedServicesDeepLinking from a dict
lti_configuration1p3_base_supported_services_deep_linking_from_dict = LtiConfiguration1p3BaseSupportedServicesDeepLinking.from_dict(lti_configuration1p3_base_supported_services_deep_linking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


