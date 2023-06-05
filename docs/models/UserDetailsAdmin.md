# flat_api.model.user_details_admin.UserDetailsAdmin

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The user unique identifier | [optional] 
**type** | str,  | str,  | The type of user account | [optional] must be one of ["user", "guest", ] 
**username** | str,  | str,  | The user name (unique for the organization) | [optional] 
**printableName** | str,  | str,  | The name that can be directly printed (name, firstname &amp; lastname, or username) | [optional] 
**firstname** | str,  | str,  | Firstname of the user (for education users) | [optional] 
**lastname** | str,  | str,  | Lastname of the user (for education users) | [optional] 
**name** | str,  | str,  | A displayable name for the user (for consumer users) | [optional] 
**picture** | None, str,  | NoneClass, str,  | The URL of the picture to display | [optional] 
**[badges](#badges)** | list, tuple,  | tuple,  | List of badges for the user profile | [optional] 
**organization** | str,  | str,  | Organization ID (for Edu users only) | [optional] 
**organizationRole** | [**OrganizationRoles**](OrganizationRoles.md) | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**classRole** | [**ClassRoles**](ClassRoles.md) | [**ClassRoles**](ClassRoles.md) |  | [optional] 
**htmlUrl** | str,  | str,  | Link to user profile (for Indiv. users only) | [optional] 
**email** | str,  | str,  | Email of the user | [optional] 
**lastActivityDate** | str, datetime,  | str,  | Date of the last user activity | [optional] value must conform to RFC-3339 date-time
**[license](#license)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Current active license of the user | [optional] 
**[groups](#groups)** | list, tuple,  | tuple,  | For Flat for Education accounts, list of Group identifiers the user is part of. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# badges

List of badges for the user profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of badges for the user profile | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Badge name, e.g. &#x60;power&#x60;, &#x60;staff&#x60;, &#x60;composerOfTheMonth&#x60; | 

# license

Current active license of the user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Current active license of the user | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | ID of the current license | [optional] 
**expirationDate** | str, datetime,  | str,  | Date when the license expires | [optional] value must conform to RFC-3339 date-time
**source** | [**LicenseSources**](LicenseSources.md) | [**LicenseSources**](LicenseSources.md) |  | [optional] 
**mode** | [**LicenseMode**](LicenseMode.md) | [**LicenseMode**](LicenseMode.md) |  | [optional] 
**active** | bool,  | BoolClass,  | ID of the current license | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# groups

For Flat for Education accounts, list of Group identifiers the user is part of.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | For Flat for Education accounts, list of Group identifiers the user is part of. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Unique group identifier | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
