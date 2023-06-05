# flat_api.CollectionApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_score_to_collection**](CollectionApi.md#add_score_to_collection) | **PUT** /collections/{collection}/scores/{score} | Add a score to the collection
[**create_collection**](CollectionApi.md#create_collection) | **POST** /collections | Create a new collection
[**delete_collection**](CollectionApi.md#delete_collection) | **DELETE** /collections/{collection} | Delete the collection
[**delete_score_from_collection**](CollectionApi.md#delete_score_from_collection) | **DELETE** /collections/{collection}/scores/{score} | Delete a score from the collection
[**edit_collection**](CollectionApi.md#edit_collection) | **PUT** /collections/{collection} | Update a collection&#39;s metadata
[**get_collection**](CollectionApi.md#get_collection) | **GET** /collections/{collection} | Get collection details
[**list_collection_scores**](CollectionApi.md#list_collection_scores) | **GET** /collections/{collection}/scores | List the scores contained in a collection
[**list_collections**](CollectionApi.md#list_collections) | **GET** /collections | List the collections
[**untrash_collection**](CollectionApi.md#untrash_collection) | **POST** /collections/{collection}/untrash | Untrash a collection


# **add_score_to_collection**
> ScoreDetails add_score_to_collection(collection, score)

Add a score to the collection

This operation will add a score to a collection. The default behavior will make the score available across multiple collections. You must have the capability `canAddScores` on the provided `collection` to perform the action. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    collection = "collection_example" # str | Unique identifier of the collection. The following aliases are supported: - `root`: The root collection of the account - `app`: Alias for the current app collection - `sharedWithMe`: Automatically contains new resources that have been shared individually - `trash`: Automatically contains resources that have been deleted 
    score = "score_example" # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    sharing_key = "sharingKey_example" # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a score to the collection
        api_response = api_instance.add_score_to_collection(collection, score)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->add_score_to_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a score to the collection
        api_response = api_instance.add_score_to_collection(collection, score, sharing_key=sharing_key)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->add_score_to_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted  |
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
**403** | Not granted to access to this collection or score |  -  |
**404** | Collection or score not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> Collection create_collection(body)

Create a new collection

This method will create a new collection and add it to your `root` collection. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
from flat_api.model.collection_creation import CollectionCreation
from flat_api.model.collection import Collection
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    body = CollectionCreation(
        title="title_example",
        privacy=CollectionPrivacy("private"),
    ) # CollectionCreation | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new collection
        api_response = api_instance.create_collection(body)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->create_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionCreation**](CollectionCreation.md)|  |

### Return type

[**Collection**](Collection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection created |  -  |
**400** | Bad collection creation request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> delete_collection(collection)

Delete the collection

This method will schedule the deletion of the collection. Until deleted, the collection will be available in the `trash`. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    collection = "collection_example" # str | Unique identifier of the collection. The following aliases are supported: - `root`: The root collection of the account - `app`: Alias for the current app collection - `sharedWithMe`: Automatically contains new resources that have been shared individually - `trash`: Automatically contains resources that have been deleted 

    # example passing only required values which don't have defaults set
    try:
        # Delete the collection
        api_instance.delete_collection(collection)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->delete_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted  |

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
**204** | Collection deleted |  -  |
**403** | Not granted to access to this collection |  -  |
**404** | Collection not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_score_from_collection**
> delete_score_from_collection(collection, score)

Delete a score from the collection

This method will delete a score from the collection. Unlike [`DELETE /scores/{score}`](#operation/deleteScore), this score will not remove the score from your account, but only from the collection. This can be used to *move* a score from one collection to another, or simply remove a score from one collection when this one is contained in multiple collections. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    collection = "collection_example" # str | Unique identifier of the collection. The following aliases are supported: - `root`: The root collection of the account - `app`: Alias for the current app collection - `sharedWithMe`: Automatically contains new resources that have been shared individually - `trash`: Automatically contains resources that have been deleted 
    score = "score_example" # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    sharing_key = "sharingKey_example" # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a score from the collection
        api_instance.delete_score_from_collection(collection, score)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->delete_score_from_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a score from the collection
        api_instance.delete_score_from_collection(collection, score, sharing_key=sharing_key)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->delete_score_from_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted  |
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  |
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
**204** | Score removed from the collection |  -  |
**403** | Not granted to access to this collection |  -  |
**404** | Collection not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_collection**
> Collection edit_collection(collection)

Update a collection's metadata

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
from flat_api.model.collection import Collection
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.collection_modification import CollectionModification
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    collection = "collection_example" # str | Unique identifier of the collection. The following aliases are supported: - `root`: The root collection of the account - `app`: Alias for the current app collection - `sharedWithMe`: Automatically contains new resources that have been shared individually - `trash`: Automatically contains resources that have been deleted 
    body = CollectionModification(
        title="title_example",
        privacy=CollectionPrivacy("private"),
    ) # CollectionModification |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a collection's metadata
        api_response = api_instance.edit_collection(collection)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->edit_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a collection's metadata
        api_response = api_instance.edit_collection(collection, body=body)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->edit_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted  |
 **body** | [**CollectionModification**](CollectionModification.md)|  | [optional]

### Return type

[**Collection**](Collection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection details |  -  |
**403** | Not granted to access to this collection |  -  |
**404** | Collection not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> Collection get_collection(collection)

Get collection details

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
from flat_api.model.collection import Collection
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    collection = "collection_example" # str | Unique identifier of the collection. The following aliases are supported: - `root`: The root collection of the account - `app`: Alias for the current app collection - `sharedWithMe`: Automatically contains new resources that have been shared individually - `trash`: Automatically contains resources that have been deleted 
    sharing_key = "sharingKey_example" # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get collection details
        api_response = api_instance.get_collection(collection)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->get_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get collection details
        api_response = api_instance.get_collection(collection, sharing_key=sharing_key)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted  |
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional]

### Return type

[**Collection**](Collection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection details |  -  |
**403** | Not granted to access to this collection |  -  |
**404** | Collection not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collection_scores**
> [ScoreDetails] list_collection_scores(collection)

List the scores contained in a collection

Use this method to list the scores contained in a collection. If no sort option is provided, the scores are sorted by `modificationDate` `desc`.  For example, to list the scores contained in your app collection, you can use `GET /v2/collections/app/scores`. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    collection = "collection_example" # str | Unique identifier of the collection. The following aliases are supported: - `root`: The root collection of the account - `app`: Alias for the current app collection - `sharedWithMe`: Automatically contains new resources that have been shared individually - `trash`: Automatically contains resources that have been deleted 
    sharing_key = "sharingKey_example" # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)
    sort = "creationDate" # str | Sort (optional)
    direction = "asc" # str | Sort direction (optional)
    limit = 25 # int | This is the maximum number of objects that may be returned (optional) if omitted the server will use the default value of 25
    next = "next_example" # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = "previous_example" # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List the scores contained in a collection
        api_response = api_instance.list_collection_scores(collection)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->list_collection_scores: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the scores contained in a collection
        api_response = api_instance.list_collection_scores(collection, sharing_key=sharing_key, sort=sort, direction=direction, limit=limit, next=next, previous=previous)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->list_collection_scores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted  |
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional]
 **sort** | **str**| Sort | [optional]
 **direction** | **str**| Sort direction | [optional]
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] if omitted the server will use the default value of 25
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional]
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional]

### Return type

[**[ScoreDetails]**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of scores |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections**
> [Collection] list_collections()

List the collections

Use this method to list the user's collections contained in `parent` (by default in the `root` collection). If no sort option is provided, the collections are sorted by `creationDate` `desc`.  Note that this method will not include the `parent` collection in the listing. For example, if you need the details of the `root` collection, you can use `GET /v2/collections/root`.  To fetch your app collection details, you can use `GET /v2/collections/app`. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
from flat_api.model.collection import Collection
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    parent = "root" # str | List the collection contained in this `parent` collection.  This option doesn't provide a complete multi-level collection support. When sharing a collection with someone, this one will have as `parent` `sharedWithMe`.  (optional) if omitted the server will use the default value of "root"
    sort = "creationDate" # str | Sort (optional)
    direction = "asc" # str | Sort direction (optional)
    limit = 25 # int | This is the maximum number of objects that may be returned (optional) if omitted the server will use the default value of 25
    next = "next_example" # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = "previous_example" # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the collections
        api_response = api_instance.list_collections(parent=parent, sort=sort, direction=direction, limit=limit, next=next, previous=previous)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->list_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| List the collection contained in this &#x60;parent&#x60; collection.  This option doesn&#39;t provide a complete multi-level collection support. When sharing a collection with someone, this one will have as &#x60;parent&#x60; &#x60;sharedWithMe&#x60;.  | [optional] if omitted the server will use the default value of "root"
 **sort** | **str**| Sort | [optional]
 **direction** | **str**| Sort direction | [optional]
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] if omitted the server will use the default value of 25
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional]
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional]

### Return type

[**[Collection]**](Collection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of collections |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **untrash_collection**
> untrash_collection(collection)

Untrash a collection

This method will restore the collection by removing it from the `trash` and add it back to the `root` collection. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import flat_api
from flat_api.api import collection_api
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
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)
    collection = "collection_example" # str | Unique identifier of the collection. The following aliases are supported: - `root`: The root collection of the account - `app`: Alias for the current app collection - `sharedWithMe`: Automatically contains new resources that have been shared individually - `trash`: Automatically contains resources that have been deleted 

    # example passing only required values which don't have defaults set
    try:
        # Untrash a collection
        api_instance.untrash_collection(collection)
    except flat_api.ApiException as e:
        print("Exception when calling CollectionApi->untrash_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted  |

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

