# OmrDetailsStepData

Detected score details for the client to review before the score is built. `title` and `instruments` are detected from the input; the language is not detected and is not part of this payload (read the job's `locales`, set at creation). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step** | **str** | Discriminator for &#x60;OmrPendingStep.data&#x60;; always &#x60;details&#x60; for this payload. | 
**title** | **str** | OCR-detected work title. | [optional] 
**instruments** | [**List[OmrDetectedInstrument]**](OmrDetectedInstrument.md) |  | 

## Example

```python
from flat_api.models.omr_details_step_data import OmrDetailsStepData

# TODO update the JSON string below
json = "{}"
# create an instance of OmrDetailsStepData from a JSON string
omr_details_step_data_instance = OmrDetailsStepData.from_json(json)
# print the JSON string representation of the object
print(OmrDetailsStepData.to_json())

# convert the object into a dict
omr_details_step_data_dict = omr_details_step_data_instance.to_dict()
# create an instance of OmrDetailsStepData from a dict
omr_details_step_data_from_dict = OmrDetailsStepData.from_dict(omr_details_step_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


