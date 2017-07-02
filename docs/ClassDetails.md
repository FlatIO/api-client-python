# ClassDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the class | [optional] 
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
**google_classroom** | [**ClassDetailsGoogleClassroom**](ClassDetailsGoogleClassroom.md) |  | [optional] 
**google_drive** | [**ClassDetailsGoogleDrive**](ClassDetailsGoogleDrive.md) |  | [optional] 
**lti** | [**ClassDetailsLti**](ClassDetailsLti.md) |  | [optional] 
**canvas** | [**ClassDetailsCanvas**](ClassDetailsCanvas.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


