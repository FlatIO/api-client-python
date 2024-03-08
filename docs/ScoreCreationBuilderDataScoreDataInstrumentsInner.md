# ScoreCreationBuilderDataScoreDataInstrumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | The  of the instrument group (e.g. &#x60;keyboards&#x60;, &#x60;brass&#x60;) | 
**instrument** | **str** | The identifier of the instrument (e.g. &#x60;piano&#x60;, &#x60;trumpet&#x60;) | 
**long_name** | **str** | The full name of the instrument | [optional] 
**short_name** | **str** | The abbreviation of the name of the instrument | [optional] 
**has_quarter_tone** | **bool** | True if the part can use quarter tone (prevent the part to have a TAB/chord grid) | [optional] 

## Example

```python
from flat_api.models.score_creation_builder_data_score_data_instruments_inner import ScoreCreationBuilderDataScoreDataInstrumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreCreationBuilderDataScoreDataInstrumentsInner from a JSON string
score_creation_builder_data_score_data_instruments_inner_instance = ScoreCreationBuilderDataScoreDataInstrumentsInner.from_json(json)
# print the JSON string representation of the object
print ScoreCreationBuilderDataScoreDataInstrumentsInner.to_json()

# convert the object into a dict
score_creation_builder_data_score_data_instruments_inner_dict = score_creation_builder_data_score_data_instruments_inner_instance.to_dict()
# create an instance of ScoreCreationBuilderDataScoreDataInstrumentsInner from a dict
score_creation_builder_data_score_data_instruments_inner_form_dict = score_creation_builder_data_score_data_instruments_inner.from_dict(score_creation_builder_data_score_data_instruments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


