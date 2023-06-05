# flat_api.model.class_details.ClassDetails

A classroom

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A classroom | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier of the class | [optional] 
**state** | [**ClassState**](ClassState.md) | [**ClassState**](ClassState.md) |  | [optional] 
**name** | str,  | str,  | The name of the class | [optional] 
**section** | str,  | str,  | The section of the class | [optional] 
**description** | str,  | str,  | An optionnal description for this class | [optional] 
**organization** | str,  | str,  | The unique identifier of the Organization owning this class | [optional] 
**owner** | str,  | str,  | The unique identifier of the User owning this class | [optional] 
**creationDate** | str, datetime,  | str,  | The date when the class was create | [optional] value must conform to RFC-3339 date-time
**enrollmentCode** | str,  | str,  | [Teachers only] The enrollment code that can be used by the students to join the class  | [optional] 
**theme** | str,  | str,  | The theme identifier using in Flat User Interface | [optional] 
**assignmentsCount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of assignments created in the class | [optional] 
**studentsGroup** | [**GroupDetails**](GroupDetails.md) | [**GroupDetails**](GroupDetails.md) |  | [optional] 
**teachersGroup** | [**GroupDetails**](GroupDetails.md) | [**GroupDetails**](GroupDetails.md) |  | [optional] 
**[issues](#issues)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Detected issues for this class | [optional] 
**[googleClassroom](#googleClassroom)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Google Classroom course-related information | [optional] 
**[googleDrive](#googleDrive)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Google Drive course-related information provided by Google Classroom | [optional] 
**[microsoftGraph](#microsoftGraph)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[lti](#lti)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Meta information provided by the LTI consumer | [optional] 
**[canvas](#canvas)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Meta information provided by Canvs LMS | [optional] 
**[mfc](#mfc)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Meta information provided by Canvs LMS | [optional] 
**[clever](#clever)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Clever.com section-related information | [optional] 
**level** | [**ClassGradeLevel**](ClassGradeLevel.md) | [**ClassGradeLevel**](ClassGradeLevel.md) |  | [optional] 
**skillsFocused** | [**EduSkillsFocused**](EduSkillsFocused.md) | [**EduSkillsFocused**](EduSkillsFocused.md) |  | [optional] 
**size** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Number of students in the classroom | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# issues

Detected issues for this class

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Detected issues for this class | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[sync](#sync)** | list, tuple,  | tuple,  | Synchronization issues for the class | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sync

Synchronization issues for the class

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Synchronization issues for the class | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | A sync issue | 

# items

A sync issue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A sync issue | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The account user identifier | [optional] 
**email** | str,  | str,  | The email address of the user concerned by this sync issue | [optional] 
**reason** | str,  | str,  | The reason why the account cannot be synced | [optional] must be one of ["otherOrgnanization", "personalSubscription", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# googleClassroom

Google Classroom course-related information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Google Classroom course-related information | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The course identifier on Google Classroom | [optional] 
**alternateLink** | str,  | str,  | Absolute link to this course in the Classroom web UI | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# googleDrive

Google Drive course-related information provided by Google Classroom

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Google Drive course-related information provided by Google Classroom | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**teacherFolderId** | str,  | str,  | [Teachers only] The Drive directory identifier of the teachers&#x27; folder  | [optional] 
**teacherFolderAlternateLink** | str,  | str,  | [Teachers only] The Drive URL of the teachers&#x27; folder  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# microsoftGraph

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The course identifier on Microsoft Graph | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lti

Meta information provided by the LTI consumer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Meta information provided by the LTI consumer | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contextId** | str,  | str,  | Unique context identifier provided | [optional] 
**contextTitle** | str,  | str,  | Context title | [optional] 
**contextLabel** | str,  | str,  | Context label | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# canvas

Meta information provided by Canvs LMS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Meta information provided by Canvs LMS | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of the course on Canvas | [optional] 
**domain** | str,  | str,  | Canvas instance domain (e.g. \&quot;canvas.instructure.com\&quot;) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mfc

Meta information provided by Canvs LMS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Meta information provided by Canvs LMS | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of the course on MusicFirst Classroom | [optional] 
**alternateLink** | str,  | str,  | Link to MusicFirst Classroom class | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# clever

Clever.com section-related information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Clever.com section-related information | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Clever section unique identifier | [optional] 
**creationDate** | str, datetime,  | str,  | The creation date of the section on clever | [optional] value must conform to RFC-3339 date-time
**modificationDate** | str, datetime,  | str,  | The last modification date of the section on clever | [optional] value must conform to RFC-3339 date-time
**subject** | str,  | str,  | Normalized subject of the course | [optional] must be one of ["english/language arts", "math", "science", "social studies", "language", "homeroom/advisory", "interventions/online learning", "technology and engineering", "PE and health", "arts and music", "other", ] 
**termName** | str,  | str,  | Name of the term when this course happens | [optional] 
**termStartDate** | str, datetime,  | str,  | Beginning date of the term | [optional] value must conform to RFC-3339 date-time
**termEndDate** | str, datetime,  | str,  | End date of the term | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

