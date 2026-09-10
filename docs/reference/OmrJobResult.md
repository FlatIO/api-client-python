# OmrJobResult

The outcome of a finished job. Present when `status` is `done`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** | Created score ID, when &#x60;output&#x60; is &#x60;library&#x60;. | [optional] 
**exports** | **List[str]** | Formats available via &#x60;getOmrJobExport&#x60;, for example &#x60;[\&quot;musicxml\&quot;, \&quot;mxl\&quot;, \&quot;midi\&quot;]&#x60;. | [optional] 

## Example

```python
from flat_api.models.omr_job_result import OmrJobResult

# TODO update the JSON string below
json = "{}"
# create an instance of OmrJobResult from a JSON string
omr_job_result_instance = OmrJobResult.from_json(json)
# print the JSON string representation of the object
print(OmrJobResult.to_json())

# convert the object into a dict
omr_job_result_dict = omr_job_result_instance.to_dict()
# create an instance of OmrJobResult from a dict
omr_job_result_from_dict = OmrJobResult.from_dict(omr_job_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


