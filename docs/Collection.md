# Collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the collection | [optional] 
**title** | [**CollectionTitle**](CollectionTitle.md) |  | [optional] 
**html_url** | **str** | The url where the collection can be viewed in a web browser | [optional] 
**type** | [**CollectionType**](CollectionType.md) |  | [optional] 
**privacy** | [**CollectionPrivacy**](CollectionPrivacy.md) |  | [optional] 
**sharing_key** | **str** | The private sharing key of the collection (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) | [optional] 
**app** | **str** | If this directory is dedicated to an app, the unique idenfier of this app | [optional] 
**user** | [**UserPublicSummary**](UserPublicSummary.md) |  | [optional] 
**rights** | [**ResourceRights**](ResourceRights.md) |  | [optional] 
**collaborators** | [**list[ResourceCollaborator]**](ResourceCollaborator.md) | The list of the collaborators of the collection | [optional] 
**capabilities** | [**CollectionCapabilities**](CollectionCapabilities.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


