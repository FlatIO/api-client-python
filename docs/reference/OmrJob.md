# OmrJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the OMR job. | 
**status** | [**OmrJobStatus**](OmrJobStatus.md) |  | 
**output** | [**OmrJobOutput**](OmrJobOutput.md) |  | [default to OmrJobOutput.LIBRARY]
**interactive_steps** | [**List[OmrStepName]**](OmrStepName.md) | Steps this job pauses at for client input, echoing the value set at creation. | 
**locales** | **List[str]** | Locale hints (BCP 47) the job was created with, used for OCR and as the default main language at the &#x60;details&#x60; step.  | [optional] 
**current_step** | [**OmrStepName**](OmrStepName.md) | The pending step when &#x60;status&#x60; is &#x60;awaitingInput&#x60;. Omitted otherwise. | [optional] 
**pending_step** | [**OmrPendingStep**](OmrPendingStep.md) |  | [optional] 
**estimated_credits** | **int** | Credits that will be or were charged at start (page-based), so a client can show a confirmation before charging. | [optional] 
**progress** | [**OmrJobProgress**](OmrJobProgress.md) |  | [optional] 
**original_file_metadata** | [**OmrJobFileMetadata**](OmrJobFileMetadata.md) |  | [optional] 
**imported_metadata** | [**OmrImportedMetadata**](OmrImportedMetadata.md) |  | [optional] 
**result** | [**OmrJobResult**](OmrJobResult.md) |  | [optional] 
**retention** | [**OmrJobRetention**](OmrJobRetention.md) |  | [optional] 
**error_code** | **str** | Stable, engine-agnostic failure code, present when &#x60;status&#x60; is &#x60;error&#x60;. Branch on this for custom handling, and render &#x60;errorMessage&#x60; for the user-facing text.  This is an open string: new codes may be added over time, so keep a generic fallback and never hardcode an exhaustive switch. Current values:  * &#x60;NO_MUSIC_DETECTED&#x60;: no musical content found (poor scan, rotated page, or tablature). * &#x60;CORRUPTED_FILE&#x60;: the input file is corrupted and could not be read. * &#x60;UNSUPPORTED_FORMAT&#x60;: the file format or notation is not supported yet. * &#x60;UNSUPPORTED_TABLATURE&#x60;: the file is guitar tablature, not supported yet. * &#x60;ENCRYPTED_PDF&#x60;: the PDF is password-protected. * &#x60;TOO_LARGE&#x60;: the document is too large or has an unusual shape to process. * &#x60;ENGINE_TIMEOUT&#x60;: recognition took longer than expected and was stopped. * &#x60;GENERIC&#x60;: unspecified failure.  | [optional] 
**error_message** | **str** | Localized, user-facing error message, present when &#x60;status&#x60; is &#x60;error&#x60;. Rendered in the caller&#39;s locale and safe to display as-is. Pair with &#x60;errorCode&#x60; for branching.  | [optional] 
**creation_date** | **datetime** | When the job was created. | [optional] 
**modification_date** | **datetime** | When the job was last updated. | [optional] 

## Example

```python
from flat_api.models.omr_job import OmrJob

# TODO update the JSON string below
json = "{}"
# create an instance of OmrJob from a JSON string
omr_job_instance = OmrJob.from_json(json)
# print the JSON string representation of the object
print(OmrJob.to_json())

# convert the object into a dict
omr_job_dict = omr_job_instance.to_dict()
# create an instance of OmrJob from a dict
omr_job_from_dict = OmrJob.from_dict(omr_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


