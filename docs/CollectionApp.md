# CollectionApp

For App collections, the details of the app that created the collection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The app unique identifier | [optional] 
**name** | **str** | The name of the app | [optional] 
**logo** | **str** | The app logo url | [optional] 

## Example

```python
from flat_api.models.collection_app import CollectionApp

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionApp from a JSON string
collection_app_instance = CollectionApp.from_json(json)
# print the JSON string representation of the object
print CollectionApp.to_json()

# convert the object into a dict
collection_app_dict = collection_app_instance.to_dict()
# create an instance of CollectionApp from a dict
collection_app_form_dict = collection_app.from_dict(collection_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


