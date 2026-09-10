# ScoreLikesCounts

A computed version of the weekly, monthly, yearly and total number of likes for a score 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | The total number of likes of the score | [optional] 
**weekly** | **float** | The number of new likes during the last week | [optional] 
**monthly** | **float** | The number of new likes during the last month | [optional] 
**yearly** | **float** | The number of new likes during the last year | [optional] 

## Example

```python
from flat_api.models.score_likes_counts import ScoreLikesCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreLikesCounts from a JSON string
score_likes_counts_instance = ScoreLikesCounts.from_json(json)
# print the JSON string representation of the object
print(ScoreLikesCounts.to_json())

# convert the object into a dict
score_likes_counts_dict = score_likes_counts_instance.to_dict()
# create an instance of ScoreLikesCounts from a dict
score_likes_counts_from_dict = ScoreLikesCounts.from_dict(score_likes_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


