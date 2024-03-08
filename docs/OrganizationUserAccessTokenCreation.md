# OrganizationUserAccessTokenCreation

Creation of a delegated API access token for an organization user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | [**List[AppScopes]**](AppScopes.md) | List of requested scopes for this credential | 

## Example

```python
from flat_api.models.organization_user_access_token_creation import OrganizationUserAccessTokenCreation

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUserAccessTokenCreation from a JSON string
organization_user_access_token_creation_instance = OrganizationUserAccessTokenCreation.from_json(json)
# print the JSON string representation of the object
print OrganizationUserAccessTokenCreation.to_json()

# convert the object into a dict
organization_user_access_token_creation_dict = organization_user_access_token_creation_instance.to_dict()
# create an instance of OrganizationUserAccessTokenCreation from a dict
organization_user_access_token_creation_form_dict = organization_user_access_token_creation.from_dict(organization_user_access_token_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


