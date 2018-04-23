# flat_api.OrganizationApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lti_credentials**](OrganizationApi.md#create_lti_credentials) | **POST** /organizations/lti/credentials | Create a new couple of LTI 1.x credentials
[**create_organization_invitation**](OrganizationApi.md#create_organization_invitation) | **POST** /organizations/invitations | Create a new invitation to join the organization
[**create_organization_user**](OrganizationApi.md#create_organization_user) | **POST** /organizations/users | Create a new user account
[**list_lti_credentials**](OrganizationApi.md#list_lti_credentials) | **GET** /organizations/lti/credentials | List LTI 1.x credentials
[**list_organization_invitations**](OrganizationApi.md#list_organization_invitations) | **GET** /organizations/invitations | List the organization invitations
[**list_organization_users**](OrganizationApi.md#list_organization_users) | **GET** /organizations/users | List the organization users
[**remove_organization_invitation**](OrganizationApi.md#remove_organization_invitation) | **DELETE** /organizations/invitations/{invitation} | Remove an organization invitation
[**remove_organization_user**](OrganizationApi.md#remove_organization_user) | **DELETE** /organizations/users/{user} | Remove an account from Flat
[**revoke_lti_credentials**](OrganizationApi.md#revoke_lti_credentials) | **DELETE** /organizations/lti/credentials/{credentials} | Revoke LTI 1.x credentials
[**update_organization_user**](OrganizationApi.md#update_organization_user) | **PUT** /organizations/users/{user} | Update account information


# **create_lti_credentials**
> LtiCredentials create_lti_credentials(body)

Create a new couple of LTI 1.x credentials

Flat for Education is a Certified LTI Provider. You can use these API methods to automate the creation of LTI credentials. You can read more about our LTI implementation, supported components and LTI Endpoints in our [Developer Documentation](https://flat.io/developers/docs/lti/). 

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
body = flat_api.LtiCredentialsCreation() # LtiCredentialsCreation | 

try:
    # Create a new couple of LTI 1.x credentials
    api_response = api_instance.create_lti_credentials(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_lti_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LtiCredentialsCreation**](LtiCredentialsCreation.md)|  | 

### Return type

[**LtiCredentials**](LtiCredentials.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_invitation**
> OrganizationInvitation create_organization_invitation(body=body)

Create a new invitation to join the organization

This method creates and sends invitation for teachers and admins.  Invitations can only be used by new Flat users or users who are not part of the organization yet.  If the email of the user is already associated to a user of your organization, the API will simply update the role of the existing user and won't send an invitation. In this case, the property `usedBy` will be directly filled with the uniquer identifier of the corresponding user. 

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
body = flat_api.OrganizationInvitationCreation() # OrganizationInvitationCreation |  (optional)

try:
    # Create a new invitation to join the organization
    api_response = api_instance.create_organization_invitation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_organization_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationInvitationCreation**](OrganizationInvitationCreation.md)|  | [optional] 

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_user**
> UserDetailsAdmin create_organization_user(body=body)

Create a new user account

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
body = flat_api.UserCreation() # UserCreation |  (optional)

try:
    # Create a new user account
    api_response = api_instance.create_organization_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_organization_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreation**](UserCreation.md)|  | [optional] 

### Return type

[**UserDetailsAdmin**](UserDetailsAdmin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lti_credentials**
> list[LtiCredentials] list_lti_credentials()

List LTI 1.x credentials

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))

try:
    # List LTI 1.x credentials
    api_response = api_instance.list_lti_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->list_lti_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LtiCredentials]**](LtiCredentials.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_invitations**
> list[OrganizationInvitation] list_organization_invitations(role=role, limit=limit, next=next, previous=previous)

List the organization invitations

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
role = 'role_example' # str | Filter users by role (optional)
limit = 50 # int | This is the maximum number of objects that may be returned (optional) (default to 50)
next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)

try:
    # List the organization invitations
    api_response = api_instance.list_organization_invitations(role=role, limit=limit, next=next, previous=previous)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->list_organization_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Filter users by role | [optional] 
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] [default to 50]
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 

### Return type

[**list[OrganizationInvitation]**](OrganizationInvitation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_users**
> list[UserDetailsAdmin] list_organization_users(role=role, limit=limit, next=next, previous=previous)

List the organization users

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
role = 'role_example' # str | Filter users by role (optional)
limit = 50 # int | This is the maximum number of objects that may be returned (optional) (default to 50)
next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)

try:
    # List the organization users
    api_response = api_instance.list_organization_users(role=role, limit=limit, next=next, previous=previous)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->list_organization_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Filter users by role | [optional] 
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] [default to 50]
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 

### Return type

[**list[UserDetailsAdmin]**](UserDetailsAdmin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_organization_invitation**
> remove_organization_invitation(invitation)

Remove an organization invitation

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
invitation = 'invitation_example' # str | Unique identifier of the invitation

try:
    # Remove an organization invitation
    api_instance.remove_organization_invitation(invitation)
except ApiException as e:
    print("Exception when calling OrganizationApi->remove_organization_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | **str**| Unique identifier of the invitation | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_organization_user**
> remove_organization_user(user, convert_to_individual=convert_to_individual)

Remove an account from Flat

This operation removes an account from Flat and its data, including: * The music scores created by this user (documents, history, comments, collaboration information) * Education related data (assignments and classroom information) 

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
user = 'user_example' # str | Unique identifier of the Flat account 
convert_to_individual = true # bool | If `true`, the account will be only removed from the organization and converted into an individual account on our public website, https://flat.io. This operation will remove the education-related data from the account. Before realizing this operation, you need to be sure that the user is at least 13 years old and that this one has read and agreed to the Individual Terms of Services of Flat available on https://flat.io/legal.  (optional)

try:
    # Remove an account from Flat
    api_instance.remove_organization_user(user, convert_to_individual=convert_to_individual)
except ApiException as e:
    print("Exception when calling OrganizationApi->remove_organization_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of the Flat account  | 
 **convert_to_individual** | **bool**| If &#x60;true&#x60;, the account will be only removed from the organization and converted into an individual account on our public website, https://flat.io. This operation will remove the education-related data from the account. Before realizing this operation, you need to be sure that the user is at least 13 years old and that this one has read and agreed to the Individual Terms of Services of Flat available on https://flat.io/legal.  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_lti_credentials**
> revoke_lti_credentials(credentials)

Revoke LTI 1.x credentials

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
credentials = 'credentials_example' # str | Credentials unique identifier 

try:
    # Revoke LTI 1.x credentials
    api_instance.revoke_lti_credentials(credentials)
except ApiException as e:
    print("Exception when calling OrganizationApi->revoke_lti_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | **str**| Credentials unique identifier  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_user**
> UserDetailsAdmin update_organization_user(user, body)

Update account information

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = flat_api.OrganizationApi(flat_api.ApiClient(configuration))
user = 'user_example' # str | Unique identifier of the Flat account 
body = flat_api.UserAdminUpdate() # UserAdminUpdate | 

try:
    # Update account information
    api_response = api_instance.update_organization_user(user, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->update_organization_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of the Flat account  | 
 **body** | [**UserAdminUpdate**](UserAdminUpdate.md)|  | 

### Return type

[**UserDetailsAdmin**](UserDetailsAdmin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

