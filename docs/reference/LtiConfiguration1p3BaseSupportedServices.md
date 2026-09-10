# LtiConfiguration1p3BaseSupportedServices

LTI services support information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ags** | [**LtiConfiguration1p3BaseSupportedServicesAgs**](LtiConfiguration1p3BaseSupportedServicesAgs.md) |  | [optional] 
**nrps** | [**LtiConfiguration1p3BaseSupportedServicesNrps**](LtiConfiguration1p3BaseSupportedServicesNrps.md) |  | [optional] 
**deep_linking** | [**LtiConfiguration1p3BaseSupportedServicesDeepLinking**](LtiConfiguration1p3BaseSupportedServicesDeepLinking.md) |  | [optional] 

## Example

```python
from flat_api.models.lti_configuration1p3_base_supported_services import LtiConfiguration1p3BaseSupportedServices

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfiguration1p3BaseSupportedServices from a JSON string
lti_configuration1p3_base_supported_services_instance = LtiConfiguration1p3BaseSupportedServices.from_json(json)
# print the JSON string representation of the object
print(LtiConfiguration1p3BaseSupportedServices.to_json())

# convert the object into a dict
lti_configuration1p3_base_supported_services_dict = lti_configuration1p3_base_supported_services_instance.to_dict()
# create an instance of LtiConfiguration1p3BaseSupportedServices from a dict
lti_configuration1p3_base_supported_services_from_dict = LtiConfiguration1p3BaseSupportedServices.from_dict(lti_configuration1p3_base_supported_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


