# CollectionContents

The contents of the collection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scores_count** | **int** | The number of scores in the collection | 

## Example

```python
from flat_api.models.collection_contents import CollectionContents

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionContents from a JSON string
collection_contents_instance = CollectionContents.from_json(json)
# print the JSON string representation of the object
print(CollectionContents.to_json())

# convert the object into a dict
collection_contents_dict = collection_contents_instance.to_dict()
# create an instance of CollectionContents from a dict
collection_contents_from_dict = CollectionContents.from_dict(collection_contents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


