# ScoreCreation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the new score. If the title is too long, the API may trim this one.  If this title is not specified, the API will try to (in this order):   - Use the title contained in the file (e.g. [&#x60;movement-title&#x60;](https://usermanuals.musicxml.com/MusicXML/Content/EL-MusicXML-movement-title.htm) or [&#x60;credit-words&#x60;](https://usermanuals.musicxml.com/MusicXML/Content/EL-MusicXML-credit-words.htm) for [MusicXML](http://www.musicxml.com/) files).   - Use the name of the file for files from a specified &#x60;source&#x60; (e.g. Google Drive) or the one in the &#x60;filename&#x60; property   - Set a default title (e.g. \&quot;New Music Score\&quot;)  | [optional] 
**filename** | **str** | If this is an imported file, its filename | [optional] 
**privacy** | [**ScorePrivacy**](ScorePrivacy.md) |  | 
**data** | **str** | The data of the score file. It must be a MusicXML 3 file (&#x60;vnd.recordare.musicxml&#x60; or &#x60;vnd.recordare.musicxml+xml&#x60;), a MIDI file (&#x60;audio/midi&#x60;) or a Flat.json (aka Adagio.json) file.  Binary payloads (&#x60;vnd.recordare.musicxml&#x60; and &#x60;audio/midi&#x60;) can be encoded in Base64, in this case the &#x60;dataEncoding&#x60; property must match the encoding used for the API request.  | [optional] 
**data_encoding** | [**ScoreDataEncoding**](ScoreDataEncoding.md) |  | [optional] 
**source** | [**ScoreSource**](ScoreSource.md) |  | [optional] 
**collection** | **str** | Unique identifier of a collection where the score will be created. If no collection identifier is provided, the score will be stored in the &#x60;root&#x60; directory.  | [optional] 
**google_drive_folder** | **str** | If the user uses Google Drive and this properties is specified, the file will be created in this directory. The currently user creating the file must be granted to write in this directory.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


