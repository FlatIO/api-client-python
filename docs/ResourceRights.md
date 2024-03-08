# ResourceRights

The rights of the current user on a score or collection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl_read** | **bool** | &#x60;True&#x60; if the current user can read the current document  | [default to False]
**acl_write** | **bool** | &#x60;True&#x60; if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [default to False]
**acl_admin** | **bool** | &#x60;True&#x60; if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [default to False]
**is_collaborator** | **bool** | &#x60;True&#x60; if the current user is a collaborator of the current document (direct or via group).  | [default to False]
**collaborator_type** | **str** | The type of the collaborator for the resource  | [optional] 

## Example

```python
from flat_api.models.resource_rights import ResourceRights

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRights from a JSON string
resource_rights_instance = ResourceRights.from_json(json)
# print the JSON string representation of the object
print ResourceRights.to_json()

# convert the object into a dict
resource_rights_dict = resource_rights_instance.to_dict()
# create an instance of ResourceRights from a dict
resource_rights_form_dict = resource_rights.from_dict(resource_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


