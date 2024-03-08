# Collection

Collection of scores

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the collection | [optional] 
**title** | **str** | The title of the collection | [optional] 
**html_url** | **str** | The url where the collection can be viewed in a web browser | [optional] 
**type** | [**CollectionType**](CollectionType.md) |  | [optional] 
**privacy** | [**CollectionPrivacy**](CollectionPrivacy.md) |  | [optional] 
**sharing_key** | **str** | The private sharing key of the collection (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) | [optional] 
**app** | [**CollectionApp**](CollectionApp.md) |  | [optional] 
**creation_date** | **datetime** | The date when the collection was created | [optional] 
**user** | [**UserPublicSummary**](UserPublicSummary.md) |  | [optional] 
**organization** | **str** | If the score has been created in an organization, the identifier of this organization.   | [optional] 
**rights** | [**ResourceRights**](ResourceRights.md) |  | [optional] 
**collaborators** | [**List[ResourceCollaborator]**](ResourceCollaborator.md) | The list of the collaborators of the collection | [optional] 
**capabilities** | [**CollectionCapabilities**](CollectionCapabilities.md) |  | 
**collections** | **List[str]** | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. | [optional] 

## Example

```python
from flat_api.models.collection import Collection

# TODO update the JSON string below
json = "{}"
# create an instance of Collection from a JSON string
collection_instance = Collection.from_json(json)
# print the JSON string representation of the object
print Collection.to_json()

# convert the object into a dict
collection_dict = collection_instance.to_dict()
# create an instance of Collection from a dict
collection_form_dict = collection.from_dict(collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


