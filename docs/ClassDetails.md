# ClassDetails

A classroom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the class | 
**state** | [**ClassState**](ClassState.md) |  | [optional] 
**name** | **str** | The name of the class | [optional] 
**section** | **str** | The section of the class | [optional] 
**description** | **str** | An optionnal description for this class | [optional] 
**organization** | **str** | The unique identifier of the Organization owning this class | [optional] 
**owner** | **str** | The unique identifier of the User owning this class | [optional] 
**creation_date** | **datetime** | The date when the class was create | [optional] 
**enrollment_code** | **str** | [Teachers only] The enrollment code that can be used by the students to join the class  | [optional] 
**theme** | **str** | The theme identifier using in Flat User Interface | [optional] 
**assignments_count** | **float** | The number of assignments created in the class | [optional] 
**students_group** | [**GroupDetails**](GroupDetails.md) |  | [optional] 
**teachers_group** | [**GroupDetails**](GroupDetails.md) |  | [optional] 
**issues** | [**ClassDetailsIssues**](ClassDetailsIssues.md) |  | [optional] 
**google_classroom** | [**ClassDetailsGoogleClassroom**](ClassDetailsGoogleClassroom.md) |  | [optional] 
**google_drive** | [**ClassDetailsGoogleDrive**](ClassDetailsGoogleDrive.md) |  | [optional] 
**microsoft_graph** | [**ClassDetailsMicrosoftGraph**](ClassDetailsMicrosoftGraph.md) |  | [optional] 
**lti** | [**ClassDetailsLti**](ClassDetailsLti.md) |  | [optional] 
**canvas** | [**ClassDetailsCanvas**](ClassDetailsCanvas.md) |  | [optional] 
**mfc** | [**ClassDetailsMfc**](ClassDetailsMfc.md) |  | [optional] 
**clever** | [**ClassDetailsClever**](ClassDetailsClever.md) |  | [optional] 
**level** | [**ClassGradeLevel**](ClassGradeLevel.md) |  | [optional] 
**skills_focused** | **List[str]** | Specific skills that will be focused in classroom | [optional] 
**size** | **float** | Number of students in the classroom | [optional] 

## Example

```python
from flat_api.models.class_details import ClassDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClassDetails from a JSON string
class_details_instance = ClassDetails.from_json(json)
# print the JSON string representation of the object
print ClassDetails.to_json()

# convert the object into a dict
class_details_dict = class_details_instance.to_dict()
# create an instance of ClassDetails from a dict
class_details_form_dict = class_details.from_dict(class_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


