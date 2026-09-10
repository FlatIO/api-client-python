# OmrJobFileMetadata

Metadata about the uploaded input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_pages** | **int** | Total number of pages across all input files. | [optional] 
**file_count** | **int** | Number of input files attached. | [optional] 
**filename** | **str** | Original filename of the input as uploaded (of the first file when several were combined). | [optional] 
**file_size** | **int** | Combined size of the input files, in bytes. | [optional] 
**mime_type** | **str** | MIME type of the input (of the first file when several were combined). | [optional] 
**file_extension** | **str** | File extension of the input, without the leading dot (for example &#x60;pdf&#x60;). | [optional] 

## Example

```python
from flat_api.models.omr_job_file_metadata import OmrJobFileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OmrJobFileMetadata from a JSON string
omr_job_file_metadata_instance = OmrJobFileMetadata.from_json(json)
# print the JSON string representation of the object
print(OmrJobFileMetadata.to_json())

# convert the object into a dict
omr_job_file_metadata_dict = omr_job_file_metadata_instance.to_dict()
# create an instance of OmrJobFileMetadata from a dict
omr_job_file_metadata_from_dict = OmrJobFileMetadata.from_dict(omr_job_file_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


