# LtiConfigurationUpdate

Update an existing LTI 1.3 configuration (deployment clone or standalone)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** | Deployment identifier provided by the platform | [optional] 
**deployment_breakdown_id** | **str** | Specific tenant identifier for multi-tenant platforms | [optional] 
**enable_email_matching** | **bool** | Enable email-based user matching during LTI authentication | [optional] 
**platform_iss** | **str** | Platform issuer URL | [optional] 
**platform_name** | **str** | Platform display name | [optional] 
**client_id** | **str** | OAuth2 client_id allocated by the platform | [optional] 
**access_token_url** | **str** | Platform access token endpoint URL | [optional] 
**authorization_url** | **str** | Platform OIDC authorization endpoint URL | [optional] 
**jwks_url** | **str** | Platform JWKS endpoint URL for public keys | [optional] 

## Example

```python
from flat_api.models.lti_configuration_update import LtiConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationUpdate from a JSON string
lti_configuration_update_instance = LtiConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationUpdate.to_json())

# convert the object into a dict
lti_configuration_update_dict = lti_configuration_update_instance.to_dict()
# create an instance of LtiConfigurationUpdate from a dict
lti_configuration_update_from_dict = LtiConfigurationUpdate.from_dict(lti_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


