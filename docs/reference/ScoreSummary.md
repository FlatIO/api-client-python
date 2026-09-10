# ScoreSummary

A summary of the score details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the score | 
**sharing_key** | **str** | The private sharing key of the score (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) | [optional] 
**title** | **str** | The title of the score | 
**privacy** | [**ScorePrivacy**](ScorePrivacy.md) |  | [default to ScorePrivacy.PRIVATE]
**user** | [**UserPublic**](UserPublic.md) |  | 
**html_url** | **str** | The url where the score can be viewed in a web browser | 

## Example

```python
from flat_api.models.score_summary import ScoreSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreSummary from a JSON string
score_summary_instance = ScoreSummary.from_json(json)
# print the JSON string representation of the object
print(ScoreSummary.to_json())

# convert the object into a dict
score_summary_dict = score_summary_instance.to_dict()
# create an instance of ScoreSummary from a dict
score_summary_from_dict = ScoreSummary.from_dict(score_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


