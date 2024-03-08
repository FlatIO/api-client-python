# ScoreCommentModeration

Information about the comment being moderated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | If true, this comment will be hidden from other users | [optional] 
**reason** | **str** | If the comment is hidden, the reason why this one has been moderated | [optional] 

## Example

```python
from flat_api.models.score_comment_moderation import ScoreCommentModeration

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreCommentModeration from a JSON string
score_comment_moderation_instance = ScoreCommentModeration.from_json(json)
# print the JSON string representation of the object
print ScoreCommentModeration.to_json()

# convert the object into a dict
score_comment_moderation_dict = score_comment_moderation_instance.to_dict()
# create an instance of ScoreCommentModeration from a dict
score_comment_moderation_form_dict = score_comment_moderation.from_dict(score_comment_moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


