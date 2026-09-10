# LtiConfiguration1p3BaseSupportedServicesNrps

Names and Role Provisioning Services support

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether NRPS claims were detected in launches from this platform | [optional] 
**version** | **str** | NRPS version supported (e.g., \&quot;2.0\&quot;) | [optional] 
**enabled** | **bool** | Whether we have NRPS enabled for this platform | [optional] 

## Example

```python
from flat_api.models.lti_configuration1p3_base_supported_services_nrps import LtiConfiguration1p3BaseSupportedServicesNrps

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfiguration1p3BaseSupportedServicesNrps from a JSON string
lti_configuration1p3_base_supported_services_nrps_instance = LtiConfiguration1p3BaseSupportedServicesNrps.from_json(json)
# print the JSON string representation of the object
print(LtiConfiguration1p3BaseSupportedServicesNrps.to_json())

# convert the object into a dict
lti_configuration1p3_base_supported_services_nrps_dict = lti_configuration1p3_base_supported_services_nrps_instance.to_dict()
# create an instance of LtiConfiguration1p3BaseSupportedServicesNrps from a dict
lti_configuration1p3_base_supported_services_nrps_from_dict = LtiConfiguration1p3BaseSupportedServicesNrps.from_dict(lti_configuration1p3_base_supported_services_nrps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


