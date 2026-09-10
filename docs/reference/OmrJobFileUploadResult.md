# OmrJobFileUploadResult

Result of adding a file to a draft job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_index** | **int** | 0-based index assigned to the uploaded file. | [optional] 
**file_count** | **int** | Total number of files now attached to the job. | [optional] 

## Example

```python
from flat_api.models.omr_job_file_upload_result import OmrJobFileUploadResult

# TODO update the JSON string below
json = "{}"
# create an instance of OmrJobFileUploadResult from a JSON string
omr_job_file_upload_result_instance = OmrJobFileUploadResult.from_json(json)
# print the JSON string representation of the object
print(OmrJobFileUploadResult.to_json())

# convert the object into a dict
omr_job_file_upload_result_dict = omr_job_file_upload_result_instance.to_dict()
# create an instance of OmrJobFileUploadResult from a dict
omr_job_file_upload_result_from_dict = OmrJobFileUploadResult.from_dict(omr_job_file_upload_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


