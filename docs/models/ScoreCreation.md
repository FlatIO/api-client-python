# flat_api.model.score_creation.ScoreCreation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | The title of the new score. If the title is too long, the API may trim this one.  If this title is not specified, the API will try to (in this order):   - Use the title contained in the file (e.g. [&#x60;movement-title&#x60;](https://usermanuals.musicxml.com/MusicXML/Content/EL-MusicXML-movement-title.htm) or [&#x60;credit-words&#x60;](https://usermanuals.musicxml.com/MusicXML/Content/EL-MusicXML-credit-words.htm) for [MusicXML](http://www.musicxml.com/) files).   - Use the name of the file for files from a specified &#x60;source&#x60; (e.g. Google Drive) or the one in the &#x60;filename&#x60; property   - Set a default title (e.g. \&quot;New Music Score\&quot;)  | [optional] 
**privacy** | [**ScorePrivacy**](ScorePrivacy.md) | [**ScorePrivacy**](ScorePrivacy.md) |  | [optional] 
**collection** | str,  | str,  | Unique identifier of a collection where the score will be created. If no collection identifier is provided, the score will be stored in the &#x60;root&#x60; directory.  | [optional] 
**googleDriveFolder** | str,  | str,  | If the user uses Google Drive and this properties is specified, the file will be created in this directory. The currently user creating the file must be granted to write in this directory.  | [optional] 
**[builderData](#builderData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**filename** | str,  | str,  | If this is an imported file, its filename | [optional] 
**data** | str,  | str,  | The data of the score file. It must be a MusicXML 3 file (&#x60;vnd.recordare.musicxml&#x60; or &#x60;vnd.recordare.musicxml+xml&#x60;), a MIDI file (&#x60;audio/midi&#x60;) or a Flat.json (aka Adagio.json) file. Binary payloads (&#x60;vnd.recordare.musicxml&#x60; and &#x60;audio/midi&#x60;) can be encoded in Base64, in this case the &#x60;dataEncoding&#x60; property must match the encoding used for the API request.  | [optional] 
**dataEncoding** | str,  | str,  | The optional encoding of the score data. This property must match the encoding used for the &#x60;data&#x60; property. | [optional] must be one of ["base64", ] 
**source** | [**ScoreSource**](ScoreSource.md) | [**ScoreSource**](ScoreSource.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# builderData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[scoreData](#scoreData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**[layoutData](#layoutData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Control the appearance of the score. If missing, default values are used. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scoreData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[instruments](#instruments)** | list, tuple,  | tuple,  | The list of instruments to add to the score. See https://prod.flat-cdn.com/fixtures/instruments_en.json for the possible values for &#x60;group&#x60; and &#x60;instrument&#x60;.  | 
**useTabStaff** | bool,  | BoolClass,  | true if the TAB staff is displayed with fretted instruments | [optional] 
**useChordGrid** | bool,  | BoolClass,  | true if the chord grid must be displayed with fretted instruments | [optional] 
**fifths** | decimal.Decimal, int, float,  | decimal.Decimal,  | The key signature of the score (expressed between -7 and 7). Major C is used when the value is not provided. | [optional] 
**nbBeats** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of beats in the measure | [optional] 
**beatType** | decimal.Decimal, int, float,  | decimal.Decimal,  | The duration of a beat in the measure | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instruments

The list of instruments to add to the score. See https://prod.flat-cdn.com/fixtures/instruments_en.json for the possible values for `group` and `instrument`. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of instruments to add to the score. See https://prod.flat-cdn.com/fixtures/instruments_en.json for the possible values for &#x60;group&#x60; and &#x60;instrument&#x60;.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**instrument** | str,  | str,  | The identifier of the instrument (e.g. &#x60;piano&#x60;, &#x60;trumpet&#x60;) | 
**group** | str,  | str,  | The  of the instrument group (e.g. &#x60;keyboards&#x60;, &#x60;brass&#x60;) | 
**longName** | str,  | str,  | The full name of the instrument | [optional] 
**shortName** | str,  | str,  | The abbreviation of the name of the instrument | [optional] 
**hasQuarterTone** | bool,  | BoolClass,  | True if the part can use quarter tone (prevent the part to have a TAB/chord grid) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# layoutData

Control the appearance of the score. If missing, default values are used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Control the appearance of the score. If missing, default values are used. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**notesSpacingCoeff** | decimal.Decimal, int, float,  | decimal.Decimal,  | A float value &gt;&#x3D; 1 that controls the spacing between notes. | [optional] 
**lengthUnit** | str,  | str,  | The unit to use for layout customizations | [optional] must be one of ["cm", "inch", ] if omitted the server will use the default value of "cm"
**pageHeight** | decimal.Decimal, int, float,  | decimal.Decimal,  | The height of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**pageWidth** | decimal.Decimal, int, float,  | decimal.Decimal,  | The width of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**pageMarginTop** | decimal.Decimal, int, float,  | decimal.Decimal,  | The top margin of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**pageMarginBottom** | decimal.Decimal, int, float,  | decimal.Decimal,  | The bottom margin of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**pageMarginLeft** | decimal.Decimal, int, float,  | decimal.Decimal,  | The left margin of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**pageMarginRight** | decimal.Decimal, int, float,  | decimal.Decimal,  | The right margin of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

