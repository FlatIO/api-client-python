# LtiConfigurationCreate1p3Deployment

LTI 1.3 deployment-based configuration creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | LTI 1.3 deployment-based creation mode | 
**deployment_type** | **str** | Parent platform key (e.g., canvas, blackboard, schoology, classlink) | 
**deployment_id** | **str** | Deployment identifier provided by the platform | 
**client_id** | **str** | OAuth2 client_id for the tenant; required for ClassLink deployments | [optional] 
**deployment_breakdown_id** | **str** | Value of the custom claim that identifies this specific tenant (for multi-tenant platforms like Schoology) | [optional] 

## Example

```python
from flat_api.models.lti_configuration_create1p3_deployment import LtiConfigurationCreate1p3Deployment

# TODO update the JSON string below
json = "{}"
# create an instance of LtiConfigurationCreate1p3Deployment from a JSON string
lti_configuration_create1p3_deployment_instance = LtiConfigurationCreate1p3Deployment.from_json(json)
# print the JSON string representation of the object
print(LtiConfigurationCreate1p3Deployment.to_json())

# convert the object into a dict
lti_configuration_create1p3_deployment_dict = lti_configuration_create1p3_deployment_instance.to_dict()
# create an instance of LtiConfigurationCreate1p3Deployment from a dict
lti_configuration_create1p3_deployment_from_dict = LtiConfigurationCreate1p3Deployment.from_dict(lti_configuration_create1p3_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


