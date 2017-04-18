# ScoreCommentUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** | The unique indentifier of the revision of the score where the comment was added. If this property is unspecified or contains \&quot;last\&quot;, the API will automatically take the last revision created.  | [optional] 
**comment** | **str** | The comment text that can includes mentions using the following format: &#x60;@[id:username]&#x60;.  | [optional] 
**raw_comment** | **str** | A raw version of the comment, that can be displayed without the mentions. If you use mentions, this property must be set.  | [optional] 
**context** | [**ScoreCommentContext**](ScoreCommentContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


