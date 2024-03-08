# ScoreCreationBuilderDataLayoutData

Control the appearance of the score. If missing, default values are used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes_spacing_coeff** | **float** | A float value &gt;&#x3D; 1 that controls the spacing between notes. | [optional] 
**length_unit** | **str** | The unit to use for layout customizations | [optional] [default to 'cm']
**page_height** | **float** | The height of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**page_width** | **float** | The width of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**page_margin_top** | **float** | The top margin of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**page_margin_bottom** | **float** | The bottom margin of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**page_margin_left** | **float** | The left margin of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 
**page_margin_right** | **float** | The right margin of the page in chosen unit (&#x60;lengthUnit&#x60;). | [optional] 

## Example

```python
from flat_api.models.score_creation_builder_data_layout_data import ScoreCreationBuilderDataLayoutData

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreCreationBuilderDataLayoutData from a JSON string
score_creation_builder_data_layout_data_instance = ScoreCreationBuilderDataLayoutData.from_json(json)
# print the JSON string representation of the object
print ScoreCreationBuilderDataLayoutData.to_json()

# convert the object into a dict
score_creation_builder_data_layout_data_dict = score_creation_builder_data_layout_data_instance.to_dict()
# create an instance of ScoreCreationBuilderDataLayoutData from a dict
score_creation_builder_data_layout_data_form_dict = score_creation_builder_data_layout_data.from_dict(score_creation_builder_data_layout_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


