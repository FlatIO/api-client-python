# FlatErrorResponse

An API Error response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A corresponding code for this error | 
**message** | **str** | A printable message for this error | 
**id** | **str** | An unique error identifier generated for the request | [optional] 
**param** | **str** | The related parameter that caused the error | [optional] 
**provider_message** | **str** | The untranslated error message returned by an external provider (e.g. Google Classroom), when the error originates from one. Only set on errors forwarded from a third party.  Meant for support and IT: display it alongside &#x60;message&#x60;, never in place of it. &#x60;message&#x60; is the localized, user-facing text; this field is raw provider output and is always in English.  | [optional] 

## Example

```python
from flat_api.models.flat_error_response import FlatErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlatErrorResponse from a JSON string
flat_error_response_instance = FlatErrorResponse.from_json(json)
# print the JSON string representation of the object
print(FlatErrorResponse.to_json())

# convert the object into a dict
flat_error_response_dict = flat_error_response_instance.to_dict()
# create an instance of FlatErrorResponse from a dict
flat_error_response_from_dict = FlatErrorResponse.from_dict(flat_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


