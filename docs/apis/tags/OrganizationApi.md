<a id="__pageTop"></a>
# flat_api.apis.tags.organization_api.OrganizationApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_orga_users**](#count_orga_users) | **get** /organizations/users/count | Count the organization users using the provided filters
[**create_lti_credentials**](#create_lti_credentials) | **post** /organizations/lti/credentials | Create a new couple of LTI 1.x credentials
[**create_organization_invitation**](#create_organization_invitation) | **post** /organizations/invitations | Create a new invitation to join the organization
[**create_organization_user**](#create_organization_user) | **post** /organizations/users | Create a new user account
[**create_organization_user_access_token**](#create_organization_user_access_token) | **post** /organizations/users/{user}/accessToken | Create a delegated API access token for an organization user
[**create_organization_user_signin_link**](#create_organization_user_signin_link) | **post** /organizations/users/{user}/signinLink | Create a sign in link for an organization user
[**list_lti_credentials**](#list_lti_credentials) | **get** /organizations/lti/credentials | List LTI 1.x credentials
[**list_organization_invitations**](#list_organization_invitations) | **get** /organizations/invitations | List the organization invitations
[**list_organization_users**](#list_organization_users) | **get** /organizations/users | List the organization users
[**remove_organization_invitation**](#remove_organization_invitation) | **delete** /organizations/invitations/{invitation} | Remove an organization invitation
[**remove_organization_user**](#remove_organization_user) | **delete** /organizations/users/{user} | Remove an account from Flat
[**revoke_lti_credentials**](#revoke_lti_credentials) | **delete** /organizations/lti/credentials/{credentials} | Revoke LTI 1.x credentials
[**update_organization_user**](#update_organization_user) | **put** /organizations/users/{user} | Update account information

# **count_orga_users**
<a id="count_orga_users"></a>
> [UserDetailsAdmin] count_orga_users()

Count the organization users using the provided filters

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.user_details_admin import UserDetailsAdmin
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only optional values
    query_params = {
        'role': [
        "user"
    ],
        'q': "q_example",
        'group': [
        "group_example"
    ],
        'noActiveLicense': True,
    }
    try:
        # Count the organization users using the provided filters
        api_response = api_instance.count_orga_users(
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->count_orga_users: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
role | RoleSchema | | optional
q | QSchema | | optional
group | GroupSchema | | optional
noActiveLicense | NoActiveLicenseSchema | | optional


# RoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["user", "teacher", "admin", ] 

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# NoActiveLicenseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_orga_users.ApiResponseFor200) | Number of users
default | [ApiResponseForDefault](#count_orga_users.ApiResponseForDefault) | Error

#### count_orga_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UserDetailsAdmin**]({{complexTypePrefix}}UserDetailsAdmin.md) | [**UserDetailsAdmin**]({{complexTypePrefix}}UserDetailsAdmin.md) | [**UserDetailsAdmin**]({{complexTypePrefix}}UserDetailsAdmin.md) |  | 

#### count_orga_users.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_lti_credentials**
<a id="create_lti_credentials"></a>
> LtiCredentials create_lti_credentials(body)

Create a new couple of LTI 1.x credentials

Flat for Education is a Certified LTI Provider. You can use these API methods to automate the creation of LTI credentials. You can read more about our LTI implementation, supported components and LTI Endpoints in our [Developer Documentation](https://flat.io/developers/docs/lti/). 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.lti_credentials import LtiCredentials
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.lti_credentials_creation import LtiCredentialsCreation
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    body = LtiCredentialsCreation(
        name="name_example",
        lms=LmsName("canvas"),
    )
    try:
        # Create a new couple of LTI 1.x credentials
        api_response = api_instance.create_lti_credentials(
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->create_lti_credentials: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LtiCredentialsCreation**](../../models/LtiCredentialsCreation.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_lti_credentials.ApiResponseFor200) | The LTI Credentials
403 | [ApiResponseFor403](#create_lti_credentials.ApiResponseFor403) | Not admin of an organization
default | [ApiResponseForDefault](#create_lti_credentials.ApiResponseForDefault) | Error

#### create_lti_credentials.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LtiCredentials**](../../models/LtiCredentials.md) |  | 


#### create_lti_credentials.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_lti_credentials.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_organization_invitation**
<a id="create_organization_invitation"></a>
> OrganizationInvitation create_organization_invitation()

Create a new invitation to join the organization

This method creates and sends invitation for teachers and admins.  Invitations can only be used by new Flat users or users who are not part of the organization yet.  If the email of the user is already associated to a user of your organization, the API will simply update the role of the existing user and won't send an invitation. In this case, the property `usedBy` will be directly filled with the uniquer identifier of the corresponding user. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.organization_invitation_creation import OrganizationInvitationCreation
from flat_api.model.organization_invitation import OrganizationInvitation
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only optional values
    body = OrganizationInvitationCreation(
        email="email_example",
        organization_role=OrganizationRoles("admin"),
    )
    try:
        # Create a new invitation to join the organization
        api_response = api_instance.create_organization_invitation(
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->create_organization_invitation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationInvitationCreation**](../../models/OrganizationInvitationCreation.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_organization_invitation.ApiResponseFor200) | New invitation created
default | [ApiResponseForDefault](#create_organization_invitation.ApiResponseForDefault) | Error

#### create_organization_invitation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationInvitation**](../../models/OrganizationInvitation.md) |  | 


#### create_organization_invitation.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_organization_user**
<a id="create_organization_user"></a>
> UserDetailsAdmin create_organization_user()

Create a new user account

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.user_creation import UserCreation
from flat_api.model.user_details_admin import UserDetailsAdmin
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only optional values
    body = UserCreation(
        username="2",
        firstname="firstname_example",
        lastname="lastname_example",
        email="email_example",
        password="password_example",
        locale=FlatLocales("en"),
        role="user",
    )
    try:
        # Create a new user account
        api_response = api_instance.create_organization_user(
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->create_organization_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserCreation**](../../models/UserCreation.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_organization_user.ApiResponseFor200) | New user created
default | [ApiResponseForDefault](#create_organization_user.ApiResponseForDefault) | Error

#### create_organization_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserDetailsAdmin**](../../models/UserDetailsAdmin.md) |  | 


#### create_organization_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_organization_user_access_token**
<a id="create_organization_user_access_token"></a>
> ApiAccessToken create_organization_user_access_token(user)

Create a delegated API access token for an organization user

This operation will create an API access token for a chosen organization user. This token will be valid for a limited time and can be used to access the API as the organization user. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.organization_user_access_token_creation import OrganizationUserAccessTokenCreation
from flat_api.model.api_access_token import ApiAccessToken
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user': "user_example",
    }
    try:
        # Create a delegated API access token for an organization user
        api_response = api_instance.create_organization_user_access_token(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->create_organization_user_access_token: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user': "user_example",
    }
    body = OrganizationUserAccessTokenCreation(
        scopes=[
            AppScopes("account.public_profile")
        ],
    )
    try:
        # Create a delegated API access token for an organization user
        api_response = api_instance.create_organization_user_access_token(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->create_organization_user_access_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationUserAccessTokenCreation**](../../models/OrganizationUserAccessTokenCreation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user | UserSchema | | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_organization_user_access_token.ApiResponseFor200) | Created API access token
default | [ApiResponseForDefault](#create_organization_user_access_token.ApiResponseForDefault) | Error

#### create_organization_user_access_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiAccessToken**](../../models/ApiAccessToken.md) |  | 


#### create_organization_user_access_token.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_organization_user_signin_link**
<a id="create_organization_user_signin_link"></a>
> UserSigninLink create_organization_user_signin_link(user)

Create a sign in link for an organization user

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.user_signin_link_creation import UserSigninLinkCreation
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.user_signin_link import UserSigninLink
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user': "user_example",
    }
    try:
        # Create a sign in link for an organization user
        api_response = api_instance.create_organization_user_signin_link(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->create_organization_user_signin_link: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user': "user_example",
    }
    body = UserSigninLinkCreation(
        destination_path="/",
    )
    try:
        # Create a sign in link for an organization user
        api_response = api_instance.create_organization_user_signin_link(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->create_organization_user_signin_link: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserSigninLinkCreation**](../../models/UserSigninLinkCreation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user | UserSchema | | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_organization_user_signin_link.ApiResponseFor200) | Sign in link
default | [ApiResponseForDefault](#create_organization_user_signin_link.ApiResponseForDefault) | Error

#### create_organization_user_signin_link.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserSigninLink**](../../models/UserSigninLink.md) |  | 


#### create_organization_user_signin_link.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_lti_credentials**
<a id="list_lti_credentials"></a>
> [LtiCredentials] list_lti_credentials()

List LTI 1.x credentials

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.lti_credentials import LtiCredentials
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List LTI 1.x credentials
        api_response = api_instance.list_lti_credentials()
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->list_lti_credentials: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_lti_credentials.ApiResponseFor200) | The list of LTI Credentials
403 | [ApiResponseFor403](#list_lti_credentials.ApiResponseFor403) | Not admin of an organization
default | [ApiResponseForDefault](#list_lti_credentials.ApiResponseForDefault) | Error

#### list_lti_credentials.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LtiCredentials**]({{complexTypePrefix}}LtiCredentials.md) | [**LtiCredentials**]({{complexTypePrefix}}LtiCredentials.md) | [**LtiCredentials**]({{complexTypePrefix}}LtiCredentials.md) |  | 

#### list_lti_credentials.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### list_lti_credentials.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_organization_invitations**
<a id="list_organization_invitations"></a>
> [OrganizationInvitation] list_organization_invitations()

List the organization invitations

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.organization_invitation import OrganizationInvitation
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only optional values
    query_params = {
        'role': "user",
        'limit': 50,
        'next': "next_example",
        'previous': "previous_example",
    }
    try:
        # List the organization invitations
        api_response = api_instance.list_organization_invitations(
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->list_organization_invitations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
role | RoleSchema | | optional
limit | LimitSchema | | optional
next | NextSchema | | optional
previous | PreviousSchema | | optional


# RoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["user", "teacher", "admin", ] 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50

# NextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PreviousSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_organization_invitations.ApiResponseFor200) | List of invitations
default | [ApiResponseForDefault](#list_organization_invitations.ApiResponseForDefault) | Error

#### list_organization_invitations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrganizationInvitation**]({{complexTypePrefix}}OrganizationInvitation.md) | [**OrganizationInvitation**]({{complexTypePrefix}}OrganizationInvitation.md) | [**OrganizationInvitation**]({{complexTypePrefix}}OrganizationInvitation.md) |  | 

#### list_organization_invitations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_organization_users**
<a id="list_organization_users"></a>
> [UserDetailsAdmin] list_organization_users()

List the organization users

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.user_details_admin import UserDetailsAdmin
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only optional values
    query_params = {
        'sort': [
        "firstname"
    ],
        'direction': "asc",
        'next': "next_example",
        'previous': "previous_example",
        'role': [
        "user"
    ],
        'q': "q_example",
        'group': [
        "group_example"
    ],
        'noActiveLicense': True,
        'licenseExpirationDate': [
        "licenseExpirationDate_example"
    ],
        'onlyIds': True,
        'limit': 25,
    }
    try:
        # List the organization users
        api_response = api_instance.list_organization_users(
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->list_organization_users: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sort | SortSchema | | optional
direction | DirectionSchema | | optional
next | NextSchema | | optional
previous | PreviousSchema | | optional
role | RoleSchema | | optional
q | QSchema | | optional
group | GroupSchema | | optional
noActiveLicense | NoActiveLicenseSchema | | optional
licenseExpirationDate | LicenseExpirationDateSchema | | optional
onlyIds | OnlyIdsSchema | | optional
limit | LimitSchema | | optional


# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["firstname", "lastname", "lastActivityDate", "licenseExpirationDate", ] 

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# NextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PreviousSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["user", "teacher", "admin", ] 

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# NoActiveLicenseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LicenseExpirationDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# OnlyIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 25

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_organization_users.ApiResponseFor200) | List of users
default | [ApiResponseForDefault](#list_organization_users.ApiResponseForDefault) | Error

#### list_organization_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UserDetailsAdmin**]({{complexTypePrefix}}UserDetailsAdmin.md) | [**UserDetailsAdmin**]({{complexTypePrefix}}UserDetailsAdmin.md) | [**UserDetailsAdmin**]({{complexTypePrefix}}UserDetailsAdmin.md) |  | 

#### list_organization_users.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_organization_invitation**
<a id="remove_organization_invitation"></a>
> remove_organization_invitation(invitation)

Remove an organization invitation

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'invitation': "invitation_example",
    }
    try:
        # Remove an organization invitation
        api_response = api_instance.remove_organization_invitation(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->remove_organization_invitation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
invitation | InvitationSchema | | 

# InvitationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_organization_invitation.ApiResponseFor204) | The invitation has been removed
default | [ApiResponseForDefault](#remove_organization_invitation.ApiResponseForDefault) | Error

#### remove_organization_invitation.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_organization_invitation.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_organization_user**
<a id="remove_organization_user"></a>
> remove_organization_user(user)

Remove an account from Flat

This operation removes an account from Flat and its data, including: * The music scores created by this user (documents, history, comments, collaboration information) * Education related data (assignments and classroom information) 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user': "user_example",
    }
    query_params = {
    }
    try:
        # Remove an account from Flat
        api_response = api_instance.remove_organization_user(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->remove_organization_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user': "user_example",
    }
    query_params = {
        'convertToIndividual': True,
    }
    try:
        # Remove an account from Flat
        api_response = api_instance.remove_organization_user(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->remove_organization_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
convertToIndividual | ConvertToIndividualSchema | | optional


# ConvertToIndividualSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user | UserSchema | | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_organization_user.ApiResponseFor204) | User deleted
default | [ApiResponseForDefault](#remove_organization_user.ApiResponseForDefault) | Error

#### remove_organization_user.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_organization_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **revoke_lti_credentials**
<a id="revoke_lti_credentials"></a>
> revoke_lti_credentials(credentials)

Revoke LTI 1.x credentials

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.flat_error_response import FlatErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'credentials': "credentials_example",
    }
    try:
        # Revoke LTI 1.x credentials
        api_response = api_instance.revoke_lti_credentials(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->revoke_lti_credentials: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
credentials | CredentialsSchema | | 

# CredentialsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#revoke_lti_credentials.ApiResponseFor204) | Credentials revoked
403 | [ApiResponseFor403](#revoke_lti_credentials.ApiResponseFor403) | Not admin of an organization
404 | [ApiResponseFor404](#revoke_lti_credentials.ApiResponseFor404) | Credentials not found
default | [ApiResponseForDefault](#revoke_lti_credentials.ApiResponseForDefault) | Error

#### revoke_lti_credentials.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### revoke_lti_credentials.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### revoke_lti_credentials.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### revoke_lti_credentials.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_organization_user**
<a id="update_organization_user"></a>
> UserDetailsAdmin update_organization_user(userbody)

Update account information

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import organization_api
from flat_api.model.user_details_admin import UserDetailsAdmin
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.user_admin_update import UserAdminUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_api.OrganizationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user': "user_example",
    }
    body = UserAdminUpdate(
        password="password_example",
        organization_role=OrganizationRoles("admin"),
        username="2",
        firstname="firstname_example",
        lastname="lastname_example",
        email="email_example",
    )
    try:
        # Update account information
        api_response = api_instance.update_organization_user(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling OrganizationApi->update_organization_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserAdminUpdate**](../../models/UserAdminUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user | UserSchema | | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_organization_user.ApiResponseFor200) | User updated
default | [ApiResponseForDefault](#update_organization_user.ApiResponseForDefault) | Error

#### update_organization_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserDetailsAdmin**](../../models/UserDetailsAdmin.md) |  | 


#### update_organization_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

