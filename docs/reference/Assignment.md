# Assignment

Assignment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the assignment | 
**type** | [**AssignmentType**](AssignmentType.md) |  | 
**capabilities** | [**AssignmentCapabilities**](AssignmentCapabilities.md) |  | 
**title** | **str** | Title of the assignment | 
**description** | **str** | Student instructions and content of the assignment (plain text) | [optional] 
**description_html** | **str** | HTML version of student instructions with rich text formatting. Supports the following HTML tags: p, br, strong, b, em, i, u, a, ul, ol, li, h1, h2, h3, img. Images are served as absolute http(s) URLs.  | [optional] 
**teacher_instructions** | **str** | Teacher-only instructions for this assignment. These instructions are only visible to teachers and are not returned when students view the assignment. If &#x60;teacherInstructionsHtml&#x60; is provided, this field will contain the plain text version for compatibility.  | [optional] 
**teacher_instructions_html** | **str** | HTML version of teacher-only instructions with rich text formatting. Supports the following HTML tags: p, br, strong, b, em, i, u, a, ul, ol, li, h1, h2, h3, img. Images are served as absolute http(s) URLs.  | [optional] 
**cover** | **str** | The URL of the cover to display | [optional] 
**cover_file** | **str** | The id of the cover to display | [optional] 
**attachments** | [**List[MediaAttachment]**](MediaAttachment.md) | Reference material handed to the students with the assignment: scores, videos, links and Drive files. A score attached here is the one each student receives their own copy of.  | 
**use_dedicated_attachments** | **bool** | For all assignments created after 02/2023, all the underlying resources must be dedicated and stored in the assignment. This boolean indicates that this assignment only supports dedicated attachments.  | [optional] 
**max_points** | **float** | If set, the grading will be enabled for the assignement  | [optional] 
**release_grades** | **str** | For worksheets, how grading will work for the assignment: - If set to &#x60;auto&#x60;, the grades will be automatically released when the student submits the submissions - If set to &#x60;manual&#x60;, the grades will only be set as &#x60;draftGrade&#x60; and will be released when the teacher returns the submissions  | [optional] 
**shuffle_exercises** | **bool** | Mixing worksheets exercises for each student | [optional] 
**toolset** | **str** | The id of the associated toolset | [optional] 
**nb_playback_authorized** | **float** | The number of playback authorized on the scores of the assignment. | [optional] 
**restrict_play_note** | **bool** | Restrict the ability to get an audio feedback every time a student adds or selects a note. | [optional] 
**restrict_to_audio_tracks** | **bool** | Restrict the audio source to provided audio tracks on a score. Students won&#39;t be able to use the editor playback. | [optional] 
**submission_students_mode** | [**AssignmentSubmissionStudentsMode**](AssignmentSubmissionStudentsMode.md) |  | [optional] 
**recording_type** | **str** | For performance assignments: recording type that will be either &#39;audio&#39; or &#39;video&#39;.  * &#x60;audio&#x60;: Only audio will be required during the recording. * &#x60;video&#x60;: Camera will be required during the recording.  Only set when type is &#39;performance&#39;.  | [optional] 
**allow_metronome** | **bool** | For performance assignments: Enable students to use the metronome while they are recording, helping them stay in time. Only set when type is &#39;performance&#39;.  | [optional] 
**allow_backing_track** | **bool** | For performance assignments: Enable students to listen to the accompaniment without their instrument part while they are playing. Only set when type is &#39;performance&#39;.  | [optional] 
**allow_speed_change** | **bool** | For performance assignments: whether students can adjust the playback speed of the score during recording.  * &#x60;true&#x60;: Students can change the tempo/speed during practice and recording * &#x60;false&#x60;: Tempo is fixed to the original score tempo  Only set when type is &#39;performance&#39;.  | [optional] 
**free_record** | **bool** | For performance assignments: \&quot;Free Record\&quot; mode.  When &#x60;true&#x60;, no score is attached to the assignment. Students freely record a varied repertoire or an ensemble performance without being constrained by a single score&#39;s structure or duration, and all score-dependent options (playback, metronome, backtracking, speed control) are hidden.  Only set when type is &#39;performance&#39;.  | [optional] 

## Example

```python
from flat_api.models.assignment import Assignment

# TODO update the JSON string below
json = "{}"
# create an instance of Assignment from a JSON string
assignment_instance = Assignment.from_json(json)
# print the JSON string representation of the object
print(Assignment.to_json())

# convert the object into a dict
assignment_dict = assignment_instance.to_dict()
# create an instance of Assignment from a dict
assignment_from_dict = Assignment.from_dict(assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


