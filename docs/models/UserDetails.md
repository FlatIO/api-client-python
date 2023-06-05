# flat_api.model.user_details.UserDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Identifier of the user | [optional] 
**type** | str,  | str,  | The type of account | [optional] must be one of ["user", "guest", ] 
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
**bio** | str,  | str,  | User&#x27;s biography | [optional] 
**registrationDate** | str, datetime,  | str,  | Date the user signed up | [optional] value must conform to RFC-3339 date-time
**likedScoresCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of the scores liked by the user | [optional] 
**followersCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of followers the user have | [optional] 
**followingCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of people the user follow | [optional] 
**ownedPublicScoresCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of public scores the user have | [optional] 
**coverPicture** | str,  | str,  | Cover picture (backgroud) for the profile | [optional] 
**profileTheme** | str,  | str,  | Theme (background) for the profile | [optional] 
**[instruments](#instruments)** | list, tuple,  | tuple,  | An array of the instrument identifiers. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  | [optional] 
**links** | [**UserCommunityProfileLinks**](UserCommunityProfileLinks.md) | [**UserCommunityProfileLinks**](UserCommunityProfileLinks.md) |  | [optional] 
**azureDetails** | [**UserAzureDetails**](UserAzureDetails.md) | [**UserAzureDetails**](UserAzureDetails.md) |  | [optional] 
**privateProfile** | bool,  | BoolClass,  | Tell either this user profile is private or not (individual accounts only) | [optional] 
**locale** | [**FlatLocales**](FlatLocales.md) | [**FlatLocales**](FlatLocales.md) |  | [optional] 
**[groups](#groups)** | list, tuple,  | tuple,  | For Flat for Education accounts, list of Group identifiers the user is part of. | [optional] 
**pictureFile** | None, str,  | NoneClass, str,  | The ID of the user profile picture | [optional] 
**coverPictureFile** | None, str,  | NoneClass, str,  | The ID of the user profile cover picture | [optional] 
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

# instruments

An array of the instrument identifiers. The format of the strings is `{instrument-group}.{instrument-id}`. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of the instrument identifiers. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

