# ClassAttachmentCreation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the attachment posted | [optional] 
**score** | **str** | A unique Flat score identifier. The user creating the assignment must at least have read access to the document. If the user has admin rights, new group permissions will be automatically added for the teachers and students of the class.  | [optional] 
**worksheet** | **str** | An unique worksheet identifier | [optional] 
**sharing_mode** | [**MediaScoreSharingMode**](MediaScoreSharingMode.md) |  | [optional] 
**lock_score_template** | **bool** | To be used with a score attached in &#x60;sharingMode&#x60; &#x60;copy&#x60; (score used as template). If true, students won&#39;t be able to change the original notes of the template. | [optional] 
**url** | **str** | The URL of the attachment. | [optional] 
**google_drive_file_id** | **str** | The ID of the Google Drive File | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


