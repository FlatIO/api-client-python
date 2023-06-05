# ResourceCollaboratorCreation

Add a collaborator to a resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | The unique identifier of a Flat user | [optional] 
**group** | **str** | The unique identifier of a Flat group | [optional] 
**user_email** | **str** | Fill this field to invite an individual user by email.  | [optional] 
**user_token** | **str** | Token received in an invitation to join the score.  | [optional] 
**acl_read** | **bool** | &#x60;True&#x60; if the related user can read the score. (probably true if the user has a permission on the document).  | [optional]  if omitted the server will use the default value of True
**acl_write** | **bool** | &#x60;True&#x60; if the related user can modify the score.  | [optional]  if omitted the server will use the default value of False
**acl_admin** | **bool** | &#x60;True&#x60; if the related user can can manage the current document, i.e. changing the document permissions and deleting the document  | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


