# UserDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The user name (unique for the organization) | [optional] 
**class_role** | [**ClassRoles**](ClassRoles.md) |  | [optional] 
**private_profile** | **bool** | Tell either this user profile is private or not (individual accounts only) | [optional] 
**followers_count** | **int** | Number of followers the user have | [optional] 
**firstname** | **str** | Firstname of the user (for education users) | [optional] 
**is_power_user** | **bool** | User license status. &#39;true&#39; if user is an individual Power user | [optional] 
**locale** | [**FlatLocales**](FlatLocales.md) |  | [optional] 
**instruments** | **list[str]** | An array of the instrument identifiers. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  | [optional] 
**html_url** | **str** | Link to user profile (for Indiv. users only) | [optional] 
**liked_scores_count** | **int** | Number of the scores liked by the user | [optional] 
**printable_name** | **str** | The name that can be directly printed (name, firstname &amp; lastname, or username) | [optional] 
**bio** | **str** | User&#39;s biography | [optional] 
**picture_file** | **str** | The ID of the user profile picture | [optional] 
**id** | **str** | Identifier of the user | [optional] 
**cover_picture_file** | **str** | The ID of the user profile cover picture | [optional] 
**picture** | **str** | The URL of the picture to display | [optional] 
**name** | **str** | A displayable name for the user (for consumer users) | [optional] 
**is_flat_team** | **bool** | Will be &#39;true&#39; if user is part of the Flat Team | [optional] 
**organization_role** | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**profile_theme** | **str** | Theme (background) for the profile | [optional] 
**cover_picture** | **str** | Cover picture (backgroud) for the profile | [optional] 
**owned_public_scores_count** | **int** | Number of public scores the user have | [optional] 
**lastname** | **str** | Lastname of the user (for education users) | [optional] 
**following_count** | **int** | Number of people the user follow | [optional] 
**organization** | **str** | Organization ID (for Edu users only) | [optional] 
**type** | **str** | The type of account | [optional] 
**registration_date** | **datetime** | Date the user signed up | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


