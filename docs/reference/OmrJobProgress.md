# OmrJobProgress

Live progress while the job is processing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **float** | Completion percentage (0-100). | [optional] 
**text** | **str** | Localized progress message, ready to display. | [optional] 
**key** | **str** | Stable progress key (for example &#x60;OMR_QUEUED&#x60;, &#x60;OMR_PROCESSING_PAGE&#x60;, &#x60;OMR_CREATING_SCORE&#x60;), for matching the current phase in a stepper UI independent of locale.  | [optional] 

## Example

```python
from flat_api.models.omr_job_progress import OmrJobProgress

# TODO update the JSON string below
json = "{}"
# create an instance of OmrJobProgress from a JSON string
omr_job_progress_instance = OmrJobProgress.from_json(json)
# print the JSON string representation of the object
print(OmrJobProgress.to_json())

# convert the object into a dict
omr_job_progress_dict = omr_job_progress_instance.to_dict()
# create an instance of OmrJobProgress from a dict
omr_job_progress_from_dict = OmrJobProgress.from_dict(omr_job_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


