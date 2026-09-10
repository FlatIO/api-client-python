# LtiConfiguration1p3Manual


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Configuration ID | 
**lti_version** | **str** | LTI version (1.3) | 
**organization_id** | **str** | Organization ID | [optional] 
**organization_name** | **str** | Organization name | [optional] 
**creator_id** | **str** | ID of the user who created this configuration | [optional] 
**creation_date** | **datetime** | Configuration creation date | 
**last_used_date** | **datetime** | Last time this configuration was used | [optional] 
**status** | **str** | Configuration status indicator | [optional] 
**mode** | **str** | Manual LTI 1.3 configuration mode | [optional] 
**platform_iss** | **str** | Platform issuer URL | [optional] 
**platform_name** | **str** | Platform display name | [optional] 
**client_id** | **str** | OAuth2 client_id allocated by the platform | [optional] 
**deployment_id** | **str** | Deployment ID linking the tool to a tenant/class (varies by platform) | [optional] 
**access_token_url** | **str** | OAuth2 token endpoint (for AGS/NRPS) | [optional] 
**authorization_url** | **str** | OIDC authorization/login endpoint | [optional] 
**jwks_url** | **str** | Platform JWKS endpoint (public keys) | [optional] 
**deployment_mode** | **str** | Deployment mode (single for organization-specific, multi for shared parent platforms) | [optional] 
**supported_services** | [**LtiConfiguration1p3BaseSupportedServices**](LtiConfiguration1p3BaseSupportedServices.md) |  | [optional] 
**tool** | [**LtiConfiguration1p3BaseTool**](LtiConfiguration1p3BaseTool.md) |  | [optional] 
**public_keyset_url** | **str** | Public keyset URL for the platform to retrieve Flat&#39;s public keys | [optional] 
**initiate_login_url** | **str** | URL for the platform to initiate LTI login | [optional] 
**redirect_uris** | **List[str]** | Allowed redirect URIs for LTI launches | [optional] 
**enable_email_matching** | **bool** | Enable email-based user matching during LTI authentication.  When true (default): If a user with the same email exists in the organization, they will be matched and logged in instead of creating a new account.  When false: Email matching is disabled. Only LTI ID matching is used, which means multiple LTI users can share the same email address and have separate Flat accounts. This is useful for cases like siblings sharing a parent email in the LMS.  | [optional] [default to True]

## Example

```python
from flat_api.models.lti_configuration1p3_manual import LtiConfiguration1p3Manual

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfiguration1p3Manual from a JSON string
lti_configuration1p3_manual_instance = LtiConfiguration1p3Manual.from_json(json)
# print the JSON string representation of the object
print(LtiConfiguration1p3Manual.to_json())

# convert the object into a dict
lti_configuration1p3_manual_dict = lti_configuration1p3_manual_instance.to_dict()
# create an instance of LtiConfiguration1p3Manual from a dict
lti_configuration1p3_manual_from_dict = LtiConfiguration1p3Manual.from_dict(lti_configuration1p3_manual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


