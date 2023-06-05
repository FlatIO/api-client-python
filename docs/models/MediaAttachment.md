# flat_api.model.media_attachment.MediaAttachment

Media attachment. The API will automatically resolve the details, oEmbed, and media available if possible and return them in this object 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Media attachment. The API will automatically resolve the details, oEmbed, and media available if possible and return them in this object  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the assignment resolved: * &#x60;rich&#x60;, &#x60;photo&#x60;, &#x60;video&#x60; are automatically resolved as &#x60;link&#x60; * A &#x60;flat&#x60; attachment is a score document where the unique identifier will be specified in the &#x60;score&#x60; property. Its sharing mode will be provided in the &#x60;sharingMode&#x60; property.  | must be one of ["rich", "photo", "video", "link", "flat", "googleDrive", "worksheet", "performance", ] 
**score** | str,  | str,  | An unique Flat score identifier | [optional] 
**revision** | str,  | str,  | An unique revision identifier of a score | [optional] 
**worksheet** | str,  | str,  | An unique worksheet identifier | [optional] 
**dedicated** | bool,  | BoolClass,  | True if the resource is dedicated for the assignment (for scores and worksheets), meaning on the user-side this one is stored in the assignment | [optional] 
**track** | str,  | str,  | A unique track identifier | [optional] 
**sharingMode** | [**MediaScoreSharingMode**](MediaScoreSharingMode.md) | [**MediaScoreSharingMode**](MediaScoreSharingMode.md) |  | [optional] 
**lockScoreTemplate** | bool,  | BoolClass,  | To be used with a score attached in &#x60;sharingMode&#x60; &#x60;copy&#x60; (score used as template). If true, students won&#x27;t be able to change the original notes of the template. | [optional] 
**title** | str,  | str,  | The resolved title of the attachment | [optional] 
**description** | str,  | str,  | The resolved description of the attachment | [optional] 
**html** | str,  | str,  | If the attachment type is &#x60;rich&#x60; or &#x60;video&#x60;, the HTML code of the media to display  | [optional] 
**htmlWidth** | str,  | str,  | If the &#x60;html&#x60; is available, the width of the widget | [optional] 
**htmlHeight** | str,  | str,  | If the &#x60;html&#x60; is available, the height of the widget | [optional] 
**url** | str,  | str,  | The url of the attachment | [optional] 
**thumbnailUrl** | str,  | str,  | If the attachment type is &#x60;rich&#x60;, &#x60;video&#x60;, &#x60;photo&#x60; or &#x60;link&#x60;, a displayable thumbnail for this attachment  | [optional] 
**thumbnailWidth** | decimal.Decimal, int,  | decimal.Decimal,  | If the &#x60;thumbnailUrl&#x60; is available, the width of the thumbnail  | [optional] 
**thumbnailHeight** | decimal.Decimal, int,  | decimal.Decimal,  | If the &#x60;thumbnailUrl&#x60; is available, the width of the thumbnail  | [optional] 
**authorName** | str,  | str,  | The resolved author name of the attachment | [optional] 
**authorUrl** | str,  | str,  | The resolved author url of the attachment | [optional] 
**iconUrl** | str,  | str,  | The URL of the icon | [optional] 
**mimeType** | str,  | str,  | The mine type of the file | [optional] 
**googleDriveFileId** | str,  | str,  | The ID of the Google Drive File | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

