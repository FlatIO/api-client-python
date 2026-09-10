# LtiConfigurationCreate

Request to create a new LTI configuration (unified 1.1 and 1.3)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | LTI 1.3 manual creation mode | 
**name** | **str** | Display name for LTI 1.1 credentials | [optional] 
**lms** | **str** | LMS identifier for LTI 1.1 credentials | [optional] 
**platform_info** | [**LtiConfigurationCreate1p3DynamicPlatformInfo**](LtiConfigurationCreate1p3DynamicPlatformInfo.md) |  | [optional] 
**locale** | **str** | Optional locale code for registration URL. Input values will be automatically normalized to a supported locale code. | [optional] 
**deployment_type** | **str** | Parent platform key (e.g., canvas, blackboard, schoology, classlink) | 
**deployment_id** | **str** | Deployment identifier provided by the platform | 
**client_id** | **str** | OAuth2 client_id allocated by the platform | [optional] 
**deployment_breakdown_id** | **str** | Value of the custom claim that identifies this specific tenant (for multi-tenant platforms like Schoology) | [optional] 
**platform_iss** | **str** | Platform issuer URL | [optional] 
**platform_name** | **str** | Platform display name | [optional] 
**access_token_url** | **str** | Platform access token endpoint URL | [optional] 
**authorization_url** | **str** | Platform OIDC authorization endpoint URL | [optional] 
**jwks_url** | **str** | Platform JWKS endpoint URL for public keys | [optional] 
**enable_email_matching** | **bool** | Enable email-based user matching during LTI authentication | [optional] 

## Example

```python
from flat_api.models.lti_configuration_create import LtiConfigurationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationCreate from a JSON string
lti_configuration_create_instance = LtiConfigurationCreate.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationCreate.to_json())

# convert the object into a dict
lti_configuration_create_dict = lti_configuration_create_instance.to_dict()
# create an instance of LtiConfigurationCreate from a dict
lti_configuration_create_from_dict = LtiConfigurationCreate.from_dict(lti_configuration_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


