# Assignment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of the assignment | [optional] 
**title** | **str** | Title of the assignment | [optional] 
**classroom** | **str** | The unique identifier of the class where this assignment was posted | [optional] 
**description** | **str** | Description and content of the assignment | [optional] 
**attachments** | [**list[MediaAttachment]**](MediaAttachment.md) |  | [optional] 
**submissions** | [**list[AssignmentSubmission]**](AssignmentSubmission.md) |  | [optional] 
**creator** | **str** | The User unique identifier of the creator of this assignment  | [optional] 
**creation_date** | **datetime** | The creation date of this assignment | [optional] 
**scheduled_date** | **datetime** | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  | [optional] 
**due_date** | **datetime** | The due date of this assignment, late submissions will be marked as paste due.  | [optional] 
**google_classroom** | [**GoogleClassroomCoursework**](GoogleClassroomCoursework.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


