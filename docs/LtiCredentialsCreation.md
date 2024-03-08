# LtiCredentialsCreation

Creation of a couple of LTI 1.x OAuth credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the couple of credentials | 
**lms** | [**LmsName**](LmsName.md) |  | 

## Example

```python
from flat_api.models.lti_credentials_creation import LtiCredentialsCreation

# TODO update the JSON string below
json = "{}"
# create an instance of LtiCredentialsCreation from a JSON string
lti_credentials_creation_instance = LtiCredentialsCreation.from_json(json)
# print the JSON string representation of the object
print LtiCredentialsCreation.to_json()

# convert the object into a dict
lti_credentials_creation_dict = lti_credentials_creation_instance.to_dict()
# create an instance of LtiCredentialsCreation from a dict
lti_credentials_creation_form_dict = lti_credentials_creation.from_dict(lti_credentials_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


