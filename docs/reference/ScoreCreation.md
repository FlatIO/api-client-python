# ScoreCreation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the new score. If the title is too long, the API may trim this one.  If this title is not specified, the API will try to (in this order):   - Use the title contained in the file (e.g. [&#x60;movement-title&#x60;](https://usermanuals.musicxml.com/MusicXML/Content/EL-MusicXML-movement-title.htm) or [&#x60;credit-words&#x60;](https://usermanuals.musicxml.com/MusicXML/Content/EL-MusicXML-credit-words.htm) for [MusicXML](http://www.musicxml.com/) files).   - Use the name of the file for files from a specified &#x60;source&#x60; (e.g. Google Drive) or the one in the &#x60;filename&#x60; property   - Set a default title (e.g. \&quot;New Music Score\&quot;)  | [optional] 
**privacy** | [**ScorePrivacy**](ScorePrivacy.md) |  | [optional] [default to ScorePrivacy.PRIVATE]
**collection** | **str** | Unique identifier of a collection where the score will be created. If no collection identifier is provided, the score will not be added to any collection and will only be visible in the &#x60;allScores&#x60; virtual collection.  | [optional] 
**google_drive_folder** | **str** | If the user uses Google Drive and this properties is specified, the file will be created in this directory. The currently user creating the file must be granted to write in this directory.  | [optional] 
**builder_data** | [**ScoreCreationBuilderDataAllOfBuilderData**](ScoreCreationBuilderDataAllOfBuilderData.md) |  | 
**filename** | **str** | If this is an imported file, its filename | [optional] 
**data** | **str** | The data of the score file. See the &#x60;POST /scores&#x60; endpoint description for the full list of supported formats. Binary payloads (e.g. compressed MusicXML, MIDI, Guitar Pro) can be encoded in Base64, in this case the &#x60;dataEncoding&#x60; property must match the encoding used for the API request.  | 
**data_encoding** | **str** | The optional encoding of the score data. This property must match the encoding used for the &#x60;data&#x60; property. | [optional] 
**supports_tasks** | **bool** | Set this to &#x60;true&#x60; if the client supports asynchronous task flows. When importing a score that requires OMR processing (a PDF or a page image), the API will return a 202 Accepted response along with a task reference. The client can then check the task status using the endpoint &#x60;GET /v2/tasks/{task}&#x60;.  | [optional] 
**source** | [**ScoreSource**](ScoreSource.md) |  | 

## Example

```python
from flat_api.models.score_creation import ScoreCreation

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreCreation from a JSON string
score_creation_instance = ScoreCreation.from_json(json)
# print the JSON string representation of the object
print(ScoreCreation.to_json())

# convert the object into a dict
score_creation_dict = score_creation_instance.to_dict()
# create an instance of ScoreCreation from a dict
score_creation_from_dict = ScoreCreation.from_dict(score_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


