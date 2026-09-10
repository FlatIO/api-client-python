# OmrLocaleDetails

An OCR-selectable locale with its English name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | BCP 47 locale code. Always one of the codes listed in &#x60;locales&#x60;. | 
**name** | **str** | English name of the language, for display in a picker. | 

## Example

```python
from flat_api.models.omr_locale_details import OmrLocaleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OmrLocaleDetails from a JSON string
omr_locale_details_instance = OmrLocaleDetails.from_json(json)
# print the JSON string representation of the object
print(OmrLocaleDetails.to_json())

# convert the object into a dict
omr_locale_details_dict = omr_locale_details_instance.to_dict()
# create an instance of OmrLocaleDetails from a dict
omr_locale_details_from_dict = OmrLocaleDetails.from_dict(omr_locale_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


