# MediaAttachment

Media attachment. The API will automatically resolve the details, oEmbed, and media available if possible and return them in this object 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the assignment resolved: * &#x60;rich&#x60;, &#x60;photo&#x60;, &#x60;video&#x60; are automatically resolved as &#x60;link&#x60; * A &#x60;flat&#x60; attachment is a score document where the unique identifier will be specified in the &#x60;score&#x60; property. Its sharing mode will be provided in the &#x60;sharingMode&#x60; property.  | 
**score** | **str** | An unique Flat score identifier | [optional] 
**revision** | **str** | An unique revision identifier of a score | [optional] 
**worksheet** | **str** | An unique worksheet identifier | [optional] 
**dedicated** | **bool** | True if the resource is dedicated for the assignment (for scores and worksheets), meaning on the user-side this one is stored in the assignment | [optional] 
**track** | **str** | A unique track identifier | [optional] 
**sharing_mode** | [**MediaScoreSharingMode**](MediaScoreSharingMode.md) |  | [optional] 
**lock_score_template** | **bool** | To be used with a score attached in &#x60;sharingMode&#x60; &#x60;copy&#x60; (score used as template). If true, students won&#39;t be able to change the original notes of the template. | [optional] 
**title** | **str** | The resolved title of the attachment | [optional] 
**description** | **str** | The resolved description of the attachment | [optional] 
**html** | **str** | If the attachment type is &#x60;rich&#x60; or &#x60;video&#x60;, the HTML code of the media to display  | [optional] 
**html_width** | **str** | If the &#x60;html&#x60; is available, the width of the widget | [optional] 
**html_height** | **str** | If the &#x60;html&#x60; is available, the height of the widget | [optional] 
**url** | **str** | The url of the attachment | [optional] 
**thumbnail_url** | **str** | If the attachment type is &#x60;rich&#x60;, &#x60;video&#x60;, &#x60;photo&#x60; or &#x60;link&#x60;, a displayable thumbnail for this attachment  | [optional] 
**thumbnail_width** | **int** | If the &#x60;thumbnailUrl&#x60; is available, the width of the thumbnail  | [optional] 
**thumbnail_height** | **int** | If the &#x60;thumbnailUrl&#x60; is available, the width of the thumbnail  | [optional] 
**author_name** | **str** | The resolved author name of the attachment | [optional] 
**author_url** | **str** | The resolved author url of the attachment | [optional] 
**icon_url** | **str** | The URL of the icon | [optional] 
**mime_type** | **str** | The mine type of the file | [optional] 
**google_drive_file_id** | **str** | The ID of the Google Drive File | [optional] 

## Example

```python
from flat_api.models.media_attachment import MediaAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAttachment from a JSON string
media_attachment_instance = MediaAttachment.from_json(json)
# print the JSON string representation of the object
print MediaAttachment.to_json()

# convert the object into a dict
media_attachment_dict = media_attachment_instance.to_dict()
# create an instance of MediaAttachment from a dict
media_attachment_form_dict = media_attachment.from_dict(media_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


