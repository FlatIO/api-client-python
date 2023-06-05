# flat_api.model.collection.Collection

Collection of scores

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of scores | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique identifier of the collection | [optional] 
**title** | str,  | str,  | The title of the collection | [optional] 
**htmlUrl** | str,  | str,  | The url where the collection can be viewed in a web browser | [optional] 
**type** | [**CollectionType**](CollectionType.md) | [**CollectionType**](CollectionType.md) |  | [optional] 
**privacy** | [**CollectionPrivacy**](CollectionPrivacy.md) | [**CollectionPrivacy**](CollectionPrivacy.md) |  | [optional] 
**sharingKey** | str,  | str,  | The private sharing key of the collection (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) | [optional] 
**app** | [**CollectionApp**](CollectionApp.md) | [**CollectionApp**](CollectionApp.md) |  | [optional] 
**creationDate** | str, datetime,  | str,  | The date when the collection was created | [optional] value must conform to RFC-3339 date-time
**user** | [**UserPublicSummary**](UserPublicSummary.md) | [**UserPublicSummary**](UserPublicSummary.md) |  | [optional] 
**rights** | [**ResourceRights**](ResourceRights.md) | [**ResourceRights**](ResourceRights.md) |  | [optional] 
**[collaborators](#collaborators)** | list, tuple,  | tuple,  | The list of the collaborators of the collection | [optional] 
**[capabilities](#capabilities)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Capabilities the current user has on this collection. Each capability corresponds to a fine-grained action that a user may take. | [optional] 
**[collections](#collections)** | list, tuple,  | tuple,  | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# collaborators

The list of the collaborators of the collection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of the collaborators of the collection | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceCollaborator**](ResourceCollaborator.md) | [**ResourceCollaborator**](ResourceCollaborator.md) | [**ResourceCollaborator**](ResourceCollaborator.md) |  | 

# capabilities

Capabilities the current user has on this collection. Each capability corresponds to a fine-grained action that a user may take.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Capabilities the current user has on this collection. Each capability corresponds to a fine-grained action that a user may take. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**canEdit** | bool,  | BoolClass,  | Whether the current user can modify the metadata for the collection  | [optional] 
**canShare** | bool,  | BoolClass,  | Whether the current user can modify the sharing settings for the collection  | [optional] 
**canDelete** | bool,  | BoolClass,  | Whether the current user can delete the collection  | [optional] 
**canAddScores** | bool,  | BoolClass,  | Whether the current user can add scores to the collection  If this collection has the &#x60;type&#x60; &#x60;trash&#x60;, this property will be set to &#x60;false&#x60;. Use &#x60;DELETE /v2/scores/{score}&#x60; to trash a score.  | [optional] 
**canDeleteScores** | bool,  | BoolClass,  | Whether the current user can delete scores from the collection  If this collection has the &#x60;type&#x60; &#x60;trash&#x60;, this property will be set to &#x60;false&#x60;. Use &#x60;POST /v2/scores/{score}/untrash&#x60; to restore a score.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# collections

The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

