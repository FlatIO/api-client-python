# flat_api.ScoreApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_score_collaborator**](ScoreApi.md#add_score_collaborator) | **POST** /scores/{score}/collaborators | Add a new collaborator
[**add_score_track**](ScoreApi.md#add_score_track) | **POST** /scores/{score}/tracks | Add a new video or audio track to the score
[**create_export_task**](ScoreApi.md#create_export_task) | **POST** /scores/{score}/revisions/{revision}/{format}/task | Create a new score export task
[**create_score**](ScoreApi.md#create_score) | **POST** /scores | Create a new score
[**create_score_revision**](ScoreApi.md#create_score_revision) | **POST** /scores/{score}/revisions | Create a new revision
[**delete_score**](ScoreApi.md#delete_score) | **DELETE** /scores/{score} | Delete a score
[**delete_score_comment**](ScoreApi.md#delete_score_comment) | **DELETE** /scores/{score}/comments/{comment} | Delete a comment
[**delete_score_track**](ScoreApi.md#delete_score_track) | **DELETE** /scores/{score}/tracks/{track} | Remove an audio or video track linked to the score
[**edit_score**](ScoreApi.md#edit_score) | **PUT** /scores/{score} | Edit a score&#39;s metadata
[**fork_score**](ScoreApi.md#fork_score) | **POST** /scores/{score}/fork | Fork a score
[**get_group_scores**](ScoreApi.md#get_group_scores) | **GET** /groups/{group}/scores | List group&#39;s scores
[**get_score**](ScoreApi.md#get_score) | **GET** /scores/{score} | Get a score&#39;s metadata
[**get_score_collaborator**](ScoreApi.md#get_score_collaborator) | **GET** /scores/{score}/collaborators/{collaborator} | Get a collaborator
[**get_score_collaborators**](ScoreApi.md#get_score_collaborators) | **GET** /scores/{score}/collaborators | List the collaborators
[**get_score_comments**](ScoreApi.md#get_score_comments) | **GET** /scores/{score}/comments | List comments
[**get_score_revision**](ScoreApi.md#get_score_revision) | **GET** /scores/{score}/revisions/{revision} | Get a score revision
[**get_score_revision_data**](ScoreApi.md#get_score_revision_data) | **GET** /scores/{score}/revisions/{revision}/{format} | Get a score revision data
[**get_score_revisions**](ScoreApi.md#get_score_revisions) | **GET** /scores/{score}/revisions | List the revisions
[**get_score_submissions**](ScoreApi.md#get_score_submissions) | **GET** /scores/{score}/submissions | List submissions related to the score
[**get_score_track**](ScoreApi.md#get_score_track) | **GET** /scores/{score}/tracks/{track} | Retrieve the details of an audio or video track linked to a score
[**get_user_likes**](ScoreApi.md#get_user_likes) | **GET** /users/{user}/likes | List liked scores
[**get_user_scores**](ScoreApi.md#get_user_scores) | **GET** /users/{user}/scores | List user&#39;s scores
[**list_score_tracks**](ScoreApi.md#list_score_tracks) | **GET** /scores/{score}/tracks | List the audio or video tracks linked to a score
[**mark_score_comment_resolved**](ScoreApi.md#mark_score_comment_resolved) | **PUT** /scores/{score}/comments/{comment}/resolved | Mark the comment as resolved
[**mark_score_comment_unresolved**](ScoreApi.md#mark_score_comment_unresolved) | **DELETE** /scores/{score}/comments/{comment}/resolved | Mark the comment as unresolved
[**post_score_comment**](ScoreApi.md#post_score_comment) | **POST** /scores/{score}/comments | Post a new comment
[**remove_score_collaborator**](ScoreApi.md#remove_score_collaborator) | **DELETE** /scores/{score}/collaborators/{collaborator} | Delete a collaborator
[**untrash_score**](ScoreApi.md#untrash_score) | **POST** /scores/{score}/untrash | Untrash a score
[**update_score_comment**](ScoreApi.md#update_score_comment) | **PUT** /scores/{score}/comments/{comment} | Update an existing comment
[**update_score_track**](ScoreApi.md#update_score_track) | **PUT** /scores/{score}/tracks/{track} | Update an audio or video track linked to a score


# **add_score_collaborator**
> ResourceCollaborator add_score_collaborator(score, body)

Add a new collaborator

Share a score with a single user or a group. This API call allows to add, invite and update the collaborators of a resource.
- To add an existing Flat user to the resource, specify its unique identifier in the `user` property.
- To invite an external user to the resource, specify its email in the `userEmail` property.
- To add a Flat group to the resource, specify its unique identifier in the `group` property.
- To update an existing collaborator, process the same request with different rights.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.resource_collaborator import ResourceCollaborator
from flat_api.models.resource_collaborator_creation import ResourceCollaboratorCreation
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    body = flat_api.ResourceCollaboratorCreation() # ResourceCollaboratorCreation | 

    try:
        # Add a new collaborator
        api_response = api_instance.add_score_collaborator(score, body)
        print("The response of ScoreApi->add_score_collaborator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->add_score_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **body** | [**ResourceCollaboratorCreation**](ResourceCollaboratorCreation.md)|  | 

### Return type

[**ResourceCollaborator**](ResourceCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly added collaborator metadata |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to manage this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_score_track**
> ScoreTrackCreationResponse add_score_track(score, body)

Add a new video or audio track to the score

Use this method to add new track to the score. This track can then be played on flat.io or in an embedded score.
This API method support medias hosted on SoundCloud, YouTube and Vimeo.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_track_creation import ScoreTrackCreation
from flat_api.models.score_track_creation_response import ScoreTrackCreationResponse
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    body = flat_api.ScoreTrackCreation() # ScoreTrackCreation | 

    try:
        # Add a new video or audio track to the score
        api_response = api_instance.add_score_track(score, body)
        print("The response of ScoreApi->add_score_track:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->add_score_track: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **body** | [**ScoreTrackCreation**](ScoreTrackCreation.md)|  | 

### Return type

[**ScoreTrackCreationResponse**](ScoreTrackCreationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created track |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_export_task**
> Task create_export_task(score, revision, format, sharing_key=sharing_key, body=body)

Create a new score export task

Some of the exports of a score takes are longer to process than a simple API requests.
Use this endpoint to launch a new export of one score hosted on Flat.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.task import Task
from flat_api.models.task_export_options import TaskExportOptions
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    revision = 'revision_example' # str | Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created. 
    format = 'format_example' # str | The format of the file that will be generated or the target service name where the file will be exported
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)
    body = flat_api.TaskExportOptions() # TaskExportOptions |  (optional)

    try:
        # Create a new score export task
        api_response = api_instance.create_export_task(score, revision, format, sharing_key=sharing_key, body=body)
        print("The response of ScoreApi->create_export_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->create_export_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **revision** | **str**| Unique identifier of a score revision. You can use &#x60;last&#x60; to fetch the information related to the last version created.  | 
 **format** | **str**| The format of the file that will be generated or the target service name where the file will be exported | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 
 **body** | [**TaskExportOptions**](TaskExportOptions.md)|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task associated to the generation of the file |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score or associated file not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_score**
> ScoreDetails create_score(body)

Create a new score

Use this API method to **create a new music score in the current User account**. This API endpoints provides 3 ways to create scores:

* `ScoreCreationBuilderData` : Create a blank score by providing the list of instruments to use. You can optionally customize the initial key signature, time signature, enable TABs, Chord grids, as well as the page layout.
* `ScoreCreationFileImport`: Import a file to create the new Flat document.

  **Preferred formats**:
  * **MusicXML**: `.xml`, `.musicxml`, `.mxl` (compressed) — MIME: `vnd.recordare.musicxml+xml`, `vnd.recordare.musicxml`. This is the only format that preserves all notation data (articulations, dynamics, layout, etc.) with full round-trip support.
  * **MIDI**: `.mid`, `.midi` — MIME: `audio/midi`. Only preserves pitch, timing, and instrument data; notation details are lost.

  **Also supported** (converted to MusicXML on import, some notation details may be lost):
  * **Guitar Pro**: `.gp`, `.gp3`, `.gp4`, `.gp5`, `.gpx`, `.gtp`
  * **MuseScore**: `.mscz`, `.mscx`
  * **Finale**: `.musx`
  * **ABC notation**: `.abc` — MIME: `text/vnd.abc`
  * **PowerTab**: `.ptb`
  * **Capella**: `.cap`, `.capx`
  * **MEI**: `.mei`
  * **Overture**: `.ove`
  * **TablEdit**: `.tef`
  * **Band-in-a-Box**: `.mgu`, `.sgu`
  * **Karaoke MIDI**: `.kar`
  * **MuseData**: `.md`
  * **Score Writer**: `.scw`
  * **Bagpipe Music Writer**: `.bmw`, `.bww`
  * **Encore**: `.enc`

  **Scanned music** (requires `supportsTasks`, runs our music recognition and spends
  credits):
  * **PDF**: `.pdf`
  * **Images**: `.jpg`, `.png`, `.webp`, `.tiff`, `.gif`, `.avif`, `.heic`, `.heif`

  The file is identified by its own content, so its extension and any declared type do
  not have to match. **One file per request**: a multi-page PDF or a multi-frame TIFF is
  fine, but several separate images of the same score (a page photographed at a time)
  need `createOmrJob`, which takes many inputs in one job and bills them as a single
  document. Its live limits are served by `getOmrCapabilities`.
* `ScoreCreationGoogleDriveImport`: Import an existing Google Drive file from the connected Google Drive account.

This API call will automatically create the first revision of the document, the score can be modified by the using our web application or by uploading a new revision of this file (`POST /v2/scores/{score}/revisions/{revision}`).

The currently authenticated user will be granted owner of the file and will be able to add other collaborators (users and groups).

If no `collection` is specified, the API will create the score in the most appropriate collection. When using an OAuth2 access token or a personal token, the score will be automatically added to your dedicated app collection in the account (`/v2/collections/app`).

If a `collection` is specified and this one has more public privacy settings than the score (e.g. `public` vs `private` for the score), the privacy settings of the created score will be adjusted to the collection ones.

You can check the adjusted privacy settings in the returned score `privacy`, and optionally adjust these settings if needed using `PUT /scores/{score}`.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_creation import ScoreCreation
from flat_api.models.score_details import ScoreDetails
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    body = flat_api.ScoreCreation() # ScoreCreation | 

    try:
        # Create a new score
        api_response = api_instance.create_score(body)
        print("The response of ScoreApi->create_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->create_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScoreCreation**](ScoreCreation.md)|  | 

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Score created |  * x-flat-score-revision -  <br>  * x-flat-score-revision-date -  <br>  |
**202** | Score will be imported using an asynchronous task (the API client has set &#x60;supportsTasks&#x60; to true) |  -  |
**400** | Bad score creation request |  -  |
**402** | Account overquota or feature not included in plan |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_score_revision**
> ScoreRevision create_score_revision(score, body)

Create a new revision

Update a score by uploading a new revision for this one.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_revision import ScoreRevision
from flat_api.models.score_revision_creation import ScoreRevisionCreation
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    body = flat_api.ScoreRevisionCreation() # ScoreRevisionCreation | 

    try:
        # Create a new revision
        api_response = api_instance.create_score_revision(score, body)
        print("The response of ScoreApi->create_score_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->create_score_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **body** | [**ScoreRevisionCreation**](ScoreRevisionCreation.md)|  | 

### Return type

[**ScoreRevision**](ScoreRevision.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new created revision metadata |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to modify this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_score**
> delete_score(score, now=now)

Delete a score

This method can be used by anyone that has at least read access to the document:

- When called by an owner/admin, it will schedule the deletion of the score, its revisions, and complete history. The score won't be accessible anymore after calling this method and the user's quota will directly be updated.
- When called by a collaborator, the score will be unshared (i.e. removed from the account & own collections).
- When called by another user that has the score in its collections, the score will be removed from all the user collections.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    now = False # bool | If `true`, the score deletion will be scheduled to be done ASAP (optional) (default to False)

    try:
        # Delete a score
        api_instance.delete_score(score, now=now)
    except Exception as e:
        print("Exception when calling ScoreApi->delete_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **now** | **bool**| If &#x60;true&#x60;, the score deletion will be scheduled to be done ASAP | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The score has been removed |  -  |
**403** | Not granted to manage this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_score_comment**
> delete_score_comment(score, comment, event_properties=event_properties, sharing_key=sharing_key)

Delete a comment

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    comment = 'comment_example' # str | Unique identifier of a sheet music comment 
    event_properties = '{\"context\":\"discover\",\"screenLevel0\":\"home\",\"screenRoute\":\"/discover\"}' # str | Optional analytics properties merged into XP tracking for this request.  JSON-encoded string representing event properties. Example:  - `?eventProperties={\"context\":\"discover\",\"screenLevel0\":\"home\"}`  (optional)
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Delete a comment
        api_instance.delete_score_comment(score, comment, event_properties=event_properties, sharing_key=sharing_key)
    except Exception as e:
        print("Exception when calling ScoreApi->delete_score_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **comment** | **str**| Unique identifier of a sheet music comment  | 
 **event_properties** | **str**| Optional analytics properties merged into XP tracking for this request.  JSON-encoded string representing event properties. Example:  - &#x60;?eventProperties&#x3D;{\&quot;context\&quot;:\&quot;discover\&quot;,\&quot;screenLevel0\&quot;:\&quot;home\&quot;}&#x60;  | [optional] 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The comment has been deleted |  -  |
**403** | Not granted to access to this score or not the original comment creator |  -  |
**404** | Score or comment not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_score_track**
> delete_score_track(score, track)

Remove an audio or video track linked to the score

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    track = 'track_example' # str | Unique identifier of a score audio track 

    try:
        # Remove an audio or video track linked to the score
        api_instance.delete_score_track(score, track)
    except Exception as e:
        print("Exception when calling ScoreApi->delete_score_track: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **track** | **str**| Unique identifier of a score audio track  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Track removed |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score or Track not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_score**
> ScoreDetails edit_score(score, body)

Edit a score's metadata

This API method allows you to change the metadata of a score document (e.g. its `title` or `privacy`), all the properties are optional.

To edit the file itself, create a new revision using the appropriate method (`POST /v2/scores/{score}/revisions/{revision}`).

When editing the `title`, `subtitle`, `composer`, `lyricist`, `arranger` or `licenseText`, the metadatas will be instantly be updated, and a real-time action will be pushed to update the document lazily.
This pending document modification will be automatically be saved as a new version by either a connected client or our internal versioning service.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_details import ScoreDetails
from flat_api.models.score_modification import ScoreModification
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    body = flat_api.ScoreModification() # ScoreModification | 

    try:
        # Edit a score's metadata
        api_response = api_instance.edit_score(score, body)
        print("The response of ScoreApi->edit_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->edit_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **body** | [**ScoreModification**](ScoreModification.md)|  | 

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Score details |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fork_score**
> ScoreDetails fork_score(score, body, sharing_key=sharing_key)

Fork a score

This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to `private`.

When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_details import ScoreDetails
from flat_api.models.score_fork import ScoreFork
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    body = flat_api.ScoreFork() # ScoreFork | 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Fork a score
        api_response = api_instance.fork_score(score, body, sharing_key=sharing_key)
        print("The response of ScoreApi->fork_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->fork_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **body** | [**ScoreFork**](ScoreFork.md)|  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Score details |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_scores**
> List[ScoreDetails] get_group_scores(group, parent=parent)

List group's scores

Get the list of scores shared with a group.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_details import ScoreDetails
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    group = 'group_example' # str | Unique identifier of a Flat group 
    parent = 'parent_example' # str | Filter the score forked from the score id `parent` (optional)

    try:
        # List group's scores
        api_response = api_instance.get_group_scores(group, parent=parent)
        print("The response of ScoreApi->get_group_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_group_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 
 **parent** | **str**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] 

### Return type

[**List[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group&#39;s scores |  -  |
**404** | Not Found - Group not found or user not member of group |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score**
> ScoreDetails get_score(score, sharing_key=sharing_key)

Get a score's metadata

Get the details of a score identified by the `score` parameter in the URL.
The currently authenticated user must have at least a read access to the document to use this API call.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_details import ScoreDetails
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Get a score's metadata
        api_response = api_instance.get_score(score, sharing_key=sharing_key)
        print("The response of ScoreApi->get_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Score details |  -  |
**402** | Account overquota and this document is out of the granted quota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_collaborator**
> ResourceCollaborator get_score_collaborator(score, collaborator, sharing_key=sharing_key)

Get a collaborator

Get the information about a collaborator (User or Group).


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.resource_collaborator import ResourceCollaborator
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    collaborator = 'collaborator_example' # str | Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group** 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Get a collaborator
        api_response = api_instance.get_score_collaborator(score, collaborator, sharing_key=sharing_key)
        print("The response of ScoreApi->get_score_collaborator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **collaborator** | **str**| Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**ResourceCollaborator**](ResourceCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collaborator information |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score or collaborator not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_collaborators**
> List[ResourceCollaborator] get_score_collaborators(score, sharing_key=sharing_key)

List the collaborators

This API call will list the different collaborators of a score and their rights on the document. The returned list will at least contain the owner of the document.

Collaborators can be a single user (the object `user` will be populated) or a group (the object `group` will be populated).


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.resource_collaborator import ResourceCollaborator
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # List the collaborators
        api_response = api_instance.get_score_collaborators(score, sharing_key=sharing_key)
        print("The response of ScoreApi->get_score_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**List[ResourceCollaborator]**](ResourceCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of collaborators |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_comments**
> List[ScoreComment] get_score_comments(score, type=type, sort=sort, direction=direction, sharing_key=sharing_key)

List comments

This method lists the different comments added on a music score (documents and inline) sorted by their post dates.

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_comment import ScoreComment
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    type = 'type_example' # str | Filter the comments by type (optional)
    sort = 'sort_example' # str | Sort (optional)
    direction = 'direction_example' # str | Sort direction (optional)
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # List comments
        api_response = api_instance.get_score_comments(score, type=type, sort=sort, direction=direction, sharing_key=sharing_key)
        print("The response of ScoreApi->get_score_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **type** | **str**| Filter the comments by type | [optional] 
 **sort** | **str**| Sort | [optional] 
 **direction** | **str**| Sort direction | [optional] 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**List[ScoreComment]**](ScoreComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The comments of the score |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_revision**
> ScoreRevision get_score_revision(score, revision, sharing_key=sharing_key)

Get a score revision

When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to get a specific
revision metadata.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_revision import ScoreRevision
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    revision = 'revision_example' # str | Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created. 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Get a score revision
        api_response = api_instance.get_score_revision(score, revision, sharing_key=sharing_key)
        print("The response of ScoreApi->get_score_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **revision** | **str**| Unique identifier of a score revision. You can use &#x60;last&#x60; to fetch the information related to the last version created.  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**ScoreRevision**](ScoreRevision.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Revision metadata |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_revision_data**
> bytes get_score_revision_data(score, revision, format, sharing_key=sharing_key, parts=parts, default_track=default_track, url=url)

Get a score revision data

Retrieve the file corresponding to a score revision (the following formats are available): Flat JSON/Adagio JSON `json`, MusicXML
`mxl`/`xml`, ABC notation `abc`, MP3 `mp3`, WAV `wav`, MIDI `midi`, Flat `flat`, a tumbnail of the first page `thumbnail.png` or auto sync points `synchronizationPoints`.

ABC notation is a text format that cannot express everything a score
contains. Like MIDI, the export is lossy: notation ABC has no equivalent
for is approximated or dropped rather than failing the request.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    revision = 'revision_example' # str | Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created. 
    format = 'format_example' # str | The format of the file you will retrieve
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)
    parts = 'parts_example' # str | An optional a set of parts uuid to be exported. This parameter must be composed of parts uuids separated by commas. For example \"59df645f-bb1c-f1b4-b573-d2afc4491f94,34ef645f-1aef-f3bc-1564-34cca4492b87\".  (optional)
    default_track = True # bool | When `format` is `mp3`, this property is set to true and the score has a default `ScoreTrack` (mp3), this one will be returned instead of the playback file.  (optional)
    url = True # bool | Returns a json with the `url` in it instead of redirecting  (optional)

    try:
        # Get a score revision data
        api_response = api_instance.get_score_revision_data(score, revision, format, sharing_key=sharing_key, parts=parts, default_track=default_track, url=url)
        print("The response of ScoreApi->get_score_revision_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score_revision_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **revision** | **str**| Unique identifier of a score revision. You can use &#x60;last&#x60; to fetch the information related to the last version created.  | 
 **format** | **str**| The format of the file you will retrieve | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 
 **parts** | **str**| An optional a set of parts uuid to be exported. This parameter must be composed of parts uuids separated by commas. For example \&quot;59df645f-bb1c-f1b4-b573-d2afc4491f94,34ef645f-1aef-f3bc-1564-34cca4492b87\&quot;.  | [optional] 
 **default_track** | **bool**| When &#x60;format&#x60; is &#x60;mp3&#x60;, this property is set to true and the score has a default &#x60;ScoreTrack&#x60; (mp3), this one will be returned instead of the playback file.  | [optional] 
 **url** | **bool**| Returns a json with the &#x60;url&#x60; in it instead of redirecting  | [optional] 

### Return type

**bytes**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.recordare.musicxml+xml, application/vnd.recordare.musicxml, audio/mp3, audio/wav, audio/midi, image/png, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Revision data |  * x-flat-score-revision -  <br>  * x-flat-score-revision-date -  <br>  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score or associated file not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_revisions**
> List[ScoreRevision] get_score_revisions(score, sharing_key=sharing_key)

List the revisions

When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to list all of them, sorted by last modification.

Depending the plan of the account, this list can be trunked to the few last revisions.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_revision import ScoreRevision
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # List the revisions
        api_response = api_instance.get_score_revisions(score, sharing_key=sharing_key)
        print("The response of ScoreApi->get_score_revisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score_revisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**List[ScoreRevision]**](ScoreRevision.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of revisions |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_submissions**
> List[AssignmentSubmission] get_score_submissions(score)

List submissions related to the score

This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.assignment_submission import AssignmentSubmission
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 

    try:
        # List submissions related to the score
        api_response = api_instance.get_score_submissions(score)
        print("The response of ScoreApi->get_score_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 

### Return type

[**List[AssignmentSubmission]**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of submissions |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_track**
> ScoreTrack get_score_track(score, track, sharing_key=sharing_key)

Retrieve the details of an audio or video track linked to a score

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_track import ScoreTrack
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    track = 'track_example' # str | Unique identifier of a score audio track 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Retrieve the details of an audio or video track linked to a score
        api_response = api_instance.get_score_track(score, track, sharing_key=sharing_key)
        print("The response of ScoreApi->get_score_track:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_score_track: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **track** | **str**| Unique identifier of a score audio track  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**ScoreTrack**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Track details |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score or Track not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_likes**
> List[ScoreDetails] get_user_likes(user, next=next, previous=previous, limit=limit, ids=ids)

List liked scores

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_details import ScoreDetails
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    user = 'user_example' # str | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
    next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    limit = 25 # int | This is the maximum number of objects that may be returned (optional) (default to 25)
    ids = True # bool | Return only the identifiers of the scores (optional)

    try:
        # List liked scores
        api_response = api_instance.get_user_likes(user, next=next, previous=previous, limit=limit, ids=ids)
        print("The response of ScoreApi->get_user_likes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_user_likes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | 
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] [default to 25]
 **ids** | **bool**| Return only the identifiers of the scores | [optional] 

### Return type

[**List[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of liked scores |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_scores**
> List[ScoreDetails] get_user_scores(user, paginate=paginate, sort=sort, direction=direction, limit=limit, next=next, previous=previous)

List user's scores

Get the list of public scores owned by a User.
If you want to access to private scores, please use the [Collections API](#tag/Collection).
For example `GET /v2/collections/allScores/scores` to list all recently updated scores.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_details import ScoreDetails
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    user = 'user_example' # str | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
    paginate = False # bool | When set to `true`, the API will return a paginated result. When set to `false` or unset, the API will return all the scores. If this parameter is unset or false, then limit/sort/direction/next/previous will be ignored.  (optional) (default to False)
    sort = 'sort_example' # str | Sort (optional)
    direction = 'direction_example' # str | Sort direction (optional)
    limit = 25 # int | This is the maximum number of objects that may be returned (optional) (default to 25)
    next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)

    try:
        # List user's scores
        api_response = api_instance.get_user_scores(user, paginate=paginate, sort=sort, direction=direction, limit=limit, next=next, previous=previous)
        print("The response of ScoreApi->get_user_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->get_user_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | 
 **paginate** | **bool**| When set to &#x60;true&#x60;, the API will return a paginated result. When set to &#x60;false&#x60; or unset, the API will return all the scores. If this parameter is unset or false, then limit/sort/direction/next/previous will be ignored.  | [optional] [default to False]
 **sort** | **str**| Sort | [optional] 
 **direction** | **str**| Sort direction | [optional] 
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] [default to 25]
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 

### Return type

[**List[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user scores |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_score_tracks**
> List[ScoreTrack] list_score_tracks(score, sharing_key=sharing_key, assignment=assignment, list_auto_track=list_auto_track)

List the audio or video tracks linked to a score

List all audio or video tracks linked to a score.

**Access Control for Performance Submission Tracks:**

Tracks with `purpose: 'performanceSubmission'` are filtered based on user role:

* **Students**: Can only see their own performance submission tracks, plus all non-performance tracks
* **Teachers and score admins**: Can see all tracks from all students

The `assignment` query parameter can be used to filter tracks for a specific assignment, but the access control rules above still apply.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_track import ScoreTrack
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)
    assignment = 'assignment_example' # str | An assignment id with which all the tracks returned will be related to  (optional)
    list_auto_track = True # bool | If true, and if available, return last automatically synchronized Flat's mp3 export as an additional track  (optional)

    try:
        # List the audio or video tracks linked to a score
        api_response = api_instance.list_score_tracks(score, sharing_key=sharing_key, assignment=assignment, list_auto_track=list_auto_track)
        print("The response of ScoreApi->list_score_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->list_score_tracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 
 **assignment** | **str**| An assignment id with which all the tracks returned will be related to  | [optional] 
 **list_auto_track** | **bool**| If true, and if available, return last automatically synchronized Flat&#39;s mp3 export as an additional track  | [optional] 

### Return type

[**List[ScoreTrack]**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tracks |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_score_comment_resolved**
> mark_score_comment_resolved(score, comment, sharing_key=sharing_key)

Mark the comment as resolved

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    comment = 'comment_example' # str | Unique identifier of a sheet music comment 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Mark the comment as resolved
        api_instance.mark_score_comment_resolved(score, comment, sharing_key=sharing_key)
    except Exception as e:
        print("Exception when calling ScoreApi->mark_score_comment_resolved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **comment** | **str**| Unique identifier of a sheet music comment  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The comment has been marked as resolved |  -  |
**403** | Not granted to mark this comment as resolved |  -  |
**404** | Score or comment not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_score_comment_unresolved**
> mark_score_comment_unresolved(score, comment, sharing_key=sharing_key)

Mark the comment as unresolved

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    comment = 'comment_example' # str | Unique identifier of a sheet music comment 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Mark the comment as unresolved
        api_instance.mark_score_comment_unresolved(score, comment, sharing_key=sharing_key)
    except Exception as e:
        print("Exception when calling ScoreApi->mark_score_comment_unresolved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **comment** | **str**| Unique identifier of a sheet music comment  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The comment has been unmarked as resolved |  -  |
**403** | Not granted to unmark this comment as resolved |  -  |
**404** | Score or comment not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_score_comment**
> ScoreComment post_score_comment(score, body, sharing_key=sharing_key)

Post a new comment

Post a document or a contextualized comment on a document.

Please note that this method includes an anti-spam system for public scores. We don't guarantee that your comments will be accepted and displayed to end-user. Comments are be blocked by returning a `403` HTTP error and hidden from other users when the `spam` property is `true`.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_comment import ScoreComment
from flat_api.models.score_comment_creation import ScoreCommentCreation
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    body = flat_api.ScoreCommentCreation() # ScoreCommentCreation | 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Post a new comment
        api_response = api_instance.post_score_comment(score, body, sharing_key=sharing_key)
        print("The response of ScoreApi->post_score_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->post_score_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **body** | [**ScoreCommentCreation**](ScoreCommentCreation.md)|  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**ScoreComment**](ScoreComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new comment |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score, to post a comment, or your API call triggered our spam filter. |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_score_collaborator**
> remove_score_collaborator(score, collaborator, event_properties=event_properties)

Delete a collaborator

Remove the specified collaborator from the score


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    collaborator = 'collaborator_example' # str | Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group** 
    event_properties = '{\"context\":\"discover\",\"screenLevel0\":\"home\",\"screenRoute\":\"/discover\"}' # str | Optional analytics properties merged into XP tracking for this request.  JSON-encoded string representing event properties. Example:  - `?eventProperties={\"context\":\"discover\",\"screenLevel0\":\"home\"}`  (optional)

    try:
        # Delete a collaborator
        api_instance.remove_score_collaborator(score, collaborator, event_properties=event_properties)
    except Exception as e:
        print("Exception when calling ScoreApi->remove_score_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **collaborator** | **str**| Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  | 
 **event_properties** | **str**| Optional analytics properties merged into XP tracking for this request.  JSON-encoded string representing event properties. Example:  - &#x60;?eventProperties&#x3D;{\&quot;context\&quot;:\&quot;discover\&quot;,\&quot;screenLevel0\&quot;:\&quot;home\&quot;}&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The collaborator has been removed |  -  |
**403** | Not granted to manage this score |  -  |
**404** | Score or collaborator not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **untrash_score**
> untrash_score(score)

Untrash a score

This method will remove the score from the `trash` collection and from the deletion queue, and add it back to the original collections.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 

    try:
        # Untrash a score
        api_instance.untrash_score(score)
    except Exception as e:
        print("Exception when calling ScoreApi->untrash_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The score has been untrashed |  -  |
**403** | Not granted to manage this score |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_score_comment**
> ScoreComment update_score_comment(score, comment, body, sharing_key=sharing_key)

Update an existing comment

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_comment import ScoreComment
from flat_api.models.score_comment_update import ScoreCommentUpdate
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    comment = 'comment_example' # str | Unique identifier of a sheet music comment 
    body = flat_api.ScoreCommentUpdate() # ScoreCommentUpdate | 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Update an existing comment
        api_response = api_instance.update_score_comment(score, comment, body, sharing_key=sharing_key)
        print("The response of ScoreApi->update_score_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->update_score_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **comment** | **str**| Unique identifier of a sheet music comment  | 
 **body** | [**ScoreCommentUpdate**](ScoreCommentUpdate.md)|  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**ScoreComment**](ScoreComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The edited comment |  -  |
**402** | Account overquota |  -  |
**403** | Not granted to access to this score or not the original comment creator |  -  |
**404** | Score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_score_track**
> ScoreTrack update_score_track(score, track, body)

Update an audio or video track linked to a score

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.score_track import ScoreTrack
from flat_api.models.score_track_update import ScoreTrackUpdate
from flat_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flat_api.ScoreApi(api_client)
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    track = 'track_example' # str | Unique identifier of a score audio track 
    body = flat_api.ScoreTrackUpdate() # ScoreTrackUpdate | 

    try:
        # Update an audio or video track linked to a score
        api_response = api_instance.update_score_track(score, track, body)
        print("The response of ScoreApi->update_score_track:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoreApi->update_score_track: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **track** | **str**| Unique identifier of a score audio track  | 
 **body** | [**ScoreTrackUpdate**](ScoreTrackUpdate.md)|  | 

### Return type

[**ScoreTrack**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated track |  -  |
**403** | Not granted to access to this score |  -  |
**404** | Score or Track not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

