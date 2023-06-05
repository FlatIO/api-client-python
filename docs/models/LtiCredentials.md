# flat_api.model.lti_credentials.LtiCredentials

A couple of LTI 1.x OAuth credentials

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A couple of LTI 1.x OAuth credentials | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier of this couple of credentials | [optional] 
**name** | str,  | str,  | Name of the couple of credentials | [optional] 
**lms** | [**LmsName**](LmsName.md) | [**LmsName**](LmsName.md) |  | [optional] 
**organization** | str,  | str,  | The unique identifier of the Organization associated to these credentials | [optional] 
**creator** | str,  | str,  | Unique identifier of the user who created these credentials | [optional] 
**creationDate** | str, datetime,  | str,  | The creation date of thse credentials | [optional] value must conform to RFC-3339 date-time
**lastUsage** | str, datetime,  | str,  | The last time these credentials were used | [optional] value must conform to RFC-3339 date-time
**consumerKey** | str,  | str,  | OAuth 1 Consumer Key | [optional] 
**consumerSecret** | str,  | str,  | OAuth 1 Consumer Secret | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

