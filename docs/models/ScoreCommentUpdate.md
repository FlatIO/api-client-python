# flat_api.model.score_comment_update.ScoreCommentUpdate

Update of a comment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Update of a comment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**revision** | str,  | str,  | The unique indentifier of the revision of the score where the comment was added. If this property is unspecified or contains \&quot;last\&quot;, the API will automatically take the last revision created.  | [optional] 
**comment** | str,  | str,  | The comment text that can includes mentions using the following format: &#x60;@[id:username]&#x60;.  | [optional] 
**rawComment** | str,  | str,  | A raw version of the comment, that can be displayed without the mentions. If you use mentions, this property must be set.  | [optional] 
**context** | [**ScoreCommentContext**](ScoreCommentContext.md) | [**ScoreCommentContext**](ScoreCommentContext.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

