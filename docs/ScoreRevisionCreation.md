# ScoreRevisionCreation

A new created revision
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The data of the score file. It must be a MusicXML 3 file (&#x60;vnd.recordare.musicxml&#x60; or &#x60;vnd.recordare.musicxml+xml&#x60;), a MIDI file (&#x60;audio/midi&#x60;) or a Flat.json (aka Adagio.json) file. Binary payloads (&#x60;vnd.recordare.musicxml&#x60; and &#x60;audio/midi&#x60;) can be encoded in Base64, in this case the &#x60;dataEncoding&#x60; property must match the encoding used for the API request.  | 
**data_encoding** | **str** | The optional encoding of the score data. This property must match the encoding used for the &#x60;data&#x60; property. | [optional] 
**autosave** | **bool** | Must be set to &#x60;true&#x60; if the revision was created automatically.  | [optional] 
**description** | **str** | A description associated to the revision | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


