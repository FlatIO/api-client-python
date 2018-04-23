# ResourceCollaboratorCreation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | The unique identifier of a Flat user | [optional] 
**group** | **str** | The unique identifier of a Flat group | [optional] 
**user_email** | **str** | Fill this field to invite an individual user by email.  | [optional] 
**user_token** | **str** | Token received in an invitation to join the score.  | [optional] 
**acl_read** | **bool** | &#x60;True&#x60; if the related user can read the score. (probably true if the user has a permission on the document).  | [optional] [default to True]
**acl_write** | **bool** | &#x60;True&#x60; if the related user can modify the score.  | [optional] [default to False]
**acl_admin** | **bool** | &#x60;True&#x60; if the related user can can manage the current document, i.e. changing the document permissions and deleting the document  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


