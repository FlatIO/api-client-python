# Collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the collection | [optional] 
**title** | **str** | The title of the collection | [optional] 
**html_url** | **str** | The url where the collection can be viewed in a web browser | [optional] 
**type** | [**CollectionType**](CollectionType.md) |  | [optional] 
**privacy** | [**CollectionPrivacy**](CollectionPrivacy.md) |  | [optional] 
**sharing_key** | **str** | The private sharing key of the collection (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) | [optional] 
**app** | **str** | If this directory is dedicated to an app, the unique idenfier of this app | [optional] 
**creation_date** | **datetime** | The date when the collection was created | [optional] 
**user** | [**UserPublicSummary**](UserPublicSummary.md) |  | [optional] 
**rights** | [**ResourceRights**](ResourceRights.md) |  | [optional] 
**collaborators** | [**list[ResourceCollaborator]**](ResourceCollaborator.md) | The list of the collaborators of the collection | [optional] 
**capabilities** | [**CollectionCapabilities**](CollectionCapabilities.md) |  | [optional] 
**collections** | **list[str]** | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


