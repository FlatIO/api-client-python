# ScoreCreationBuilderDataScoreData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_tab_staff** | **bool** | true if the TAB staff is displayed with fretted instruments | [optional] 
**use_chord_grid** | **bool** | true if the chord grid must be displayed with fretted instruments | [optional] 
**fifths** | **float** | The key signature of the score (expressed between -7 and 7). Major C is used when the value is not provided. | [optional] 
**nb_beats** | **float** | The number of beats in the measure | [optional] 
**beat_type** | **float** | The duration of a beat in the measure | [optional] 
**instruments** | [**List[ScoreCreationBuilderDataScoreDataInstrumentsInner]**](ScoreCreationBuilderDataScoreDataInstrumentsInner.md) | The list of instruments to add to the score. See https://prod.flat-cdn.com/fixtures/instruments_en.json for the possible values for &#x60;group&#x60; and &#x60;instrument&#x60;.  | 

## Example

```python
from flat_api.models.score_creation_builder_data_score_data import ScoreCreationBuilderDataScoreData

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreCreationBuilderDataScoreData from a JSON string
score_creation_builder_data_score_data_instance = ScoreCreationBuilderDataScoreData.from_json(json)
# print the JSON string representation of the object
print ScoreCreationBuilderDataScoreData.to_json()

# convert the object into a dict
score_creation_builder_data_score_data_dict = score_creation_builder_data_score_data_instance.to_dict()
# create an instance of ScoreCreationBuilderDataScoreData from a dict
score_creation_builder_data_score_data_form_dict = score_creation_builder_data_score_data.from_dict(score_creation_builder_data_score_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


