# flat_api.model.class_creation.ClassCreation

Creation of a classroom

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Creation of a classroom | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the new class | 
**section** | str,  | str,  | The section of the new class | [optional] 
**level** | [**ClassGradeLevel**](ClassGradeLevel.md) | [**ClassGradeLevel**](ClassGradeLevel.md) |  | [optional] 
**skillsFocused** | [**EduSkillsFocused**](EduSkillsFocused.md) | [**EduSkillsFocused**](EduSkillsFocused.md) |  | [optional] 
**size** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Number of students in the classroom | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

