# ResourceCollaborator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl_read** | **bool** | &#x60;True&#x60; if the current user can read the current document  | [optional] [default to False]
**acl_write** | **bool** | &#x60;True&#x60; if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [optional] [default to False]
**acl_admin** | **bool** | &#x60;True&#x60; if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [optional] [default to False]
**id** | **str** | The unique identifier of the permission | [optional] 
**score** | **str** | If this object is a permission of a score, this property will contain the unique identifier of the score | [optional] 
**collection** | **str** | If this object is a permission of a collection, this property will contain the unique identifier of the collection | [optional] 
**user** | [**UserPublic**](UserPublic.md) |  | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**user_email** | **str** | If the collaborator is not a user of Flat yet, this field will contain his email.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


