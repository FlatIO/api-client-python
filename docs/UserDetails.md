# UserDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user unique identifier | 
**type** | **str** | The type of user account | 
**product** | [**TutteoProduct**](TutteoProduct.md) |  | 
**username** | **str** | The user name (unique for the organization) | 
**printable_name** | **str** | The name that can be directly printed (name, firstname &amp; lastname, or username) | [optional] 
**firstname** | **str** | Firstname of the user (for education users) | [optional] 
**lastname** | **str** | Lastname of the user (for education users) | [optional] 
**name** | **str** | A displayable name for the user (for consumer users) | [optional] 
**picture** | **str** | The URL of the picture to display | 
**badges** | **List[str]** | List of badges for the user profile:  - &#x60;power&#x60; - &#x60;staff&#x60; - &#x60;composerOfTheMonth&#x60; - &#x60;ambassador&#x60; - &#x60;challenge&#x60;  | [optional] 
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
**instruments** | **List[str]** | An array of the instrument identifiers. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  | [optional] 
**links** | [**UserCommunityProfileLinks**](UserCommunityProfileLinks.md) |  | [optional] 
**azure_details** | [**UserAzureDetails**](UserAzureDetails.md) |  | [optional] 
**private_profile** | **bool** | Tell either this user profile is private or not (individual accounts only) | [optional] 
**locale** | [**FlatLocales**](FlatLocales.md) |  | [optional] 
**groups** | **List[str]** | For Flat for Education accounts, list of Group identifiers the user is part of. | [optional] 
**picture_file** | **str** | The ID of the user profile picture | [optional] 
**cover_picture_file** | **str** | The ID of the user profile cover picture | [optional] 

## Example

```python
from flat_api.models.user_details import UserDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetails from a JSON string
user_details_instance = UserDetails.from_json(json)
# print the JSON string representation of the object
print UserDetails.to_json()

# convert the object into a dict
user_details_dict = user_details_instance.to_dict()
# create an instance of UserDetails from a dict
user_details_form_dict = user_details.from_dict(user_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


