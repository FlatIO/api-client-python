# flat_api.model.score_comment_creation.ScoreCommentCreation

Creation of a comment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Creation of a comment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**comment** | str,  | str,  | The comment text that can includes mentions using the following format: &#x60;@[id:username]&#x60;.  | 
**revision** | str,  | str,  | The unique indentifier of the revision of the score where the comment was added. If this property is unspecified or contains \&quot;last\&quot;, the API will automatically take the last revision created.  | [optional] 
**rawComment** | str,  | str,  | A raw version of the comment, that can be displayed without the mentions. If you use mentions, this property must be set.  | [optional] 
**[mentions](#mentions)** | list, tuple,  | tuple,  | The list of user identifiers mentioned in this comment | [optional] 
**replyTo** | str,  | str,  | When the comment is a reply to another comment, the unique identifier of the parent comment  | [optional] 
**context** | [**ScoreCommentContext**](ScoreCommentContext.md) | [**ScoreCommentContext**](ScoreCommentContext.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mentions

The list of user identifiers mentioned in this comment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of user identifiers mentioned in this comment | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

