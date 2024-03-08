# ScoreCreationBuilderData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score_data** | [**ScoreCreationBuilderDataScoreData**](ScoreCreationBuilderDataScoreData.md) |  | 
**layout_data** | [**ScoreCreationBuilderDataLayoutData**](ScoreCreationBuilderDataLayoutData.md) |  | [optional] 

## Example

```python
from flat_api.models.score_creation_builder_data import ScoreCreationBuilderData

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreCreationBuilderData from a JSON string
score_creation_builder_data_instance = ScoreCreationBuilderData.from_json(json)
# print the JSON string representation of the object
print ScoreCreationBuilderData.to_json()

# convert the object into a dict
score_creation_builder_data_dict = score_creation_builder_data_instance.to_dict()
# create an instance of ScoreCreationBuilderData from a dict
score_creation_builder_data_form_dict = score_creation_builder_data.from_dict(score_creation_builder_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


