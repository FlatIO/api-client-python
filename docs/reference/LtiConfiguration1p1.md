# LtiConfiguration1p1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Configuration ID | 
**lti_version** | **str** | LTI version (1.1) | 
**organization_id** | **str** | Organization ID | [optional] 
**organization_name** | **str** | Organization name | [optional] 
**creator_id** | **str** | ID of the user who created this configuration | [optional] 
**creation_date** | **datetime** | Configuration creation date | 
**last_used_date** | **datetime** | Last time this configuration was used | [optional] 
**status** | **str** | Configuration status indicator | [optional] 
**consumer_key** | **str** | LTI 1.1 consumer key | [optional] 
**consumer_secret** | **str** | LTI 1.1 consumer secret (only included for admins) | [optional] 
**lms** | **str** | LMS type | [optional] 
**name** | **str** | Configuration name | [optional] 
**tool** | [**LtiConfiguration1p1AllOfTool**](LtiConfiguration1p1AllOfTool.md) |  | [optional] 

## Example

```python
from flat_api.models.lti_configuration1p1 import LtiConfiguration1p1

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfiguration1p1 from a JSON string
lti_configuration1p1_instance = LtiConfiguration1p1.from_json(json)
# print the JSON string representation of the object
print(LtiConfiguration1p1.to_json())

# convert the object into a dict
lti_configuration1p1_dict = lti_configuration1p1_instance.to_dict()
# create an instance of LtiConfiguration1p1 from a dict
lti_configuration1p1_from_dict = LtiConfiguration1p1.from_dict(lti_configuration1p1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


