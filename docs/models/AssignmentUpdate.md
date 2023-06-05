# flat_api.model.assignment_update.AssignmentUpdate

Assignment Resource Editing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Assignment Resource Editing | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | [**AssignmentType**](AssignmentType.md) | [**AssignmentType**](AssignmentType.md) |  | [optional] 
**title** | str,  | str,  | Title of the assignment | [optional] 
**description** | str,  | str,  | Description and content of the assignment | [optional] 
**[attachments](#attachments)** | list, tuple,  | tuple,  |  | [optional] 
**nbPlaybackAuthorized** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The number of playback authorized on the scores of the assignment. | [optional] 
**toolset** | None, str,  | NoneClass, str,  | The id of the toolset to apply to this assignment. The toolset will be copied to the assignment as a dedicated object to prevent unexpected changes when making modifications to the template toolset. This property can be set to null to delete the linked toolset and switch back to all the tools available for this assignment.  | [optional] 
**coverFile** | None, str,  | NoneClass, str,  | The id of the cover to display | [optional] 
**cover** | None, str,  | NoneClass, str,  | The URL of the cover to display | [optional] 
**maxPoints** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | If set, the grading will be enabled for the assignement with this value as the maximum of points  | [optional] 
**releaseGrades** | str,  | str,  | For worksheets, how grading will work for the assignment: - If set to &#x60;auto&#x60;, the grades will be automatically released when the student submits the submissions - If set to &#x60;manual&#x60;, the grades will only be set as &#x60;draftGrade&#x60; and will be released when the teacher returns the submissions  | [optional] must be one of ["auto", "manual", ] 
**shuffleExercises** | bool,  | BoolClass,  | Mixing worksheets exercises for each student | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClassAttachmentCreation**](ClassAttachmentCreation.md) | [**ClassAttachmentCreation**](ClassAttachmentCreation.md) | [**ClassAttachmentCreation**](ClassAttachmentCreation.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

