# OmrJobInputFile

A single image or PDF input, base64-encoded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytes** | File data, base64-encoded. The type is read from the content itself, so no declared MIME type or filename extension is needed. Accepted types are listed by &#x60;getOmrCapabilities&#x60; in &#x60;acceptedMimeTypes&#x60;.  | 
**filename** | **str** | Optional original filename, kept for display. | [optional] 

## Example

```python
from flat_api.models.omr_job_input_file import OmrJobInputFile

# TODO update the JSON string below
json = "{}"
# create an instance of OmrJobInputFile from a JSON string
omr_job_input_file_instance = OmrJobInputFile.from_json(json)
# print the JSON string representation of the object
print(OmrJobInputFile.to_json())

# convert the object into a dict
omr_job_input_file_dict = omr_job_input_file_instance.to_dict()
# create an instance of OmrJobInputFile from a dict
omr_job_input_file_from_dict = OmrJobInputFile.from_dict(omr_job_input_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


