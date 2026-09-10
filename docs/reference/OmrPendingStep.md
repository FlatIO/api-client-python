# OmrPendingStep

The step currently awaiting client input. The `data` shape is keyed by `step`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step** | [**OmrStepName**](OmrStepName.md) |  | 
**data** | [**OmrDetailsStepData**](OmrDetailsStepData.md) |  | 

## Example

```python
from flat_api.models.omr_pending_step import OmrPendingStep

# TODO update the JSON string below
json = "{}"
# create an instance of OmrPendingStep from a JSON string
omr_pending_step_instance = OmrPendingStep.from_json(json)
# print the JSON string representation of the object
print(OmrPendingStep.to_json())

# convert the object into a dict
omr_pending_step_dict = omr_pending_step_instance.to_dict()
# create an instance of OmrPendingStep from a dict
omr_pending_step_from_dict = OmrPendingStep.from_dict(omr_pending_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


