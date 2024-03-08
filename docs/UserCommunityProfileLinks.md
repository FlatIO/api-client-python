# UserCommunityProfileLinks

Social networks links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spotify_url** | **str** | Spotify Profile URL | [optional] 
**youtube_url** | **str** | YouTube channel URL | [optional] 
**soundcloud_url** | **str** | SoundCloud Profile URL | [optional] 
**tiktok_url** | **str** | TikTok profile URL. For updates, also accepts TikTok usernames | [optional] 
**instagram_url** | **str** | Instagram profile URL. For updates, also accepts Instagram usernames | [optional] 
**website_url** | **str** | Personnal website URL | [optional] 

## Example

```python
from flat_api.models.user_community_profile_links import UserCommunityProfileLinks

# TODO update the JSON string below
json = "{}"
# create an instance of UserCommunityProfileLinks from a JSON string
user_community_profile_links_instance = UserCommunityProfileLinks.from_json(json)
# print the JSON string representation of the object
print UserCommunityProfileLinks.to_json()

# convert the object into a dict
user_community_profile_links_dict = user_community_profile_links_instance.to_dict()
# create an instance of UserCommunityProfileLinks from a dict
user_community_profile_links_form_dict = user_community_profile_links.from_dict(user_community_profile_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


