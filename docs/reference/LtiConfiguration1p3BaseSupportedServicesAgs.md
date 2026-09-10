# LtiConfiguration1p3BaseSupportedServicesAgs

Assignment and Grade Services support

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether AGS claims were detected in launches from this platform | [optional] 
**version** | **str** | AGS version supported (e.g., \&quot;2.0\&quot;) | [optional] 
**enabled** | **bool** | Whether we have AGS enabled for this platform | [optional] 
**lineitems_url** | **str** | Base URL for line items operations as provided by the platform | [optional] 

## Example

```python
from flat_api.models.lti_configuration1p3_base_supported_services_ags import LtiConfiguration1p3BaseSupportedServicesAgs

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfiguration1p3BaseSupportedServicesAgs from a JSON string
lti_configuration1p3_base_supported_services_ags_instance = LtiConfiguration1p3BaseSupportedServicesAgs.from_json(json)
# print the JSON string representation of the object
print(LtiConfiguration1p3BaseSupportedServicesAgs.to_json())

# convert the object into a dict
lti_configuration1p3_base_supported_services_ags_dict = lti_configuration1p3_base_supported_services_ags_instance.to_dict()
# create an instance of LtiConfiguration1p3BaseSupportedServicesAgs from a dict
lti_configuration1p3_base_supported_services_ags_from_dict = LtiConfiguration1p3BaseSupportedServicesAgs.from_dict(lti_configuration1p3_base_supported_services_ags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


