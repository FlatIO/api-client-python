# ScoreCollaborator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the score permission | [optional] 
**score** | **str** | The unique identifier of the score | [optional] 
**user** | [**UserPublic**](UserPublic.md) |  | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**user_email** | **str** | If the collaborator is not a user of Flat yet, this field will contain his email.  | [optional] 
**acl_read** | **bool** | &#x60;True&#x60; if the related user can read the score. (probably true if the user has a permission on the document).  | [optional] [default to True]
**acl_write** | **bool** | &#x60;True&#x60; if the related user can modify the score.  | [optional] [default to False]
**acl_admin** | **bool** | &#x60;True&#x60; if the related user can can manage the current document, i.e. changing the document permissions and deleting the document  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


