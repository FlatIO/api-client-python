# ResourceCollaborator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl_read** | **bool** | &#x60;True&#x60; if the current user can read the current document  | [default to False]
**acl_write** | **bool** | &#x60;True&#x60; if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [default to False]
**acl_admin** | **bool** | &#x60;True&#x60; if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [default to False]
**is_collaborator** | **bool** | &#x60;True&#x60; if the current user is a collaborator of the current document (direct or via group).  | [default to False]
**collaborator_type** | **str** | The type of the collaborator for the resource  | [optional] 
**id** | **str** | The unique identifier of the permission | [optional] 
**var_date** | **datetime** | The date when the permission was added | [optional] 
**score** | **str** | If this object is a permission of a score, this property will contain the unique identifier of the score | [optional] 
**collection** | **str** | If this object is a permission of a collection, this property will contain the unique identifier of the collection | [optional] 
**user** | [**UserPublic**](UserPublic.md) |  | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**user_email** | **str** | If the collaborator is not a user of Flat yet, this field will contain their email.  | [optional] 
**invited** | **bool** | If this property is &#x60;true&#x60;, this is still a pending invitation  | [optional] 

## Example

```python
from flat_api.models.resource_collaborator import ResourceCollaborator

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCollaborator from a JSON string
resource_collaborator_instance = ResourceCollaborator.from_json(json)
# print the JSON string representation of the object
print ResourceCollaborator.to_json()

# convert the object into a dict
resource_collaborator_dict = resource_collaborator_instance.to_dict()
# create an instance of ResourceCollaborator from a dict
resource_collaborator_form_dict = resource_collaborator.from_dict(resource_collaborator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


