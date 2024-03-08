# OrganizationInvitation

Details of an invitation to join an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The invitation unique identifier | [optional] 
**creation_date** | **datetime** | The creation date of the invitation | [optional] 
**organization** | **str** | The unique identifier of the Organization owning this class | 
**organization_role** | [**OrganizationRoles**](OrganizationRoles.md) |  | 
**custom_code** | **str** | Enrollment code to use when joining this organization | 
**email** | **str** | The email address this invitation was sent to | [optional] 
**invited_by** | **str** | The unique identifier of the User who created this invitation | [optional] 
**allow_multiple_use** | **bool** | If true, the invitation can be used multiple times. If false, the invitation can only be used once.  | 
**used_by** | **List[str]** | List of users who used this invitation | [optional] 

## Example

```python
from flat_api.models.organization_invitation import OrganizationInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInvitation from a JSON string
organization_invitation_instance = OrganizationInvitation.from_json(json)
# print the JSON string representation of the object
print OrganizationInvitation.to_json()

# convert the object into a dict
organization_invitation_dict = organization_invitation_instance.to_dict()
# create an instance of OrganizationInvitation from a dict
organization_invitation_form_dict = organization_invitation.from_dict(organization_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


