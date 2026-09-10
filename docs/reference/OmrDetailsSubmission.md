# OmrDetailsSubmission

Overrides for the `details` step. Omitted fields keep the server's detected values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step** | **str** | Discriminator for &#x60;OmrStepSubmission&#x60;; always &#x60;details&#x60; for this submission. | 
**title** | **str** | Override the detected work title. | [optional] 
**main_language** | **str** | Override the main language (BCP 47) used for lyric and text reading on resume. Defaults to the job locale (&#x60;locales&#x60;); set this to correct it on the review screen.  | [optional] 
**instruments** | [**List[OmrInstrumentOverride]**](OmrInstrumentOverride.md) | Per-part overrides, each matched to a detected part by &#x60;index&#x60;. | [optional] 

## Example

```python
from flat_api.models.omr_details_submission import OmrDetailsSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of OmrDetailsSubmission from a JSON string
omr_details_submission_instance = OmrDetailsSubmission.from_json(json)
# print the JSON string representation of the object
print(OmrDetailsSubmission.to_json())

# convert the object into a dict
omr_details_submission_dict = omr_details_submission_instance.to_dict()
# create an instance of OmrDetailsSubmission from a dict
omr_details_submission_from_dict = OmrDetailsSubmission.from_dict(omr_details_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


