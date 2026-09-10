# Collection

Collection of scores

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the collection | 
**title** | **str** | The title of the collection | 
**html_url** | **str** | The url where the collection can be viewed in a web browser | 
**type** | [**CollectionType**](CollectionType.md) |  | 
**label_key** | **str** | Product-specific translation key for the collection type.  Only set for specific collection types: * For &#x60;regular&#x60; type: &#x60;playlist&#x60; (Flat) or &#x60;collection&#x60; (Flat for Education) * For &#x60;collaborations&#x60; type: &#x60;collaboration&#x60; (Flat) or &#x60;shared-scores&#x60; (Flat for Education)  Not set for other collection types.  | [optional] 
**privacy** | [**CollectionPrivacy**](CollectionPrivacy.md) |  | [default to CollectionPrivacy.PRIVATE]
**sharing_key** | **str** | The private sharing key of the collection (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) | [optional] 
**app** | [**CollectionApp**](CollectionApp.md) |  | [optional] 
**creation_date** | **datetime** | The date when the collection was created | 
**modification_date** | **datetime** | The date when the collection was last modified | [optional] 
**user** | [**UserPublicSummary**](UserPublicSummary.md) |  | [optional] 
**organization** | **str** | If the score has been created in an organization, the identifier of this organization.   | [optional] 
**rights** | [**ResourceRights**](ResourceRights.md) |  | [optional] 
**collaborators** | [**List[ResourceCollaborator]**](ResourceCollaborator.md) | The list of the collaborators of the collection | [optional] 
**is_pinned** | **bool** | Whether the collection is pinned by the owner | [optional] 
**contents** | [**CollectionContents**](CollectionContents.md) |  | 
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
print(Collection.to_json())

# convert the object into a dict
collection_dict = collection_instance.to_dict()
# create an instance of Collection from a dict
collection_from_dict = Collection.from_dict(collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


