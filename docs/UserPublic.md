# UserPublic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user unique identifier | [optional] 
**type** | **str** | The type of user account | [optional] 
**username** | **str** | The user name (unique for the organization) | [optional] 
**printable_name** | **str** | The name that can be directly printed (name, firstname &amp; lastname, or username) | [optional] 
**firstname** | **str** | Firstname of the user (for education users) | [optional] 
**lastname** | **str** | Lastname of the user (for education users) | [optional] 
**name** | **str** | A displayable name for the user (for consumer users) | [optional] 
**picture** | **str, none_type** | The URL of the picture to display | [optional] 
**badges** | **[str]** | List of badges for the user profile | [optional] 
**organization** | **str** | Organization ID (for Edu users only) | [optional] 
**organization_role** | [**OrganizationRoles**](OrganizationRoles.md) |  | [optional] 
**class_role** | [**ClassRoles**](ClassRoles.md) |  | [optional] 
**html_url** | **str** | Link to user profile (for Indiv. users only) | [optional] 
**bio** | **str** | User&#39;s biography | [optional] 
**registration_date** | **datetime** | Date the user signed up | [optional] 
**liked_scores_count** | **int** | Number of the scores liked by the user | [optional] 
**followers_count** | **int** | Number of followers the user have | [optional] 
**following_count** | **int** | Number of people the user follow | [optional] 
**owned_public_scores_count** | **int** | Number of public scores the user have | [optional] 
**cover_picture** | **str** | Cover picture (backgroud) for the profile | [optional] 
**profile_theme** | **str** | Theme (background) for the profile | [optional] 
**instruments** | **[str]** | An array of the instrument identifiers. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  | [optional] 
**links** | [**UserCommunityProfileLinks**](UserCommunityProfileLinks.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


