<a id="__pageTop"></a>
# flat_api.apis.tags.score_api.ScoreApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_score_collaborator**](#add_score_collaborator) | **post** /scores/{score}/collaborators | Add a new collaborator
[**add_score_track**](#add_score_track) | **post** /scores/{score}/tracks | Add a new video or audio track to the score
[**create_export_task**](#create_export_task) | **post** /scores/{score}/revisions/{revision}/{format}/task | Create a new score export task
[**create_score**](#create_score) | **post** /scores | Create a new score
[**create_score_revision**](#create_score_revision) | **post** /scores/{score}/revisions | Create a new revision
[**delete_score**](#delete_score) | **delete** /scores/{score} | Delete a score
[**delete_score_comment**](#delete_score_comment) | **delete** /scores/{score}/comments/{comment} | Delete a comment
[**delete_score_track**](#delete_score_track) | **delete** /scores/{score}/tracks/{track} | Remove an audio or video track linked to the score
[**edit_score**](#edit_score) | **put** /scores/{score} | Edit a score&#x27;s metadata
[**fork_score**](#fork_score) | **post** /scores/{score}/fork | Fork a score
[**ger_user_likes**](#ger_user_likes) | **get** /users/{user}/likes | List liked scores
[**get_group_scores**](#get_group_scores) | **get** /groups/{group}/scores | List group&#x27;s scores
[**get_score**](#get_score) | **get** /scores/{score} | Get a score&#x27;s metadata
[**get_score_collaborator**](#get_score_collaborator) | **get** /scores/{score}/collaborators/{collaborator} | Get a collaborator
[**get_score_collaborators**](#get_score_collaborators) | **get** /scores/{score}/collaborators | List the collaborators
[**get_score_comments**](#get_score_comments) | **get** /scores/{score}/comments | List comments
[**get_score_revision**](#get_score_revision) | **get** /scores/{score}/revisions/{revision} | Get a score revision
[**get_score_revision_data**](#get_score_revision_data) | **get** /scores/{score}/revisions/{revision}/{format} | Get a score revision data
[**get_score_revisions**](#get_score_revisions) | **get** /scores/{score}/revisions | List the revisions
[**get_score_submissions**](#get_score_submissions) | **get** /scores/{score}/submissions | List submissions related to the score
[**get_score_track**](#get_score_track) | **get** /scores/{score}/tracks/{track} | Retrieve the details of an audio or video track linked to a score
[**get_user_scores**](#get_user_scores) | **get** /users/{user}/scores | List user&#x27;s scores
[**list_score_tracks**](#list_score_tracks) | **get** /scores/{score}/tracks | List the audio or video tracks linked to a score
[**mark_score_comment_resolved**](#mark_score_comment_resolved) | **put** /scores/{score}/comments/{comment}/resolved | Mark the comment as resolved
[**mark_score_comment_unresolved**](#mark_score_comment_unresolved) | **delete** /scores/{score}/comments/{comment}/resolved | Mark the comment as unresolved
[**post_score_comment**](#post_score_comment) | **post** /scores/{score}/comments | Post a new comment
[**remove_score_collaborator**](#remove_score_collaborator) | **delete** /scores/{score}/collaborators/{collaborator} | Delete a collaborator
[**untrash_score**](#untrash_score) | **post** /scores/{score}/untrash | Untrash a score
[**update_score_comment**](#update_score_comment) | **put** /scores/{score}/comments/{comment} | Update an existing comment
[**update_score_track**](#update_score_track) | **put** /scores/{score}/tracks/{track} | Update an audio or video track linked to a score

# **add_score_collaborator**
<a id="add_score_collaborator"></a>
> ResourceCollaborator add_score_collaborator(scorebody)

Add a new collaborator

Share a score with a single user or a group. This API call allows to add, invite and update the collaborators of a resource. - To add an existing Flat user to the resource, specify its unique identifier in the `user` property. - To invite an external user to the resource, specify its email in the `userEmail` property. - To add a Flat group to the resource, specify its unique identifier in the `group` property. - To update an existing collaborator, process the same request with different rights. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.resource_collaborator import ResourceCollaborator
from flat_api.model.resource_collaborator_creation import ResourceCollaboratorCreation
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    body = ResourceCollaboratorCreation(
        user="user_example",
        group="group_example",
        user_email="user_email_example",
        user_token="user_token_example",
        acl_read=True,
        acl_write=False,
        acl_admin=False,
    )
    try:
        # Add a new collaborator
        api_response = api_instance.add_score_collaborator(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->add_score_collaborator: %s\n" % e)
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
[**ResourceCollaboratorCreation**](../../models/ResourceCollaboratorCreation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_score_collaborator.ApiResponseFor200) | The newly added collaborator metadata
402 | [ApiResponseFor402](#add_score_collaborator.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#add_score_collaborator.ApiResponseFor403) | Not granted to manage this score
404 | [ApiResponseFor404](#add_score_collaborator.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#add_score_collaborator.ApiResponseForDefault) | Error

#### add_score_collaborator.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceCollaborator**](../../models/ResourceCollaborator.md) |  | 


#### add_score_collaborator.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### add_score_collaborator.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### add_score_collaborator.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### add_score_collaborator.ApiResponseForDefault
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

# **add_score_track**
<a id="add_score_track"></a>
> ScoreTrack add_score_track(scorebody)

Add a new video or audio track to the score

Use this method to add new track to the score. This track can then be played on flat.io or in an embedded score. This API method support medias hosted on SoundCloud, YouTube and Vimeo. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_track import ScoreTrack
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.score_track_creation import ScoreTrackCreation
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    body = ScoreTrackCreation(
        title="title_example",
        default=True,
        state=ScoreTrackState("draft"),
        url="url_example",
        synchronization_points=[
            ScoreTrackPoint(
                type="measure",
                measure_uuid="measure_uuid_example",
                time=3.14,
            )
        ],
    )
    try:
        # Add a new video or audio track to the score
        api_response = api_instance.add_score_track(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->add_score_track: %s\n" % e)
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
[**ScoreTrackCreation**](../../models/ScoreTrackCreation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_score_track.ApiResponseFor200) | Created track
403 | [ApiResponseFor403](#add_score_track.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#add_score_track.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#add_score_track.ApiResponseForDefault) | Error

#### add_score_track.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreTrack**](../../models/ScoreTrack.md) |  | 


#### add_score_track.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### add_score_track.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### add_score_track.ApiResponseForDefault
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

# **create_export_task**
<a id="create_export_task"></a>
> Task create_export_task(scorerevisionformat)

Create a new score export task

Some of the exports of a score takes are longer to process than a simple API requests. Use this endpoint to launch a new export of one score hosted on Flat. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.task_export_options import TaskExportOptions
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.task import Task
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'revision': "revision_example",
        'format': "mp3",
    }
    query_params = {
    }
    try:
        # Create a new score export task
        api_response = api_instance.create_export_task(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->create_export_task: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'revision': "revision_example",
        'format': "mp3",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    body = TaskExportOptions(
        parts=[
            "parts_example"
        ],
    )
    try:
        # Create a new score export task
        api_response = api_instance.create_export_task(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->create_export_task: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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
[**TaskExportOptions**](../../models/TaskExportOptions.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
revision | RevisionSchema | | 
format | FormatSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RevisionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["mp3", "wav", "practicefirst", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_export_task.ApiResponseFor200) | Task associated to the generation of the file
402 | [ApiResponseFor402](#create_export_task.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#create_export_task.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#create_export_task.ApiResponseFor404) | Score or associated file not found
default | [ApiResponseForDefault](#create_export_task.ApiResponseForDefault) | Error

#### create_export_task.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Task**](../../models/Task.md) |  | 


#### create_export_task.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_export_task.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_export_task.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_export_task.ApiResponseForDefault
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

# **create_score**
<a id="create_score"></a>
> ScoreDetails create_score(body)

Create a new score

Use this API method to **create a new music score in the current User account**. This API endpoints provides 3 ways to create scores:  * `ScoreCreationBuilderData` : Create a blank score by providing the list of instruments to use. You can optionally customize the initial key signature, time signature, enable TABs, Chord grids, as well as the page layout. * `ScoreCreationFileImport`: Import an existing MusicXML 3 file (`vnd.recordare.musicxml` or `vnd.recordare.musicxml+xml`), a MIDI file (`audio/midi`), Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar, or MuseScore file to create the new Flat document. * `ScoreCreationGoogleDriveImport`: Import an existing Google Drive file from the connected Google Drive account.  This API call will automatically create the first revision of the document, the score can be modified by the using our web application or by uploading a new revision of this file (`POST /v2/scores/{score}/revisions/{revision}`).  The currently authenticated user will be granted owner of the file and will be able to add other collaborators (users and groups).  If no `collection` is specified, the API will create the score in the most appropriate collection. When using an OAuth2 access token or a personal token, the score will be automatically added to your dedicated app collection in the account (`/v2/collections/app`).  If a `collection` is specified and this one has more public privacy settings than the score (e.g. `public` vs `private` for the score), the privacy settings of the created score will be adjusted to the collection ones.  You can check the adjusted privacy settings in the returned score `privacy`, and optionally adjust these settings if needed using `PUT /scores/{score}`. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_creation import ScoreCreation
from flat_api.model.score_details import ScoreDetails
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    body = ScoreCreation(
        title="title_example",
        privacy=ScorePrivacy("private"),
        collection="collection_example",
        google_drive_folder="google_drive_folder_example",
        builder_data=dict(
            score_data=dict(
                use_tab_staff=True,
                use_chord_grid=True,
                fifths=3.14,
                nb_beats=3.14,
                beat_type=3.14,
                instruments=[
                    dict(
                        group="group_example",
                        instrument="instrument_example",
                        long_name="long_name_example",
                        short_name="short_name_example",
                        has_quarter_tone=True,
                    )
                ],
            ),
            layout_data=dict(
                notes_spacing_coeff=3.14,
                length_unit="cm",
                page_height=3.14,
                page_width=3.14,
                page_margin_top=3.14,
                page_margin_bottom=3.14,
                page_margin_left=3.14,
                page_margin_right=3.14,
            ),
        ),
        filename="filename_example",
        data="data_example",
        data_encoding="base64",
        source=ScoreSource(
            google_drive="google_drive_example",
        ),
    )
    try:
        # Create a new score
        api_response = api_instance.create_score(
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->create_score: %s\n" % e)
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
[**ScoreCreation**](../../models/ScoreCreation.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_score.ApiResponseFor200) | Score created
400 | [ApiResponseFor400](#create_score.ApiResponseFor400) | Bad score creation request
402 | [ApiResponseFor402](#create_score.ApiResponseFor402) | Account overquota
default | [ApiResponseForDefault](#create_score.ApiResponseForDefault) | Error

#### create_score.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreDetails**](../../models/ScoreDetails.md) |  | 


#### create_score.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_score.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_score.ApiResponseForDefault
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

# **create_score_revision**
<a id="create_score_revision"></a>
> ScoreRevision create_score_revision(scorebody)

Create a new revision

Update a score by uploading a new revision for this one. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_revision_creation import ScoreRevisionCreation
from flat_api.model.score_revision import ScoreRevision
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    body = ScoreRevisionCreation(
        data="<score-partwise version=\"3.0\"></score-partwise>",
        data_encoding="base64",
        autosave=True,
        description="description_example",
    )
    try:
        # Create a new revision
        api_response = api_instance.create_score_revision(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->create_score_revision: %s\n" % e)
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
[**ScoreRevisionCreation**](../../models/ScoreRevisionCreation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_score_revision.ApiResponseFor200) | The new created revision metadata
402 | [ApiResponseFor402](#create_score_revision.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#create_score_revision.ApiResponseFor403) | Not granted to modify this score
404 | [ApiResponseFor404](#create_score_revision.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#create_score_revision.ApiResponseForDefault) | Error

#### create_score_revision.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreRevision**](../../models/ScoreRevision.md) |  | 


#### create_score_revision.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_score_revision.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_score_revision.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### create_score_revision.ApiResponseForDefault
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

# **delete_score**
<a id="delete_score"></a>
> delete_score(score)

Delete a score

This method can be used by the owner/admin (`aclAdmin` rights) of a score as well as regular collaborators.  When called by an owner/admin, it will schedule the deletion of the score, its revisions, and complete history. The score won't be accessible anymore after calling this method and the user's quota will directly be updated.  When called by a regular collaborator (`aclRead` / `aclWrite`), the score will be unshared (i.e. removed from the account & own collections). 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    query_params = {
    }
    try:
        # Delete a score
        api_response = api_instance.delete_score(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->delete_score: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    query_params = {
        'now': False,
    }
    try:
        # Delete a score
        api_response = api_instance.delete_score(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->delete_score: %s\n" % e)
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
now | NowSchema | | optional


# NowSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_score.ApiResponseFor204) | The score has been removed
403 | [ApiResponseFor403](#delete_score.ApiResponseFor403) | Not granted to manage this score
404 | [ApiResponseFor404](#delete_score.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#delete_score.ApiResponseForDefault) | Error

#### delete_score.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_score.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### delete_score.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### delete_score.ApiResponseForDefault
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

# **delete_score_comment**
<a id="delete_score_comment"></a>
> delete_score_comment(scorecomment)

Delete a comment

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'comment': "comment_example",
    }
    query_params = {
    }
    try:
        # Delete a comment
        api_response = api_instance.delete_score_comment(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->delete_score_comment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'comment': "comment_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # Delete a comment
        api_response = api_instance.delete_score_comment(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->delete_score_comment: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
comment | CommentSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CommentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_score_comment.ApiResponseFor204) | The comment has been deleted
403 | [ApiResponseFor403](#delete_score_comment.ApiResponseFor403) | Not granted to access to this score or not the original comment creator
404 | [ApiResponseFor404](#delete_score_comment.ApiResponseFor404) | Score or comment not found
default | [ApiResponseForDefault](#delete_score_comment.ApiResponseForDefault) | Error

#### delete_score_comment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_score_comment.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### delete_score_comment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### delete_score_comment.ApiResponseForDefault
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

# **delete_score_track**
<a id="delete_score_track"></a>
> delete_score_track(scoretrack)

Remove an audio or video track linked to the score

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'track': "track_example",
    }
    try:
        # Remove an audio or video track linked to the score
        api_response = api_instance.delete_score_track(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->delete_score_track: %s\n" % e)
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
score | ScoreSchema | | 
track | TrackSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TrackSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_score_track.ApiResponseFor204) | Track removed
403 | [ApiResponseFor403](#delete_score_track.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#delete_score_track.ApiResponseFor404) | Score or Track not found
default | [ApiResponseForDefault](#delete_score_track.ApiResponseForDefault) | Error

#### delete_score_track.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_score_track.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### delete_score_track.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### delete_score_track.ApiResponseForDefault
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

# **edit_score**
<a id="edit_score"></a>
> ScoreDetails edit_score(score)

Edit a score's metadata

This API method allows you to change the metadata of a score document (e.g. its `title` or `privacy`), all the properties are optional.  To edit the file itself, create a new revision using the appropriate method (`POST /v2/scores/{score}/revisions/{revision}`).  When editing the `title`, `subtitle`, `composer`, `lyricist`, `arranger` or `licenseText`, the metadatas will be instantly be updated, and a real-time action will be pushed to update the document lazily. This pending document modification will be automatically be saved as a new version by either a connected client or our internal versioning service. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_modification import ScoreModification
from flat_api.model.score_details import ScoreDetails
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    try:
        # Edit a score's metadata
        api_response = api_instance.edit_score(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->edit_score: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    body = ScoreModification(
        title="title_example",
        subtitle="subtitle_example",
        composer="composer_example",
        lyricist="lyricist_example",
        arranger="arranger_example",
        privacy=ScorePrivacy("private"),
        sharing_key="bf325375e030fccba00917317c574773100bf03b5fc61486286e564b23e9566b6ed19656dc3c5466a04c9eb07d770063ebd5468bf54d65309a8da56a8235f8f3",
        description="description_example",
        tags=[
            "tags_example"
        ],
        creation_type=ScoreCreationType("original"),
        license=ScoreLicense("copyright"),
        license_text="license_text_example",
    )
    try:
        # Edit a score's metadata
        api_response = api_instance.edit_score(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->edit_score: %s\n" % e)
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
[**ScoreModification**](../../models/ScoreModification.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_score.ApiResponseFor200) | Score details
402 | [ApiResponseFor402](#edit_score.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#edit_score.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#edit_score.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#edit_score.ApiResponseForDefault) | Error

#### edit_score.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreDetails**](../../models/ScoreDetails.md) |  | 


#### edit_score.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### edit_score.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### edit_score.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### edit_score.ApiResponseForDefault
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

# **fork_score**
<a id="fork_score"></a>
> ScoreDetails fork_score(scorebody)

Fork a score

This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to `private`.  When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_details import ScoreDetails
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.score_fork import ScoreFork
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    query_params = {
    }
    body = ScoreFork(
        collection="root",
        keep_original_title=True,
    )
    try:
        # Fork a score
        api_response = api_instance.fork_score(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->fork_score: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    body = ScoreFork(
        collection="root",
        keep_original_title=True,
    )
    try:
        # Fork a score
        api_response = api_instance.fork_score(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->fork_score: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
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
[**ScoreFork**](../../models/ScoreFork.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#fork_score.ApiResponseFor200) | Score details
402 | [ApiResponseFor402](#fork_score.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#fork_score.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#fork_score.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#fork_score.ApiResponseForDefault) | Error

#### fork_score.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreDetails**](../../models/ScoreDetails.md) |  | 


#### fork_score.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### fork_score.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### fork_score.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### fork_score.ApiResponseForDefault
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

# **ger_user_likes**
<a id="ger_user_likes"></a>
> [ScoreDetails] ger_user_likes(user)

List liked scores

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_details import ScoreDetails
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user': "user_example",
    }
    query_params = {
    }
    try:
        # List liked scores
        api_response = api_instance.ger_user_likes(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->ger_user_likes: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user': "user_example",
    }
    query_params = {
        'ids': True,
    }
    try:
        # List liked scores
        api_response = api_instance.ger_user_likes(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->ger_user_likes: %s\n" % e)
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
ids | IdsSchema | | optional


# IdsSchema

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
200 | [ApiResponseFor200](#ger_user_likes.ApiResponseFor200) | List of liked scores
default | [ApiResponseForDefault](#ger_user_likes.ApiResponseForDefault) | Error

#### ger_user_likes.ApiResponseFor200
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
[**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) | [**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) | [**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) |  | 

#### ger_user_likes.ApiResponseForDefault
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

# **get_group_scores**
<a id="get_group_scores"></a>
> [ScoreDetails] get_group_scores(group)

List group's scores

Get the list of scores shared with a group. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_details import ScoreDetails
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'group': "group_example",
    }
    query_params = {
    }
    try:
        # List group's scores
        api_response = api_instance.get_group_scores(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_group_scores: %s\n" % e)

    # example passing only optional values
    path_params = {
        'group': "group_example",
    }
    query_params = {
        'parent': "parent_example",
    }
    try:
        # List group's scores
        api_response = api_instance.get_group_scores(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_group_scores: %s\n" % e)
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
parent | ParentSchema | | optional


# ParentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
group | GroupSchema | | 

# GroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_group_scores.ApiResponseFor200) | The group&#x27;s scores
default | [ApiResponseForDefault](#get_group_scores.ApiResponseForDefault) | Error

#### get_group_scores.ApiResponseFor200
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
[**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) | [**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) | [**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) |  | 

#### get_group_scores.ApiResponseForDefault
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

# **get_score**
<a id="get_score"></a>
> ScoreDetails get_score(score)

Get a score's metadata

Get the details of a score identified by the `score` parameter in the URL. The currently authenticated user must have at least a read access to the document to use this API call. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_details import ScoreDetails
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    query_params = {
    }
    try:
        # Get a score's metadata
        api_response = api_instance.get_score(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # Get a score's metadata
        api_response = api_instance.get_score(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score.ApiResponseFor200) | Score details
402 | [ApiResponseFor402](#get_score.ApiResponseFor402) | Account overquota and this document is out of the granted quota
403 | [ApiResponseFor403](#get_score.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#get_score.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#get_score.ApiResponseForDefault) | Error

#### get_score.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreDetails**](../../models/ScoreDetails.md) |  | 


#### get_score.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score.ApiResponseForDefault
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

# **get_score_collaborator**
<a id="get_score_collaborator"></a>
> ResourceCollaborator get_score_collaborator(scorecollaborator)

Get a collaborator

Get the information about a collaborator (User or Group). 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.resource_collaborator import ResourceCollaborator
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'collaborator': "collaborator_example",
    }
    query_params = {
    }
    try:
        # Get a collaborator
        api_response = api_instance.get_score_collaborator(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_collaborator: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'collaborator': "collaborator_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # Get a collaborator
        api_response = api_instance.get_score_collaborator(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_collaborator: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
collaborator | CollaboratorSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CollaboratorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_collaborator.ApiResponseFor200) | Collaborator information
402 | [ApiResponseFor402](#get_score_collaborator.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#get_score_collaborator.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#get_score_collaborator.ApiResponseFor404) | Score or collaborator not found
default | [ApiResponseForDefault](#get_score_collaborator.ApiResponseForDefault) | Error

#### get_score_collaborator.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceCollaborator**](../../models/ResourceCollaborator.md) |  | 


#### get_score_collaborator.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_collaborator.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_collaborator.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_collaborator.ApiResponseForDefault
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

# **get_score_collaborators**
<a id="get_score_collaborators"></a>
> [ResourceCollaborator] get_score_collaborators(score)

List the collaborators

This API call will list the different collaborators of a score and their rights on the document. The returned list will at least contain the owner of the document.  Collaborators can be a single user (the object `user` will be populated) or a group (the object `group` will be populated). 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.resource_collaborator import ResourceCollaborator
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    query_params = {
    }
    try:
        # List the collaborators
        api_response = api_instance.get_score_collaborators(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_collaborators: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # List the collaborators
        api_response = api_instance.get_score_collaborators(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_collaborators: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_collaborators.ApiResponseFor200) | List of collaborators
402 | [ApiResponseFor402](#get_score_collaborators.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#get_score_collaborators.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#get_score_collaborators.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#get_score_collaborators.ApiResponseForDefault) | Error

#### get_score_collaborators.ApiResponseFor200
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
[**ResourceCollaborator**]({{complexTypePrefix}}ResourceCollaborator.md) | [**ResourceCollaborator**]({{complexTypePrefix}}ResourceCollaborator.md) | [**ResourceCollaborator**]({{complexTypePrefix}}ResourceCollaborator.md) |  | 

#### get_score_collaborators.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_collaborators.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_collaborators.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_collaborators.ApiResponseForDefault
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

# **get_score_comments**
<a id="get_score_comments"></a>
> [ScoreComment] get_score_comments(score)

List comments

This method lists the different comments added on a music score (documents and inline) sorted by their post dates.

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_comment import ScoreComment
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    query_params = {
    }
    try:
        # List comments
        api_response = api_instance.get_score_comments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_comments: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
        'type': "document",
        'sort': "date",
        'direction': "asc",
    }
    try:
        # List comments
        api_response = api_instance.get_score_comments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_comments: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional
type | TypeSchema | | optional
sort | SortSchema | | optional
direction | DirectionSchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["document", "inline", ] 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["date", ] 

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_comments.ApiResponseFor200) | The comments of the score
402 | [ApiResponseFor402](#get_score_comments.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#get_score_comments.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#get_score_comments.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#get_score_comments.ApiResponseForDefault) | Error

#### get_score_comments.ApiResponseFor200
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
[**ScoreComment**]({{complexTypePrefix}}ScoreComment.md) | [**ScoreComment**]({{complexTypePrefix}}ScoreComment.md) | [**ScoreComment**]({{complexTypePrefix}}ScoreComment.md) |  | 

#### get_score_comments.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_comments.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_comments.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_comments.ApiResponseForDefault
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

# **get_score_revision**
<a id="get_score_revision"></a>
> ScoreRevision get_score_revision(scorerevision)

Get a score revision

When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to get a specific revision metadata. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_revision import ScoreRevision
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'revision': "revision_example",
    }
    query_params = {
    }
    try:
        # Get a score revision
        api_response = api_instance.get_score_revision(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_revision: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'revision': "revision_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # Get a score revision
        api_response = api_instance.get_score_revision(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_revision: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
revision | RevisionSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RevisionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_revision.ApiResponseFor200) | Revision metadata
402 | [ApiResponseFor402](#get_score_revision.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#get_score_revision.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#get_score_revision.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#get_score_revision.ApiResponseForDefault) | Error

#### get_score_revision.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreRevision**](../../models/ScoreRevision.md) |  | 


#### get_score_revision.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revision.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revision.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revision.ApiResponseForDefault
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

# **get_score_revision_data**
<a id="get_score_revision_data"></a>
> file_type get_score_revision_data(scorerevisionformat)

Get a score revision data

Retrieve the file corresponding to a score revision (the following formats are available): Flat JSON/Adagio JSON `json`, MusicXML `mxl`/`xml`, MP3 `mp3`, WAV `wav`, MIDI `midi`, a tumbnail of the first page `thumbnail.png` or auto sync points `synchronizationPoints`. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'revision': "revision_example",
        'format': "json",
    }
    query_params = {
    }
    try:
        # Get a score revision data
        api_response = api_instance.get_score_revision_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_revision_data: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'revision': "revision_example",
        'format': "json",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
        'parts': "parts_example",
        'defaultTrack': True,
        'url': True,
    }
    try:
        # Get a score revision data
        api_response = api_instance.get_score_revision_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_revision_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/vnd.recordare.musicxml+xml', 'application/vnd.recordare.musicxml', 'audio/mp3', 'audio/wav', 'audio/midi', 'image/png', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sharingKey | SharingKeySchema | | optional
parts | PartsSchema | | optional
defaultTrack | DefaultTrackSchema | | optional
url | UrlSchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DefaultTrackSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# UrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
revision | RevisionSchema | | 
format | FormatSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RevisionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["json", "mxl", "xml", "mp3", "wav", "midi", "thumbnail.png", "synchronizationPoints", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_revision_data.ApiResponseFor200) | Revision data
402 | [ApiResponseFor402](#get_score_revision_data.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#get_score_revision_data.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#get_score_revision_data.ApiResponseFor404) | Score or associated file not found
default | [ApiResponseForDefault](#get_score_revision_data.ApiResponseForDefault) | Error

#### get_score_revision_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationVndRecordareMusicxmlxml, SchemaFor200ResponseBodyApplicationVndRecordareMusicxml, SchemaFor200ResponseBodyAudioMp3, SchemaFor200ResponseBodyAudioWav, SchemaFor200ResponseBodyAudioMidi, SchemaFor200ResponseBodyImagePng, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaFor200ResponseBodyApplicationVndRecordareMusicxmlxml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaFor200ResponseBodyApplicationVndRecordareMusicxml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaFor200ResponseBodyAudioMp3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaFor200ResponseBodyAudioWav

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaFor200ResponseBodyAudioMidi

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaFor200ResponseBodyImagePng

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### get_score_revision_data.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revision_data.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revision_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revision_data.ApiResponseForDefault
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

# **get_score_revisions**
<a id="get_score_revisions"></a>
> [ScoreRevision] get_score_revisions(score)

List the revisions

When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to list all of them, sorted by last modification.  Depending the plan of the account, this list can be trunked to the few last revisions. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_revision import ScoreRevision
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    query_params = {
    }
    try:
        # List the revisions
        api_response = api_instance.get_score_revisions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_revisions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # List the revisions
        api_response = api_instance.get_score_revisions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_revisions: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_revisions.ApiResponseFor200) | List of revisions
402 | [ApiResponseFor402](#get_score_revisions.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#get_score_revisions.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#get_score_revisions.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#get_score_revisions.ApiResponseForDefault) | Error

#### get_score_revisions.ApiResponseFor200
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
[**ScoreRevision**]({{complexTypePrefix}}ScoreRevision.md) | [**ScoreRevision**]({{complexTypePrefix}}ScoreRevision.md) | [**ScoreRevision**]({{complexTypePrefix}}ScoreRevision.md) |  | 

#### get_score_revisions.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revisions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revisions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_revisions.ApiResponseForDefault
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

# **get_score_submissions**
<a id="get_score_submissions"></a>
> [AssignmentSubmission] get_score_submissions(score)

List submissions related to the score

This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.assignment_submission import AssignmentSubmission
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    try:
        # List submissions related to the score
        api_response = api_instance.get_score_submissions(
            path_params=path_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_submissions: %s\n" % e)
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
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_submissions.ApiResponseFor200) | List of submissions
default | [ApiResponseForDefault](#get_score_submissions.ApiResponseForDefault) | Error

#### get_score_submissions.ApiResponseFor200
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
[**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) | [**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) | [**AssignmentSubmission**]({{complexTypePrefix}}AssignmentSubmission.md) |  | 

#### get_score_submissions.ApiResponseForDefault
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

# **get_score_track**
<a id="get_score_track"></a>
> ScoreTrack get_score_track(scoretrack)

Retrieve the details of an audio or video track linked to a score

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_track import ScoreTrack
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'track': "track_example",
    }
    query_params = {
    }
    try:
        # Retrieve the details of an audio or video track linked to a score
        api_response = api_instance.get_score_track(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_track: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'track': "track_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # Retrieve the details of an audio or video track linked to a score
        api_response = api_instance.get_score_track(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_score_track: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
track | TrackSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TrackSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_score_track.ApiResponseFor200) | Track details
403 | [ApiResponseFor403](#get_score_track.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#get_score_track.ApiResponseFor404) | Score or Track not found
default | [ApiResponseForDefault](#get_score_track.ApiResponseForDefault) | Error

#### get_score_track.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreTrack**](../../models/ScoreTrack.md) |  | 


#### get_score_track.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_track.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### get_score_track.ApiResponseForDefault
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

# **get_user_scores**
<a id="get_user_scores"></a>
> [ScoreDetails] get_user_scores(user)

List user's scores

Get the list of public scores owned by a User.  **DEPRECATED**: Please note that the current behavior will be deprecrated on **2019-01-01**. This method will no longer list private and shared scores, but only public scores of a Flat account. If you want to access to private scores, please use the [Collections API](#tag/Collection) instead. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_details import ScoreDetails
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user': "user_example",
    }
    query_params = {
    }
    try:
        # List user's scores
        api_response = api_instance.get_user_scores(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_user_scores: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user': "user_example",
    }
    query_params = {
        'parent': "parent_example",
    }
    try:
        # List user's scores
        api_response = api_instance.get_user_scores(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->get_user_scores: %s\n" % e)
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
parent | ParentSchema | | optional


# ParentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_user_scores.ApiResponseFor200) | The user scores
default | [ApiResponseForDefault](#get_user_scores.ApiResponseForDefault) | Error

#### get_user_scores.ApiResponseFor200
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
[**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) | [**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) | [**ScoreDetails**]({{complexTypePrefix}}ScoreDetails.md) |  | 

#### get_user_scores.ApiResponseForDefault
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

# **list_score_tracks**
<a id="list_score_tracks"></a>
> [ScoreTrack] list_score_tracks(score)

List the audio or video tracks linked to a score

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_track import ScoreTrack
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    query_params = {
    }
    try:
        # List the audio or video tracks linked to a score
        api_response = api_instance.list_score_tracks(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->list_score_tracks: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
        'assignment': "assignment_example",
        'listAutoTrack': True,
    }
    try:
        # List the audio or video tracks linked to a score
        api_response = api_instance.list_score_tracks(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->list_score_tracks: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional
assignment | AssignmentSchema | | optional
listAutoTrack | ListAutoTrackSchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssignmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ListAutoTrackSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_score_tracks.ApiResponseFor200) | List of tracks
403 | [ApiResponseFor403](#list_score_tracks.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#list_score_tracks.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#list_score_tracks.ApiResponseForDefault) | Error

#### list_score_tracks.ApiResponseFor200
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
[**ScoreTrack**]({{complexTypePrefix}}ScoreTrack.md) | [**ScoreTrack**]({{complexTypePrefix}}ScoreTrack.md) | [**ScoreTrack**]({{complexTypePrefix}}ScoreTrack.md) |  | 

#### list_score_tracks.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### list_score_tracks.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### list_score_tracks.ApiResponseForDefault
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

# **mark_score_comment_resolved**
<a id="mark_score_comment_resolved"></a>
> mark_score_comment_resolved(scorecomment)

Mark the comment as resolved

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'comment': "comment_example",
    }
    query_params = {
    }
    try:
        # Mark the comment as resolved
        api_response = api_instance.mark_score_comment_resolved(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->mark_score_comment_resolved: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'comment': "comment_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # Mark the comment as resolved
        api_response = api_instance.mark_score_comment_resolved(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->mark_score_comment_resolved: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
comment | CommentSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CommentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#mark_score_comment_resolved.ApiResponseFor204) | The comment has been marked as resolved
403 | [ApiResponseFor403](#mark_score_comment_resolved.ApiResponseFor403) | Not granted to mark this comment as resolved
404 | [ApiResponseFor404](#mark_score_comment_resolved.ApiResponseFor404) | Score or comment not found
default | [ApiResponseForDefault](#mark_score_comment_resolved.ApiResponseForDefault) | Error

#### mark_score_comment_resolved.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### mark_score_comment_resolved.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### mark_score_comment_resolved.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### mark_score_comment_resolved.ApiResponseForDefault
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

# **mark_score_comment_unresolved**
<a id="mark_score_comment_unresolved"></a>
> mark_score_comment_unresolved(scorecomment)

Mark the comment as unresolved

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'comment': "comment_example",
    }
    query_params = {
    }
    try:
        # Mark the comment as unresolved
        api_response = api_instance.mark_score_comment_unresolved(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->mark_score_comment_unresolved: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'comment': "comment_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    try:
        # Mark the comment as unresolved
        api_response = api_instance.mark_score_comment_unresolved(
            path_params=path_params,
            query_params=query_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->mark_score_comment_unresolved: %s\n" % e)
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
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
comment | CommentSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CommentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#mark_score_comment_unresolved.ApiResponseFor204) | The comment has been unmarked as resolved
403 | [ApiResponseFor403](#mark_score_comment_unresolved.ApiResponseFor403) | Not granted to unmark this comment as resolved
404 | [ApiResponseFor404](#mark_score_comment_unresolved.ApiResponseFor404) | Score or comment not found
default | [ApiResponseForDefault](#mark_score_comment_unresolved.ApiResponseForDefault) | Error

#### mark_score_comment_unresolved.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### mark_score_comment_unresolved.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### mark_score_comment_unresolved.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### mark_score_comment_unresolved.ApiResponseForDefault
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

# **post_score_comment**
<a id="post_score_comment"></a>
> ScoreComment post_score_comment(scorebody)

Post a new comment

Post a document or a contextualized comment on a document.  Please note that this method includes an anti-spam system for public scores. We don't guarantee that your comments will be accepted and displayed to end-user. Comments are be blocked by returning a `403` HTTP error and hidden from other users when the `spam` property is `true`. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_comment_creation import ScoreCommentCreation
from flat_api.model.score_comment import ScoreComment
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    query_params = {
    }
    body = ScoreCommentCreation(
        revision="revision_example",
        comment="comment_example",
        raw_comment="raw_comment_example",
        mentions=[
            "mentions_example"
        ],
        reply_to="reply_to_example",
        context=ScoreCommentContext(
            part_uuid="part_uuid_example",
            staff_idx=3.14,
            staff_uuid="staff_uuid_example",
            measure_uuids=[
                "measure_uuids_example"
            ],
            start_time_pos=3.14,
            stop_time_pos=3.14,
            start_dpq=3.14,
            stop_dpq=3.14,
        ),
    )
    try:
        # Post a new comment
        api_response = api_instance.post_score_comment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->post_score_comment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    body = ScoreCommentCreation(
        revision="revision_example",
        comment="comment_example",
        raw_comment="raw_comment_example",
        mentions=[
            "mentions_example"
        ],
        reply_to="reply_to_example",
        context=ScoreCommentContext(
            part_uuid="part_uuid_example",
            staff_idx=3.14,
            staff_uuid="staff_uuid_example",
            measure_uuids=[
                "measure_uuids_example"
            ],
            start_time_pos=3.14,
            stop_time_pos=3.14,
            start_dpq=3.14,
            stop_dpq=3.14,
        ),
    )
    try:
        # Post a new comment
        api_response = api_instance.post_score_comment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->post_score_comment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
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
[**ScoreCommentCreation**](../../models/ScoreCommentCreation.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_score_comment.ApiResponseFor200) | The new comment
402 | [ApiResponseFor402](#post_score_comment.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#post_score_comment.ApiResponseFor403) | Not granted to access to this score, to post a comment, or your API call triggered our spam filter.
404 | [ApiResponseFor404](#post_score_comment.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#post_score_comment.ApiResponseForDefault) | Error

#### post_score_comment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreComment**](../../models/ScoreComment.md) |  | 


#### post_score_comment.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### post_score_comment.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### post_score_comment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### post_score_comment.ApiResponseForDefault
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

# **remove_score_collaborator**
<a id="remove_score_collaborator"></a>
> remove_score_collaborator(scorecollaborator)

Delete a collaborator

Remove the specified collaborator from the score 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'collaborator': "collaborator_example",
    }
    try:
        # Delete a collaborator
        api_response = api_instance.remove_score_collaborator(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->remove_score_collaborator: %s\n" % e)
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
score | ScoreSchema | | 
collaborator | CollaboratorSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CollaboratorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_score_collaborator.ApiResponseFor204) | The collaborator has been removed
403 | [ApiResponseFor403](#remove_score_collaborator.ApiResponseFor403) | Not granted to manage this score
404 | [ApiResponseFor404](#remove_score_collaborator.ApiResponseFor404) | Score or collaborator not found
default | [ApiResponseForDefault](#remove_score_collaborator.ApiResponseForDefault) | Error

#### remove_score_collaborator.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_score_collaborator.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### remove_score_collaborator.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### remove_score_collaborator.ApiResponseForDefault
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

# **untrash_score**
<a id="untrash_score"></a>
> untrash_score(score)

Untrash a score

This method will remove the score from the `trash` collection and from the deletion queue, and add it back to the original collections. 

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
    }
    try:
        # Untrash a score
        api_response = api_instance.untrash_score(
            path_params=path_params,
        )
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->untrash_score: %s\n" % e)
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
score | ScoreSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#untrash_score.ApiResponseFor204) | The score has been untrashed
403 | [ApiResponseFor403](#untrash_score.ApiResponseFor403) | Not granted to manage this score
404 | [ApiResponseFor404](#untrash_score.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#untrash_score.ApiResponseForDefault) | Error

#### untrash_score.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### untrash_score.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### untrash_score.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### untrash_score.ApiResponseForDefault
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

# **update_score_comment**
<a id="update_score_comment"></a>
> ScoreComment update_score_comment(scorecommentbody)

Update an existing comment

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_comment import ScoreComment
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.score_comment_update import ScoreCommentUpdate
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'comment': "comment_example",
    }
    query_params = {
    }
    body = ScoreCommentUpdate(
        revision="revision_example",
        comment="comment_example",
        raw_comment="raw_comment_example",
        context=ScoreCommentContext(
            part_uuid="part_uuid_example",
            staff_idx=3.14,
            staff_uuid="staff_uuid_example",
            measure_uuids=[
                "measure_uuids_example"
            ],
            start_time_pos=3.14,
            stop_time_pos=3.14,
            start_dpq=3.14,
            stop_dpq=3.14,
        ),
    )
    try:
        # Update an existing comment
        api_response = api_instance.update_score_comment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->update_score_comment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'score': "score_example",
        'comment': "comment_example",
    }
    query_params = {
        'sharingKey': "sharingKey_example",
    }
    body = ScoreCommentUpdate(
        revision="revision_example",
        comment="comment_example",
        raw_comment="raw_comment_example",
        context=ScoreCommentContext(
            part_uuid="part_uuid_example",
            staff_idx=3.14,
            staff_uuid="staff_uuid_example",
            measure_uuids=[
                "measure_uuids_example"
            ],
            start_time_pos=3.14,
            stop_time_pos=3.14,
            start_dpq=3.14,
            stop_dpq=3.14,
        ),
    )
    try:
        # Update an existing comment
        api_response = api_instance.update_score_comment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->update_score_comment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
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
[**ScoreCommentUpdate**](../../models/ScoreCommentUpdate.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sharingKey | SharingKeySchema | | optional


# SharingKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
comment | CommentSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CommentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_score_comment.ApiResponseFor200) | The edited comment
402 | [ApiResponseFor402](#update_score_comment.ApiResponseFor402) | Account overquota
403 | [ApiResponseFor403](#update_score_comment.ApiResponseFor403) | Not granted to access to this score or not the original comment creator
404 | [ApiResponseFor404](#update_score_comment.ApiResponseFor404) | Score not found
default | [ApiResponseForDefault](#update_score_comment.ApiResponseForDefault) | Error

#### update_score_comment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreComment**](../../models/ScoreComment.md) |  | 


#### update_score_comment.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### update_score_comment.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### update_score_comment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### update_score_comment.ApiResponseForDefault
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

# **update_score_track**
<a id="update_score_track"></a>
> ScoreTrack update_score_track(scoretrackbody)

Update an audio or video track linked to a score

### Example

* OAuth Authentication (OAuth2):
```python
import flat_api
from flat_api.apis.tags import score_api
from flat_api.model.score_track import ScoreTrack
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.score_track_update import ScoreTrackUpdate
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
    api_instance = score_api.ScoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'score': "score_example",
        'track': "track_example",
    }
    body = ScoreTrackUpdate(
        title="title_example",
        default=True,
        state=ScoreTrackState("draft"),
        synchronization_points=[
            ScoreTrackPoint(
                type="measure",
                measure_uuid="measure_uuid_example",
                time=3.14,
            )
        ],
    )
    try:
        # Update an audio or video track linked to a score
        api_response = api_instance.update_score_track(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling ScoreApi->update_score_track: %s\n" % e)
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
[**ScoreTrackUpdate**](../../models/ScoreTrackUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
score | ScoreSchema | | 
track | TrackSchema | | 

# ScoreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TrackSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_score_track.ApiResponseFor200) | Updated track
403 | [ApiResponseFor403](#update_score_track.ApiResponseFor403) | Not granted to access to this score
404 | [ApiResponseFor404](#update_score_track.ApiResponseFor404) | Score or Track not found
default | [ApiResponseForDefault](#update_score_track.ApiResponseForDefault) | Error

#### update_score_track.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScoreTrack**](../../models/ScoreTrack.md) |  | 


#### update_score_track.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### update_score_track.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FlatErrorResponse**](../../models/FlatErrorResponse.md) |  | 


#### update_score_track.ApiResponseForDefault
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

