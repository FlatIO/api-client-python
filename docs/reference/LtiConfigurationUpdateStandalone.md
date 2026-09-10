# LtiConfigurationUpdateStandalone

Update fields allowed for standalone (manual/dynamic) configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** | Deployment identifier provided by the platform | [optional] 
**platform_iss** | **str** | Platform issuer URL | [optional] 
**platform_name** | **str** | Platform display name | [optional] 
**client_id** | **str** | OAuth2 client_id allocated by the platform | [optional] 
**access_token_url** | **str** | Platform access token endpoint URL | [optional] 
**authorization_url** | **str** | Platform OIDC authorization endpoint URL | [optional] 
**jwks_url** | **str** | Platform JWKS endpoint URL for public keys | [optional] 
**enable_email_matching** | **bool** | Enable email-based user matching during LTI authentication | [optional] 

## Example

```python
from flat_api.models.lti_configuration_update_standalone import LtiConfigurationUpdateStandalone

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationUpdateStandalone from a JSON string
lti_configuration_update_standalone_instance = LtiConfigurationUpdateStandalone.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationUpdateStandalone.to_json())

# convert the object into a dict
lti_configuration_update_standalone_dict = lti_configuration_update_standalone_instance.to_dict()
# create an instance of LtiConfigurationUpdateStandalone from a dict
lti_configuration_update_standalone_from_dict = LtiConfigurationUpdateStandalone.from_dict(lti_configuration_update_standalone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


