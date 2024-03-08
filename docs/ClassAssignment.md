# ClassAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the assignment | 
**type** | [**AssignmentType**](AssignmentType.md) |  | 
**capabilities** | [**AssignmentCopyResponseCapabilities**](AssignmentCopyResponseCapabilities.md) |  | 
**title** | **str** | Title of the assignment | 
**description** | **str** | Description and content of the assignment | [optional] 
**cover** | **str** | The URL of the cover to display | [optional] 
**cover_file** | **str** | The id of the cover to display | [optional] 
**attachments** | [**List[MediaAttachment]**](MediaAttachment.md) |  | 
**use_dedicated_attachments** | **bool** | For all assignments created after 02/2023, all the underlying resources must be dedicated and stored in the assignment. This boolean indicates that this assignment only supports dedicated attachments.  | [optional] 
**max_points** | **float** | If set, the grading will be enabled for the assignement  | [optional] 
**release_grades** | **str** | For worksheets, how grading will work for the assignment: - If set to &#x60;auto&#x60;, the grades will be automatically released when the student submits the submissions - If set to &#x60;manual&#x60;, the grades will only be set as &#x60;draftGrade&#x60; and will be released when the teacher returns the submissions  | [optional] 
**shuffle_exercises** | **bool** | Mixing worksheets exercises for each student | [optional] 
**toolset** | **str** | The id of the associated toolset | [optional] 
**nb_playback_authorized** | **float** | The number of playback authorized on the scores of the assignment. | [optional] 
**creator** | **str** | The User unique identifier of the creator of this assignment  | [optional] 
**state** | **str** | State of the assignment | [optional] 
**classroom** | **str** | The unique identifier of the class where this assignment was posted | [optional] 
**creation_date** | **datetime** | The creation date of this assignment | [optional] 
**scheduled_date** | **datetime** | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  | [optional] 
**due_date** | **datetime** | The due date of this assignment, late submissions will be marked as paste due.  | [optional] 
**assignee_mode** | **str** | Possible modes of assigning assignments | [optional] 
**assigned_students** | **List[str]** | Identifiers for the students that have access to the assignment | [optional] 
**submissions** | [**List[AssignmentSubmission]**](AssignmentSubmission.md) |  | [optional] 
**google_classroom** | [**GoogleClassroomCoursework**](GoogleClassroomCoursework.md) |  | [optional] 
**microsoft_graph** | [**MicrosoftGraphAssignment**](MicrosoftGraphAssignment.md) |  | [optional] 
**mfc** | [**ClassAssignmentMfc**](ClassAssignmentMfc.md) |  | [optional] 
**canvas** | [**ClassAssignmentCanvas**](ClassAssignmentCanvas.md) |  | [optional] 
**lti** | [**ClassAssignmentLti**](ClassAssignmentLti.md) |  | [optional] 
**issue** | **str** | Detected issue for this assignment | [optional] 

## Example

```python
from flat_api.models.class_assignment import ClassAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAssignment from a JSON string
class_assignment_instance = ClassAssignment.from_json(json)
# print the JSON string representation of the object
print ClassAssignment.to_json()

# convert the object into a dict
class_assignment_dict = class_assignment_instance.to_dict()
# create an instance of ClassAssignment from a dict
class_assignment_form_dict = class_assignment.from_dict(class_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


