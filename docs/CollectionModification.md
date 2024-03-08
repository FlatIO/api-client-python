# CollectionModification

Edit the collection metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the collection | [optional] 
**privacy** | [**CollectionPrivacy**](CollectionPrivacy.md) |  | [optional] 

## Example

```python
from flat_api.models.collection_modification import CollectionModification

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionModification from a JSON string
collection_modification_instance = CollectionModification.from_json(json)
# print the JSON string representation of the object
print CollectionModification.to_json()

# convert the object into a dict
collection_modification_dict = collection_modification_instance.to_dict()
# create an instance of CollectionModification from a dict
collection_modification_form_dict = collection_modification.from_dict(collection_modification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


