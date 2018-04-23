# flat_api.ScoreApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_score_collaborator**](ScoreApi.md#add_score_collaborator) | **POST** /scores/{score}/collaborators | Add a new collaborator
[**add_score_track**](ScoreApi.md#add_score_track) | **POST** /scores/{score}/tracks | Add a new video or audio track to the score
[**create_score**](ScoreApi.md#create_score) | **POST** /scores | Create a new score
[**create_score_revision**](ScoreApi.md#create_score_revision) | **POST** /scores/{score}/revisions | Create a new revision
[**delete_score**](ScoreApi.md#delete_score) | **DELETE** /scores/{score} | Delete a score
[**delete_score_comment**](ScoreApi.md#delete_score_comment) | **DELETE** /scores/{score}/comments/{comment} | Delete a comment
[**delete_score_track**](ScoreApi.md#delete_score_track) | **DELETE** /scores/{score}/tracks/{track} | Remove an audio or video track linked to the score
[**edit_score**](ScoreApi.md#edit_score) | **PUT** /scores/{score} | Edit a score&#39;s metadata
[**fork_score**](ScoreApi.md#fork_score) | **POST** /scores/{score}/fork | Fork a score
[**ger_user_likes**](ScoreApi.md#ger_user_likes) | **GET** /users/{user}/likes | List liked scores
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

Share a score with a single user or a group. This API call allows to add, invite and update the collaborators of a resource. - To add an existing Flat user to the resource, specify its unique identifier in the `user` property. - To invite an external user to the resource, specify its email in the `userEmail` property. - To add a Flat group to the resource, specify its unique identifier in the `group` property. - To update an existing collaborator, process the same request with different rights. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
body = flat_api.ResourceCollaboratorCreation() # ResourceCollaboratorCreation | 

try:
    # Add a new collaborator
    api_response = api_instance.add_score_collaborator(score, body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_score_track**
> ScoreTrack add_score_track(score, body)

Add a new video or audio track to the score

Use this method to add new track to the score. This track can then be played on flat.io or in an embedded score. This API method support medias hosted on SoundCloud, YouTube and Vimeo. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
body = flat_api.ScoreTrackCreation() # ScoreTrackCreation | 

try:
    # Add a new video or audio track to the score
    api_response = api_instance.add_score_track(score, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->add_score_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **body** | [**ScoreTrackCreation**](ScoreTrackCreation.md)|  | 

### Return type

[**ScoreTrack**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_score**
> ScoreDetails create_score(body)

Create a new score

Use this API method to **create a new music score in the current User account**. You will need a MusicXML 3 (`vnd.recordare.musicxml` or `vnd.recordare.musicxml+xml`) or a MIDI (`audio/midi`) file to create the new Flat document.  This API call will automatically create the first revision of the document, the score can be modified by the using our web application or by uploading a new revision of this file (`POST /v2/scores/{score}/revisions/{revision}`).  The currently authenticated user will be granted owner of the file and will be able to add other collaborators (users and groups).  If no `collection` is specified, the API will create the score in the most appropriate collection. This can be the `root` collection or a different collection based on the user's settings or API authentication method. If a `collection` is specified and this one has more public privacy settings than the score (e.g. `public` vs `private` for the score), the privacy settings of the created score will be adjusted to the collection ones. You can check the adjusted privacy settings in the returned score `privacy`, and optionally adjust these settings if needed using `PUT /scores/{score}`. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
body = flat_api.ScoreCreation() # ScoreCreation | 

try:
    # Create a new score
    api_response = api_instance.create_score(body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_score_revision**
> ScoreRevision create_score_revision(score, body)

Create a new revision

Update a score by uploading a new revision for this one. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
body = flat_api.ScoreRevisionCreation() # ScoreRevisionCreation | 

try:
    # Create a new revision
    api_response = api_instance.create_score_revision(score, body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_score**
> delete_score(score)

Delete a score

This method can be used by the owner/admin (`aclAdmin` rights) of a score as well as regular collaborators.  When called by an owner/admin, it will schedule the deletion of the score, its revisions, and complete history. The score won't be accessible anymore after calling this method and the user's quota will directly be updated.  When called by a regular collaborator (`aclRead` / `aclWrite`), the score will be unshared (i.e. removed from the account & own collections). 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 

try:
    # Delete a score
    api_instance.delete_score(score)
except ApiException as e:
    print("Exception when calling ScoreApi->delete_score: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_score_comment**
> delete_score_comment(score, comment, sharing_key=sharing_key)

Delete a comment

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
comment = 'comment_example' # str | Unique identifier of a sheet music comment 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Delete a comment
    api_instance.delete_score_comment(score, comment, sharing_key=sharing_key)
except ApiException as e:
    print("Exception when calling ScoreApi->delete_score_comment: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_score_track**
> delete_score_track(score, track)

Remove an audio or video track linked to the score

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
track = 'track_example' # str | Unique identifier of a score audio track 

try:
    # Remove an audio or video track linked to the score
    api_instance.delete_score_track(score, track)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_score**
> ScoreDetails edit_score(score, body=body)

Edit a score's metadata

This API method allows you to change the metadata of a score document (e.g. its `title` or `privacy`), all the properties are optional.  To edit the file itself, create a new revision using the appropriate method (`POST /v2/scores/{score}/revisions/{revision}`).  When editing the `title` of the score, the API metadata are updated directly when calling this method, unlike the data itself. The title in the score data will be \"lazy\" updated at the next score save with the editor or our internal save. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
body = flat_api.ScoreModification() # ScoreModification |  (optional)

try:
    # Edit a score's metadata
    api_response = api_instance.edit_score(score, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->edit_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **body** | [**ScoreModification**](ScoreModification.md)|  | [optional] 

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fork_score**
> ScoreDetails fork_score(score, body, sharing_key=sharing_key)

Fork a score

This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to `private`.  When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
body = flat_api.ScoreFork() # ScoreFork | 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Fork a score
    api_response = api_instance.fork_score(score, body, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ger_user_likes**
> list[ScoreDetails] ger_user_likes(user, ids=ids)

List liked scores

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
user = 'user_example' # str | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
ids = true # bool | Return only the identifiers of the scores (optional)

try:
    # List liked scores
    api_response = api_instance.ger_user_likes(user, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->ger_user_likes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | 
 **ids** | **bool**| Return only the identifiers of the scores | [optional] 

### Return type

[**list[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_scores**
> list[ScoreDetails] get_group_scores(group, parent=parent)

List group's scores

Get the list of scores shared with a group. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
group = 'group_example' # str | Unique identifier of a Flat group 
parent = 'parent_example' # str | Filter the score forked from the score id `parent` (optional)

try:
    # List group's scores
    api_response = api_instance.get_group_scores(group, parent=parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_group_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Unique identifier of a Flat group  | 
 **parent** | **str**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] 

### Return type

[**list[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score**
> ScoreDetails get_score(score, sharing_key=sharing_key)

Get a score's metadata

Get the details of a score identified by the `score` parameter in the URL. The currently authenticated user must have at least a read access to the document to use this API call. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Get a score's metadata
    api_response = api_instance.get_score(score, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_collaborator**
> ResourceCollaborator get_score_collaborator(score, collaborator, sharing_key=sharing_key)

Get a collaborator

Get the information about a collaborator (User or Group). 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
collaborator = 'collaborator_example' # str | Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group** 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Get a collaborator
    api_response = api_instance.get_score_collaborator(score, collaborator, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_collaborators**
> list[ResourceCollaborator] get_score_collaborators(score, sharing_key=sharing_key)

List the collaborators

This API call will list the different collaborators of a score and their rights on the document. The returned list will at least contain the owner of the document.  Collaborators can be a single user (the object `user` will be populated) or a group (the object `group` will be populated). 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # List the collaborators
    api_response = api_instance.get_score_collaborators(score, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_score_collaborators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**list[ResourceCollaborator]**](ResourceCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_comments**
> list[ScoreComment] get_score_comments(score, sharing_key=sharing_key, type=type, sort=sort, direction=direction)

List comments

This method lists the different comments added on a music score (documents and inline) sorted by their post dates.

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)
type = 'type_example' # str | Filter the comments by type (optional)
sort = 'sort_example' # str | Sort (optional)
direction = 'direction_example' # str | Sort direction (optional)

try:
    # List comments
    api_response = api_instance.get_score_comments(score, sharing_key=sharing_key, type=type, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_score_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 
 **type** | **str**| Filter the comments by type | [optional] 
 **sort** | **str**| Sort | [optional] 
 **direction** | **str**| Sort direction | [optional] 

### Return type

[**list[ScoreComment]**](ScoreComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_revision**
> ScoreRevision get_score_revision(score, revision, sharing_key=sharing_key)

Get a score revision

When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to get a specific revision metadata. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
revision = 'revision_example' # str | Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created. 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Get a score revision
    api_response = api_instance.get_score_revision(score, revision, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_revision_data**
> str get_score_revision_data(score, revision, format, sharing_key=sharing_key, parts=parts, only_cached=only_cached)

Get a score revision data

Retrieve the file corresponding to a score revision (the following formats are available: Flat JSON/Adagio JSON `json`, MusicXML `mxl`/`xml`, MP3 `mp3`, WAV `wav`, MIDI `midi`, or a tumbnail of the first page `thumbnail.png`). 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
revision = 'revision_example' # str | Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created. 
format = 'format_example' # str | The format of the file you will retrieve
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)
parts = 'parts_example' # str | An optional a set of parts to be exported. This parameter must be specified with a list of integers. For example \"1,2,5\".  (optional)
only_cached = true # bool | Only return files already generated and cached in Flat's production cache. If the file is not availabe, a 404 will be returned  (optional)

try:
    # Get a score revision data
    api_response = api_instance.get_score_revision_data(score, revision, format, sharing_key=sharing_key, parts=parts, only_cached=only_cached)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_score_revision_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **revision** | **str**| Unique identifier of a score revision. You can use &#x60;last&#x60; to fetch the information related to the last version created.  | 
 **format** | **str**| The format of the file you will retrieve | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 
 **parts** | **str**| An optional a set of parts to be exported. This parameter must be specified with a list of integers. For example \&quot;1,2,5\&quot;.  | [optional] 
 **only_cached** | **bool**| Only return files already generated and cached in Flat&#39;s production cache. If the file is not availabe, a 404 will be returned  | [optional] 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.recordare.musicxml+xml, application/vnd.recordare.musicxml, audio/mp3, audio/wav, audio/midi, image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_revisions**
> list[ScoreRevision] get_score_revisions(score, sharing_key=sharing_key)

List the revisions

When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to list all of them, sorted by last modification.  Depending the plan of the account, this list can be trunked to the few last revisions. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # List the revisions
    api_response = api_instance.get_score_revisions(score, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_score_revisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**list[ScoreRevision]**](ScoreRevision.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_submissions**
> list[AssignmentSubmission] get_score_submissions(score)

List submissions related to the score

This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 

try:
    # List submissions related to the score
    api_response = api_instance.get_score_submissions(score)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_score_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 

### Return type

[**list[AssignmentSubmission]**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_track**
> ScoreTrack get_score_track(score, track, sharing_key=sharing_key)

Retrieve the details of an audio or video track linked to a score

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
track = 'track_example' # str | Unique identifier of a score audio track 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Retrieve the details of an audio or video track linked to a score
    api_response = api_instance.get_score_track(score, track, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_scores**
> list[ScoreDetails] get_user_scores(user, parent=parent)

List user's scores

Get the list of public scores owned by a User.  **DEPRECATED**: Please note that the current behavior will be deprecrated on **2019-01-01**. This method will no longer list private and shared scores, but only public scores of a Flat account. If you want to access to private scores, please use the [Collections API](#tag/Collection) instead. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
user = 'user_example' # str | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
parent = 'parent_example' # str | Filter the score forked from the score id `parent` (optional)

try:
    # List user's scores
    api_response = api_instance.get_user_scores(user, parent=parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_user_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | 
 **parent** | **str**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] 

### Return type

[**list[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_score_tracks**
> list[ScoreTrack] list_score_tracks(score, sharing_key=sharing_key)

List the audio or video tracks linked to a score

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # List the audio or video tracks linked to a score
    api_response = api_instance.list_score_tracks(score, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->list_score_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**list[ScoreTrack]**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_score_comment_resolved**
> mark_score_comment_resolved(score, comment, sharing_key=sharing_key)

Mark the comment as resolved

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
comment = 'comment_example' # str | Unique identifier of a sheet music comment 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Mark the comment as resolved
    api_instance.mark_score_comment_resolved(score, comment, sharing_key=sharing_key)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_score_comment_unresolved**
> mark_score_comment_unresolved(score, comment, sharing_key=sharing_key)

Mark the comment as unresolved

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
comment = 'comment_example' # str | Unique identifier of a sheet music comment 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Mark the comment as unresolved
    api_instance.mark_score_comment_unresolved(score, comment, sharing_key=sharing_key)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_score_comment**
> ScoreComment post_score_comment(score, body, sharing_key=sharing_key)

Post a new comment

Post a document or a contextualized comment on a document.  Please note that this method includes an anti-spam system for public scores. We don't guarantee that your comments will be accepted and displayed to end-user. Comments are be blocked by returning a `403` HTTP error and hidden from other users when the `spam` property is `true`. 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
body = flat_api.ScoreCommentCreation() # ScoreCommentCreation | 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Post a new comment
    api_response = api_instance.post_score_comment(score, body, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_score_collaborator**
> remove_score_collaborator(score, collaborator)

Delete a collaborator

Remove the specified collaborator from the score 

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
collaborator = 'collaborator_example' # str | Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group** 

try:
    # Delete a collaborator
    api_instance.remove_score_collaborator(score, collaborator)
except ApiException as e:
    print("Exception when calling ScoreApi->remove_score_collaborator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **collaborator** | **str**| Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **untrash_score**
> untrash_score(score)

Untrash a score

This method will remove the score from the `trash` collection and from the deletion queue, and add it back to the original collections. 

### Example
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flat_api.ScoreApi()
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 

try:
    # Untrash a score
    api_instance.untrash_score(score)
except ApiException as e:
    print("Exception when calling ScoreApi->untrash_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_score_comment**
> ScoreComment update_score_comment(score, comment, body, sharing_key=sharing_key)

Update an existing comment

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
comment = 'comment_example' # str | Unique identifier of a sheet music comment 
body = flat_api.ScoreCommentUpdate() # ScoreCommentUpdate | 
sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

try:
    # Update an existing comment
    api_response = api_instance.update_score_comment(score, comment, body, sharing_key=sharing_key)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_score_track**
> ScoreTrack update_score_track(score, track, body)

Update an audio or video track linked to a score

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
api_instance = flat_api.ScoreApi(flat_api.ApiClient(configuration))
score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
track = 'track_example' # str | Unique identifier of a score audio track 
body = flat_api.ScoreTrackUpdate() # ScoreTrackUpdate | 

try:
    # Update an audio or video track linked to a score
    api_response = api_instance.update_score_track(score, track, body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

