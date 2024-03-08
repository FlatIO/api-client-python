# EduResourceLtiLink

LTI Link details for the class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lti_url** | **str** | An URL that can be used to launch LTI with this resource in a classroom. | 

## Example

```python
from flat_api.models.edu_resource_lti_link import EduResourceLtiLink

# TODO update the JSON string below
json = "{}"
# create an instance of EduResourceLtiLink from a JSON string
edu_resource_lti_link_instance = EduResourceLtiLink.from_json(json)
# print the JSON string representation of the object
print EduResourceLtiLink.to_json()

# convert the object into a dict
edu_resource_lti_link_dict = edu_resource_lti_link_instance.to_dict()
# create an instance of EduResourceLtiLink from a dict
edu_resource_lti_link_form_dict = edu_resource_lti_link.from_dict(edu_resource_lti_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


