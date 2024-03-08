# AssignmentCopyResponse


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
**resource** | **str** | If this assignment is stored as a resource in the Flat for Education Resource Library, the unique identifier of the resource. | [optional] 

## Example

```python
from flat_api.models.assignment_copy_response import AssignmentCopyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentCopyResponse from a JSON string
assignment_copy_response_instance = AssignmentCopyResponse.from_json(json)
# print the JSON string representation of the object
print AssignmentCopyResponse.to_json()

# convert the object into a dict
assignment_copy_response_dict = assignment_copy_response_instance.to_dict()
# create an instance of AssignmentCopyResponse from a dict
assignment_copy_response_form_dict = assignment_copy_response.from_dict(assignment_copy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


