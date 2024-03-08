# ScoreCommentCreation

Creation of a comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** | The unique indentifier of the revision of the score where the comment was added. If this property is unspecified or contains \&quot;last\&quot;, the API will automatically take the last revision created.  | [optional] 
**comment** | **str** | The comment text that can includes mentions using the following format: &#x60;@[id:username]&#x60;.  | 
**raw_comment** | **str** | A raw version of the comment, that can be displayed without the mentions. If you use mentions, this property must be set.  | [optional] 
**mentions** | **List[str]** | The list of user identifiers mentioned in this comment | [optional] 
**reply_to** | **str** | When the comment is a reply to another comment, the unique identifier of the parent comment  | [optional] 
**context** | [**ScoreCommentContext**](ScoreCommentContext.md) |  | [optional] 

## Example

```python
from flat_api.models.score_comment_creation import ScoreCommentCreation

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreCommentCreation from a JSON string
score_comment_creation_instance = ScoreCommentCreation.from_json(json)
# print the JSON string representation of the object
print ScoreCommentCreation.to_json()

# convert the object into a dict
score_comment_creation_dict = score_comment_creation_instance.to_dict()
# create an instance of ScoreCommentCreation from a dict
score_comment_creation_form_dict = score_comment_creation.from_dict(score_comment_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


