# flat_api.model.score_comment.ScoreComment

Comment added on a sheet music

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Comment added on a sheet music | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The comment unique identifier | [optional] 
**type** | str,  | str,  | The type of the comment | [optional] must be one of ["document", "inline", ] 
**user** | str,  | str,  | The author unique identifier | [optional] 
**score** | str,  | str,  | The unique identifier of the score where the comment was posted | [optional] 
**revision** | str,  | str,  | The unique identifier of revision the comment was posted | [optional] 
**replyTo** | str,  | str,  | When the comment is a reply to another comment, the unique identifier of the parent comment  | [optional] 
**date** | str, datetime,  | str,  | The date when the comment was posted | [optional] value must conform to RFC-3339 date-time
**modificationDate** | str, datetime,  | str,  | The date of the last comment modification | [optional] value must conform to RFC-3339 date-time
**comment** | str,  | str,  | The comment text that can includes mentions using the following format: &#x60;@[id:username]&#x60;.  | [optional] 
**rawComment** | str,  | str,  | A raw version of the comment, that can be displayed without parsing the mentions.  | [optional] 
**context** | [**ScoreCommentContext**](ScoreCommentContext.md) | [**ScoreCommentContext**](ScoreCommentContext.md) |  | [optional] 
**[mentions](#mentions)** | list, tuple,  | tuple,  | The list of user identifier mentioned on the score | [optional] 
**resolved** | bool,  | BoolClass,  | For inline comments, the comment can be marked as resolved and will be hidden in the future responses  | [optional] 
**resolvedBy** | str,  | str,  | If the user is marked as resolved, this will contain the unique identifier of the User who marked this comment as resolved  | [optional] 
**[moderation](#moderation)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the comment being moderated | [optional] 
**spam** | bool,  | BoolClass,  | &#x60;true  if the message has been detected as spam and hidden from other users  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mentions

The list of user identifier mentioned on the score

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of user identifier mentioned on the score | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# moderation

Information about the comment being moderated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the comment being moderated | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hidden** | bool,  | BoolClass,  | If true, this comment will be hidden from other users | [optional] 
**reason** | str,  | str,  | If the comment is hidden, the reason why this one has been moderated | [optional] must be one of ["spam", "inappropriate", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

