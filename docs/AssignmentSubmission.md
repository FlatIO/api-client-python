# AssignmentSubmission

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the submission | [optional] 
**state** | [**AssignmentSubmissionState**](AssignmentSubmissionState.md) |  | [optional] 
**classroom** | **str** | Unique identifier of the classroom where the assignment was posted  | [optional] 
**assignment** | **str** | Unique identifier of the assignment | [optional] 
**creator** | **str** | The User identifier of the student who created the submission | [optional] 
**creation_date** | **str** | The date when the submission was created | [optional] 
**attachments** | [**list[MediaAttachment]**](MediaAttachment.md) |  | [optional] 
**submission_date** | **str** | The date when the student submitted his work | [optional] 
**return_date** | **str** | The date when the teacher returned the work | [optional] 
**return_creator** | **str** | The User unique identifier of the teacher who returned the submission  | [optional] 
**grade** | **float** | Optional grade. If unset, no grade was set. | [optional] 
**draft_grade** | **float** | Optional grade. If unset, no grade was set. This value is only visible by the teacher, and we will be set to &#x60;grade&#x60; once the teacher returns the submission | [optional] 
**max_points** | **float** | Optional max points for the grade. If set, a corresponding &#x60;draftGrade&#x60; or &#x60;grade&#x60; will be set. | [optional] 
**exercises_ids** | **list[str]** | The ids of exercises when they need to be in a specific order | [optional] 
**google_classroom** | [**GoogleClassroomSubmission**](GoogleClassroomSubmission.md) |  | [optional] 
**microsoft_graph** | [**MicrosoftGraphSubmission**](MicrosoftGraphSubmission.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


