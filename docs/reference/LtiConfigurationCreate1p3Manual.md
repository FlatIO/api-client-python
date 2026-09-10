# LtiConfigurationCreate1p3Manual

LTI 1.3 manual configuration creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | LTI 1.3 manual creation mode | 
**platform_iss** | **str** | Platform issuer URL | [optional] 
**platform_name** | **str** | Platform display name | [optional] 
**client_id** | **str** | OAuth2 client_id allocated by the platform | [optional] 
**deployment_id** | **str** | Deployment identifier provided by the platform | [optional] 
**access_token_url** | **str** | Platform access token endpoint URL | [optional] 
**authorization_url** | **str** | Platform OIDC authorization endpoint URL | [optional] 
**jwks_url** | **str** | Platform JWKS endpoint URL for public keys | [optional] 
**enable_email_matching** | **bool** | Enable email-based user matching during LTI authentication | [optional] 

## Example

```python
from flat_api.models.lti_configuration_create1p3_manual import LtiConfigurationCreate1p3Manual

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationCreate1p3Manual from a JSON string
lti_configuration_create1p3_manual_instance = LtiConfigurationCreate1p3Manual.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationCreate1p3Manual.to_json())

# convert the object into a dict
lti_configuration_create1p3_manual_dict = lti_configuration_create1p3_manual_instance.to_dict()
# create an instance of LtiConfigurationCreate1p3Manual from a dict
lti_configuration_create1p3_manual_from_dict = LtiConfigurationCreate1p3Manual.from_dict(lti_configuration_create1p3_manual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


