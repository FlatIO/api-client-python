# OmrImportedMetadata

Metadata extracted from the recognized score.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruments** | **List[str]** | Instrument IDs of the assembled parts. | [optional] 
**number_measures** | **int** | Number of measures in the recognized score. | [optional] 
**main_tempo_qpm** | **float** | Main tempo, in quarter notes per minute. | [optional] 
**main_key_signature** | **int** | Main key signature as a fifths count (negative for flats, positive for sharps, 0 for C major / A minor). | [optional] 

## Example

```python
from flat_api.models.omr_imported_metadata import OmrImportedMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OmrImportedMetadata from a JSON string
omr_imported_metadata_instance = OmrImportedMetadata.from_json(json)
# print the JSON string representation of the object
print(OmrImportedMetadata.to_json())

# convert the object into a dict
omr_imported_metadata_dict = omr_imported_metadata_instance.to_dict()
# create an instance of OmrImportedMetadata from a dict
omr_imported_metadata_from_dict = OmrImportedMetadata.from_dict(omr_imported_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


