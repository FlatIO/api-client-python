# AssignmentSubmission

Assignment Submission

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the submission | 
**state** | [**AssignmentSubmissionState**](AssignmentSubmissionState.md) |  | 
**classroom** | **str** | Unique identifier of the classroom where the assignment was posted  | 
**assignment** | **str** | Unique identifier of the assignment | 
**creator** | **str** | The User identifier of the student who created the submission | 
**attachments** | [**[MediaAttachment]**](MediaAttachment.md) |  | 
**creation_date** | **str** | The date when the submission was created | [optional] 
**submission_date** | **str** | The date when the student submitted their work | [optional] 
**return_date** | **str** | The date when the teacher returned the work | [optional] 
**return_creator** | **str** | The User unique identifier of the teacher who returned the submission  | [optional] 
**grade** | **float, none_type** | Optional grade. If unset, no grade was set. | [optional] 
**draft_grade** | **float, none_type** | Optional grade. If unset, no grade was set. This value is only visible by the teacher, and we will be set to &#x60;grade&#x60; once the teacher returns the submission | [optional] 
**max_points** | **float** | Optional max points for the grade. If set, a corresponding &#x60;draftGrade&#x60; or &#x60;grade&#x60; will be set. | [optional] 
**exercises_ids** | **[str], none_type** | The ids of exercises when they need to be in a specific order | [optional] 
**google_classroom** | [**GoogleClassroomSubmission**](GoogleClassroomSubmission.md) |  | [optional] 
**microsoft_graph** | [**MicrosoftGraphSubmission**](MicrosoftGraphSubmission.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


