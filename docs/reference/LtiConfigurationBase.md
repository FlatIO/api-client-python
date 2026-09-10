# LtiConfigurationBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Configuration ID | 
**lti_version** | **str** | LTI version | 
**organization_id** | **str** | Organization ID | [optional] 
**organization_name** | **str** | Organization name | [optional] 
**creator_id** | **str** | ID of the user who created this configuration | [optional] 
**creation_date** | **datetime** | Configuration creation date | 
**last_used_date** | **datetime** | Last time this configuration was used | [optional] 
**status** | **str** | Configuration status indicator | [optional] 

## Example

```python
from flat_api.models.lti_configuration_base import LtiConfigurationBase

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationBase from a JSON string
lti_configuration_base_instance = LtiConfigurationBase.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationBase.to_json())

# convert the object into a dict
lti_configuration_base_dict = lti_configuration_base_instance.to_dict()
# create an instance of LtiConfigurationBase from a dict
lti_configuration_base_from_dict = LtiConfigurationBase.from_dict(lti_configuration_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


