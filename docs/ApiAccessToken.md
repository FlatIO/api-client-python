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
**scopes** | [**[AppScopes]**](AppScopes.md) | The list of scopes associated to the token  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


