# AssignmentCreation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AssignmentType**](AssignmentType.md) |  | [optional] 
**state** | **str** | State of the assignment | [optional] 
**title** | **str** | Title of the assignment | [optional] 
**description** | **str** | Description and content of the assignment | [optional] 
**attachments** | [**list[ClassAttachmentCreation]**](ClassAttachmentCreation.md) |  | [optional] 
**due_date** | **datetime** | The due date of this assignment, late submissions will be marked as paste due. If not set, the assignment won&#39;t have a due date.  | [optional] 
**scheduled_date** | **datetime** | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  | [optional] 
**nb_playback_authorized** | **float** | The number of playback authorized on the scores of the assignment. | [optional] 
**toolset** | **str** | The id of the associated toolset | [optional] 
**cover_file** | **str** | The id of the cover to display | [optional] 
**cover** | **str** | The URL of the cover to display | [optional] 
**max_points** | **float** | If set, the grading will be enabled for the assignement with this value as the maximum of points  | [optional] 
**google_classroom** | [**AssignmentCreationGoogleClassroom**](AssignmentCreationGoogleClassroom.md) |  | [optional] 
**microsoft_graph** | [**AssignmentCreationMicrosoftGraph**](AssignmentCreationMicrosoftGraph.md) |  | [optional] 
**assignee_mode** | **str** | Possible modes of assigning assignments | [optional] 
**assigned_students** | **list[str]** | Identifiers for the students that have access to the assignment | [optional] 
**shuffle_exercises** | **bool** | Mixing exercises for each students | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


