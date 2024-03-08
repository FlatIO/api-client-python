# ApiAccessToken

An API access token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of this private token | [optional] 
**name** | **str** | Name of the personal access token | [optional] 
**token** | **str** | The token. This token will only be returned once, then only the first 4 characters will be returned.  | [optional] 
**issued_date** | **datetime** | The date then this token was issued  | [optional] 
**expiration_date** | **datetime** | The date then this token will expire  | [optional] 
**scopes** | [**List[AppScopes]**](AppScopes.md) | The list of scopes associated to the token  | [optional] 

## Example

```python
from flat_api.models.api_access_token import ApiAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAccessToken from a JSON string
api_access_token_instance = ApiAccessToken.from_json(json)
# print the JSON string representation of the object
print ApiAccessToken.to_json()

# convert the object into a dict
api_access_token_dict = api_access_token_instance.to_dict()
# create an instance of ApiAccessToken from a dict
api_access_token_form_dict = api_access_token.from_dict(api_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


