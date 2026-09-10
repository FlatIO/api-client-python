# CreateLtiConfiguration200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_url** | **str** | One-time registration URL (only for dynamic registration) | [optional] 

## Example

```python
from flat_api.models.create_lti_configuration200_response import CreateLtiConfiguration200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLtiConfiguration200Response from a JSON string
create_lti_configuration200_response_instance = CreateLtiConfiguration200Response.from_json(json)
# print the JSON string representation of the object
print(CreateLtiConfiguration200Response.to_json())

# convert the object into a dict
create_lti_configuration200_response_dict = create_lti_configuration200_response_instance.to_dict()
# create an instance of CreateLtiConfiguration200Response from a dict
create_lti_configuration200_response_from_dict = CreateLtiConfiguration200Response.from_dict(create_lti_configuration200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


