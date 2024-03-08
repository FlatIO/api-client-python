# ClassDetailsMfc

Meta information provided by Canvs LMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the course on MusicFirst Classroom | [optional] 
**alternate_link** | **str** | Link to MusicFirst Classroom class | [optional] 

## Example

```python
from flat_api.models.class_details_mfc import ClassDetailsMfc

# TODO update the JSON string below
json = "{}"
# create an instance of ClassDetailsMfc from a JSON string
class_details_mfc_instance = ClassDetailsMfc.from_json(json)
# print the JSON string representation of the object
print ClassDetailsMfc.to_json()

# convert the object into a dict
class_details_mfc_dict = class_details_mfc_instance.to_dict()
# create an instance of ClassDetailsMfc from a dict
class_details_mfc_form_dict = class_details_mfc.from_dict(class_details_mfc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


