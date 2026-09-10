# ScoreCreationBuilderDataAllOfBuilderDataScoreData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_tab_staff** | **bool** | true if the TAB staff is displayed with fretted instruments | [optional] 
**use_chord_grid** | **bool** | true if the chord grid must be displayed with fretted instruments | [optional] 
**fifths** | **float** | The key signature of the score (expressed between -7 and 7). Major C is used when the value is not provided. | [optional] 
**nb_beats** | **float** | The number of beats in the measure | [optional] 
**beat_type** | **float** | The duration of a beat in the measure | [optional] 
**instruments** | [**List[ScoreCreationBuilderDataAllOfBuilderDataScoreDataInstruments]**](ScoreCreationBuilderDataAllOfBuilderDataScoreDataInstruments.md) | The list of instruments to add to the score. See the [Instrument IDs reference](https://flat.io/developers/docs/api/instruments) for the possible values for &#x60;group&#x60; and &#x60;instrument&#x60; (also available as the [&#x60;@flat/instruments&#x60;](https://www.npmjs.com/package/@flat/instruments) package).  | 

## Example

```python
from flat_api.models.score_creation_builder_data_all_of_builder_data_score_data import ScoreCreationBuilderDataAllOfBuilderDataScoreData

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreCreationBuilderDataAllOfBuilderDataScoreData from a JSON string
score_creation_builder_data_all_of_builder_data_score_data_instance = ScoreCreationBuilderDataAllOfBuilderDataScoreData.from_json(json)
# print the JSON string representation of the object
print(ScoreCreationBuilderDataAllOfBuilderDataScoreData.to_json())

# convert the object into a dict
score_creation_builder_data_all_of_builder_data_score_data_dict = score_creation_builder_data_all_of_builder_data_score_data_instance.to_dict()
# create an instance of ScoreCreationBuilderDataAllOfBuilderDataScoreData from a dict
score_creation_builder_data_all_of_builder_data_score_data_from_dict = ScoreCreationBuilderDataAllOfBuilderDataScoreData.from_dict(score_creation_builder_data_all_of_builder_data_score_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


