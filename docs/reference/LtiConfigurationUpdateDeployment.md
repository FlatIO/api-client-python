# LtiConfigurationUpdateDeployment

Update fields allowed for deployment-based configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** | Deployment identifier provided by the platform | [optional] 
**deployment_breakdown_id** | **str** | Specific tenant identifier for multi-tenant platforms | [optional] 
**enable_email_matching** | **bool** | Enable email-based user matching during LTI authentication | [optional] 

## Example

```python
from flat_api.models.lti_configuration_update_deployment import LtiConfigurationUpdateDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationUpdateDeployment from a JSON string
lti_configuration_update_deployment_instance = LtiConfigurationUpdateDeployment.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationUpdateDeployment.to_json())

# convert the object into a dict
lti_configuration_update_deployment_dict = lti_configuration_update_deployment_instance.to_dict()
# create an instance of LtiConfigurationUpdateDeployment from a dict
lti_configuration_update_deployment_from_dict = LtiConfigurationUpdateDeployment.from_dict(lti_configuration_update_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


