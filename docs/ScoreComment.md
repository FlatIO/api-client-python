# ScoreComment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The comment unique identifier | [optional] 
**type** | **str** | The type of the comment | [optional] 
**user** | **str** | The author unique identifier | [optional] 
**score** | **str** | The unique identifier of the score where the comment was posted | [optional] 
**revision** | **str** | The unique identifier of revision the comment was posted | [optional] 
**reply_to** | **str** | When the comment is a reply to another comment, the unique identifier of the parent comment  | [optional] 
**date** | **datetime** | The date when the comment was posted | [optional] 
**modification_date** | **datetime** | The date of the last comment modification | [optional] 
**comment** | **str** | The comment text that can includes mentions using the following format: &#x60;@[id:username]&#x60;.  | [optional] 
**raw_comment** | **str** | A raw version of the comment, that can be displayed without parsing the mentions.  | [optional] 
**context** | [**ScoreCommentContext**](ScoreCommentContext.md) |  | [optional] 
**mentions** | **list[str]** | The list of user identifier mentioned on the score | [optional] 
**resolved** | **bool** | For inline comments, the comment can be marked as resolved and will be hidden in the future responses  | [optional] 
**resolved_by** | **str** | If the user is marked as resolved, this will contain the unique identifier of the User who marked this comment as resolved  | [optional] 
**moderation** | [**ScoreCommentModeration**](ScoreCommentModeration.md) |  | [optional] 
**spam** | **bool** | &#x60;true  if the message has been detected as spam and hidden from other users  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


