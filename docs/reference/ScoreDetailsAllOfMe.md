# ScoreDetailsAllOfMe

Information about the authenticated user and this score

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_liked** | **bool** | True if the current user likes this score | 
**is_in_library** | **bool** | True if the score is stored in one of the user&#39;s collections | 

## Example

```python
from flat_api.models.score_details_all_of_me import ScoreDetailsAllOfMe

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreDetailsAllOfMe from a JSON string
score_details_all_of_me_instance = ScoreDetailsAllOfMe.from_json(json)
# print the JSON string representation of the object
print(ScoreDetailsAllOfMe.to_json())

# convert the object into a dict
score_details_all_of_me_dict = score_details_all_of_me_instance.to_dict()
# create an instance of ScoreDetailsAllOfMe from a dict
score_details_all_of_me_from_dict = ScoreDetailsAllOfMe.from_dict(score_details_all_of_me_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


