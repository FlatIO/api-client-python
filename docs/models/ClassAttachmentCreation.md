# flat_api.model.class_attachment_creation.ClassAttachmentCreation

Attachment creation for an assignment or stream post. This attachment must contain a `score` or an `url`, all the details of this one will be resolved and returned as `ClassAttachment` once the assignment or stream post is created. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Attachment creation for an assignment or stream post. This attachment must contain a &#x60;score&#x60; or an &#x60;url&#x60;, all the details of this one will be resolved and returned as &#x60;ClassAttachment&#x60; once the assignment or stream post is created.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the attachment posted: * &#x60;rich&#x60;, &#x60;photo&#x60;, &#x60;video&#x60; are attachment types that are automatically resolved from a &#x60;link&#x60; attachment. * A &#x60;flat&#x60; attachment is a score document where the unique identifier will be specified in the &#x60;score&#x60; property. Its sharing mode will be provided in the &#x60;sharingMode&#x60; property.  | [optional] must be one of ["rich", "photo", "video", "link", "flat", "googleDrive", "worksheet", "performance", ] 
**score** | str,  | str,  | A unique Flat score identifier. The user creating the assignment must at least have read access to the document. If the user has admin rights, new group permissions will be automatically added for the teachers and students of the class.  | [optional] 
**worksheet** | str,  | str,  | An unique worksheet identifier | [optional] 
**sharingMode** | [**MediaScoreSharingMode**](MediaScoreSharingMode.md) | [**MediaScoreSharingMode**](MediaScoreSharingMode.md) |  | [optional] 
**lockScoreTemplate** | bool,  | BoolClass,  | To be used with a score attached in &#x60;sharingMode&#x60; &#x60;copy&#x60; (score used as template). If true, students won&#x27;t be able to change the original notes of the template. | [optional] 
**url** | str,  | str,  | The URL of the attachment. | [optional] 
**googleDriveFileId** | str,  | str,  | The ID of the Google Drive File | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

