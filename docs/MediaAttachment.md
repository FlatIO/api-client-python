# MediaAttachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the assignment resolved: * &#x60;rich&#x60;, &#x60;photo&#x60;, &#x60;video&#x60; are attachment types that are automatically resolved from a &#x60;link&#x60; attachment. * A &#x60;flat&#x60; attachment is a score document where the unique identifier will be specified in the &#x60;score&#x60; property. Its sharing mode will be provided in the &#x60;sharingMode&#x60; property.  | [optional] 
**score** | **str** | An unique Flat score identifier | [optional] 
**revision** | **str** | An unique revision identifier of a score | [optional] 
**correct** | **bool** | If the attachment is an exercise question, this state will describe if it is correct or not.For exercise assignments only. | [optional] 
**sharing_mode** | [**MediaScoreSharingMode**](MediaScoreSharingMode.md) |  | [optional] 
**title** | **str** | The resolved title of the attachment | [optional] 
**description** | **str** | The resolved description of the attachment | [optional] 
**html** | **str** | If the attachment type is &#x60;rich&#x60; or &#x60;video&#x60;, the HTML code of the media to display  | [optional] 
**html_width** | **str** | If the &#x60;html&#x60; is available, the width of the widget | [optional] 
**html_height** | **str** | If the &#x60;html&#x60; is available, the height of the widget | [optional] 
**url** | **str** | The url of the attachment | [optional] 
**thumbnail_url** | **str** | If the attachment type is &#x60;rich&#x60;, &#x60;video&#x60;, &#x60;photo&#x60; or &#x60;link&#x60;, a displayable thumbnail for this attachment  | [optional] 
**thumbnail_width** | **str** | If the &#x60;thumbnailUrl&#x60; is available, the width of the thumbnail  | [optional] 
**thumbnail_height** | **str** | If the &#x60;thumbnailUrl&#x60; is available, the width of the thumbnail  | [optional] 
**author_name** | **str** | The resolved author name of the attachment | [optional] 
**author_url** | **str** | The resolved author url of the attachment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


