# OmrJobCreation

Parameters to create an OMR job. Send without `files` to create a draft (then add files with `addOmrJobFile` and run `startOmrJob`), or include `files` and `autoStart: true` to import in a single request. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | [**OmrJobOutput**](OmrJobOutput.md) |  | [optional] [default to OmrJobOutput.LIBRARY]
**interactive_steps** | [**List[OmrStepName]**](OmrStepName.md) | Steps at which the pipeline should pause for this client. Omit or send &#x60;[]&#x60; for a fully automatic import. The server only pauses at the steps listed here; declare only steps your client can actually render.  | [optional] [default to []]
**locales** | **List[str]** | Locale hints (BCP 47) to improve text and lyric detection, for example &#x60;[\&quot;ja\&quot;, \&quot;en\&quot;]&#x60;. The first entry drives the OCR reader. This is the input hint; the detected main language is confirmed later at the &#x60;details&#x60; step.  | [optional] 
**collection** | **str** | Target collection ID. Only used when &#x60;output&#x60; is &#x60;library&#x60;. | [optional] 
**idempotency_key** | **str** | Optional client-supplied key. A retry with the same key returns the existing job instead of creating a duplicate, for safe retries on flaky networks.  | [optional] 
**files** | [**List[OmrJobInputFile]**](OmrJobInputFile.md) | Optional inline inputs for a one-shot import. For multi-image or mobile capture, omit this and use &#x60;addOmrJobFile&#x60;. | [optional] 
**auto_start** | **bool** | Start processing immediately. Only valid when &#x60;files&#x60; is provided. | [optional] 

## Example

```python
from flat_api.models.omr_job_creation import OmrJobCreation

# TODO update the JSON string below
json = "{}"
# create an instance of OmrJobCreation from a JSON string
omr_job_creation_instance = OmrJobCreation.from_json(json)
# print the JSON string representation of the object
print(OmrJobCreation.to_json())

# convert the object into a dict
omr_job_creation_dict = omr_job_creation_instance.to_dict()
# create an instance of OmrJobCreation from a dict
omr_job_creation_from_dict = OmrJobCreation.from_dict(omr_job_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


