# AssignmentUpdate

Assignment Resource Editing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AssignmentType**](AssignmentType.md) |  | [optional] 
**title** | **str** | Title of the assignment | [optional] 
**description** | **str** | Description and content of the assignment | [optional] 
**attachments** | [**[ClassAttachmentCreation]**](ClassAttachmentCreation.md) |  | [optional] 
**nb_playback_authorized** | **float, none_type** | The number of playback authorized on the scores of the assignment. | [optional] 
**toolset** | **str, none_type** | The id of the toolset to apply to this assignment. The toolset will be copied to the assignment as a dedicated object to prevent unexpected changes when making modifications to the template toolset. This property can be set to null to delete the linked toolset and switch back to all the tools available for this assignment.  | [optional] 
**cover_file** | **str, none_type** | The id of the cover to display | [optional] 
**cover** | **str, none_type** | The URL of the cover to display | [optional] 
**max_points** | **float, none_type** | If set, the grading will be enabled for the assignement with this value as the maximum of points  | [optional] 
**release_grades** | **str** | For worksheets, how grading will work for the assignment: - If set to &#x60;auto&#x60;, the grades will be automatically released when the student submits the submissions - If set to &#x60;manual&#x60;, the grades will only be set as &#x60;draftGrade&#x60; and will be released when the teacher returns the submissions  | [optional] 
**shuffle_exercises** | **bool** | Mixing worksheets exercises for each student | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

