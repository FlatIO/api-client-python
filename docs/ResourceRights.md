# ResourceRights

The rights of the current user on a score or collection
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl_read** | **bool** | &#x60;True&#x60; if the current user can read the current document  | [optional] [default to False]
**acl_write** | **bool** | &#x60;True&#x60; if the current user can modify the current document.  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [optional] [default to False]
**acl_admin** | **bool** | &#x60;True&#x60; if the current user can manage the current document (i.e. share, delete)  If this is a right of a Collection, the capabilities of the associated user can be lower than this permission, check out the &#x60;capabilities&#x60; property as the end-user to have the complete possibilities with the collection.  | [optional] [default to False]
**is_collaborator** | **bool** | &#x60;True&#x60; if the current user is a collaborator of the current document (direct or via group).  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


