# flat_api.model.api_access_token.ApiAccessToken

An API access token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An API access token | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of this private token | [optional] 
**name** | str,  | str,  | Name of the personal access token | [optional] 
**token** | str,  | str,  | The token. This token will only be returned once, then only the first 4 characters will be returned.  | [optional] 
**issuedDate** | str, datetime,  | str,  | The date then this token was issued  | [optional] value must conform to RFC-3339 date-time
**expirationDate** | str, datetime,  | str,  | The date then this token will expire  | [optional] value must conform to RFC-3339 date-time
**[scopes](#scopes)** | list, tuple,  | tuple,  | The list of scopes associated to the token  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scopes

The list of scopes associated to the token 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of scopes associated to the token  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AppScopes**](AppScopes.md) | [**AppScopes**](AppScopes.md) | [**AppScopes**](AppScopes.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

