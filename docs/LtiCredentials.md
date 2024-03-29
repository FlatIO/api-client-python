# LtiCredentials

A couple of LTI 1.x OAuth credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of this couple of credentials | [optional] 
**name** | **str** | Name of the couple of credentials | [optional] 
**lms** | [**LmsName**](LmsName.md) |  | [optional] 
**organization** | **str** | The unique identifier of the Organization associated to these credentials | [optional] 
**creator** | **str** | Unique identifier of the user who created these credentials | [optional] 
**creation_date** | **datetime** | The creation date of thse credentials | [optional] 
**last_usage** | **datetime** | The last time these credentials were used | [optional] 
**consumer_key** | **str** | OAuth 1 Consumer Key | [optional] 
**consumer_secret** | **str** | OAuth 1 Consumer Secret | [optional] 

## Example

```python
from flat_api.models.lti_credentials import LtiCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of LtiCredentials from a JSON string
lti_credentials_instance = LtiCredentials.from_json(json)
# print the JSON string representation of the object
print LtiCredentials.to_json()

# convert the object into a dict
lti_credentials_dict = lti_credentials_instance.to_dict()
# create an instance of LtiCredentials from a dict
lti_credentials_form_dict = lti_credentials.from_dict(lti_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


