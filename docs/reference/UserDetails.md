# UserDetails

User details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user unique identifier | 
**type** | **str** | The type of user account | 
**product** | [**TutteoProduct**](TutteoProduct.md) |  | [default to TutteoProduct.FLAT]
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
**all_public_scores_count** | **int** | Total number of public scores the user participates in (owned + joined) | [optional] 
**likes_count** | **int** | Number of likes on the user published scores | [optional] 
**plays_count** | **int** | Number of plays on the user published scores | [optional] 
**cover_picture** | **str** | Cover picture (backgroud) for the profile | [optional] 
**profile_theme** | **str** | Theme (background) for the profile | [optional] 
**links** | [**UserCommunityProfileLinks**](UserCommunityProfileLinks.md) |  | [optional] 
**is_email_verified** | **bool** | Whether the user&#39;s email address has been verified | [optional] 
**azure_details** | [**UserAzureDetails**](UserAzureDetails.md) |  | [optional] 
**private_profile** | **bool** | Tell either this user profile is private or not (individual accounts only) | [optional] 
**locale** | **str** | The user language. Input values will be automatically normalized to a supported locale code. Unknown locales will default to &#x60;en&#x60;.  Current supported locales include: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ja-HIRA&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nb&#x60;, &#x60;nl&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;  | [optional] [default to 'en']
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
print(UserDetails.to_json())

# convert the object into a dict
user_details_dict = user_details_instance.to_dict()
# create an instance of UserDetails from a dict
user_details_from_dict = UserDetails.from_dict(user_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


