# CollectionCapabilities

Capabilities the current user has on this collection. Each capability corresponds to a fine-grained action that a user may take.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_edit** | **bool** | Whether the current user can modify the metadata for the collection  | [optional] 
**can_share** | **bool** | Whether the current user can modify the sharing settings for the collection  | [optional] 
**can_delete** | **bool** | Whether the current user can delete the collection  | [optional] 
**can_add_scores** | **bool** | Whether the current user can add scores to the collection  If this collection has the &#x60;type&#x60; &#x60;trash&#x60;, this property will be set to &#x60;false&#x60;. Use &#x60;DELETE /v2/scores/{score}&#x60; to trash a score.  | [optional] 
**can_delete_scores** | **bool** | Whether the current user can delete scores from the collection  If this collection has the &#x60;type&#x60; &#x60;trash&#x60;, this property will be set to &#x60;false&#x60;. Use &#x60;POST /v2/scores/{score}/untrash&#x60; to restore a score.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


