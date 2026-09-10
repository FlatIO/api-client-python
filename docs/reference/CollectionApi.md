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
> ScoreDetails add_score_to_collection(collection, score, sharing_key=sharing_key)

Add a score to the collection

This operation will add a score to a collection. The default behavior will make the score available across multiple collections.
You must have the capability `canAddScores` on the provided `collection` to perform the action.


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
    api_instance = flat_api.CollectionApi(api_client)
    collection = 'collection_example' # str | Unique identifier of the collection.  The following collection aliases are supported: - `root`: **Deprecated.** The root collection of the account - `app`: Alias for the current app collection - `trash`: Automatically contains resources that have been deleted 
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Add a score to the collection
        api_response = api_instance.add_score_to_collection(collection, score, sharing_key=sharing_key)
        print("The response of CollectionApi->add_score_to_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->add_score_to_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection.  The following collection aliases are supported: - &#x60;root&#x60;: **Deprecated.** The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;trash&#x60;: Automatically contains resources that have been deleted  | 
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
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

This method will create a new collection in your account.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.collection import Collection
from flat_api.models.collection_creation import CollectionCreation
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
    api_instance = flat_api.CollectionApi(api_client)
    body = flat_api.CollectionCreation() # CollectionCreation | 

    try:
        # Create a new collection
        api_response = api_instance.create_collection(body)
        print("The response of CollectionApi->create_collection:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = flat_api.CollectionApi(api_client)
    collection = 'collection_example' # str | Unique identifier of the collection.  The following collection aliases are supported: - `root`: **Deprecated.** The root collection of the account - `app`: Alias for the current app collection - `trash`: Automatically contains resources that have been deleted  The following virtual collections are supported: - `allScores`: All the scores contained in the user account - `collaborations`: All shared scores by the user or someone else - `likes`: Liked scores 

    try:
        # Delete the collection
        api_instance.delete_collection(collection)
    except Exception as e:
        print("Exception when calling CollectionApi->delete_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection.  The following collection aliases are supported: - &#x60;root&#x60;: **Deprecated.** The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;trash&#x60;: Automatically contains resources that have been deleted  The following virtual collections are supported: - &#x60;allScores&#x60;: All the scores contained in the user account - &#x60;collaborations&#x60;: All shared scores by the user or someone else - &#x60;likes&#x60;: Liked scores  | 

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
> delete_score_from_collection(collection, score, event_properties=event_properties, sharing_key=sharing_key)

Delete a score from the collection

This method will delete a score from the collection. Unlike [`DELETE /scores/{score}`](#operation/deleteScore), this score will not remove the score from your account, but only from the collection.
This can be used to *move* a score from one collection to another, or simply remove a score from one collection when this one is contained in multiple collections.


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
    api_instance = flat_api.CollectionApi(api_client)
    collection = 'collection_example' # str | Unique identifier of the collection.  The following collection aliases are supported: - `root`: **Deprecated.** The root collection of the account - `app`: Alias for the current app collection - `trash`: Automatically contains resources that have been deleted 
    score = 'score_example' # str | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    event_properties = '{\"context\":\"discover\",\"screenLevel0\":\"home\",\"screenRoute\":\"/discover\"}' # str | Optional analytics properties merged into XP tracking for this request.  JSON-encoded string representing event properties. Example:  - `?eventProperties={\"context\":\"discover\",\"screenLevel0\":\"home\"}`  (optional)
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Delete a score from the collection
        api_instance.delete_score_from_collection(collection, score, event_properties=event_properties, sharing_key=sharing_key)
    except Exception as e:
        print("Exception when calling CollectionApi->delete_score_from_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection.  The following collection aliases are supported: - &#x60;root&#x60;: **Deprecated.** The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;trash&#x60;: Automatically contains resources that have been deleted  | 
 **score** | **str**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | 
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
**204** | Score removed from the collection |  -  |
**403** | Not granted to access to this collection |  -  |
**404** | Collection not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_collection**
> Collection edit_collection(collection, body)

Update a collection's metadata

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.collection import Collection
from flat_api.models.collection_modification import CollectionModification
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
    api_instance = flat_api.CollectionApi(api_client)
    collection = 'collection_example' # str | Unique identifier of the collection.  The following collection aliases are supported: - `root`: **Deprecated.** The root collection of the account - `app`: Alias for the current app collection - `trash`: Automatically contains resources that have been deleted  The following virtual collections are supported: - `allScores`: All the scores contained in the user account - `collaborations`: All shared scores by the user or someone else - `likes`: Liked scores 
    body = flat_api.CollectionModification() # CollectionModification | 

    try:
        # Update a collection's metadata
        api_response = api_instance.edit_collection(collection, body)
        print("The response of CollectionApi->edit_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->edit_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection.  The following collection aliases are supported: - &#x60;root&#x60;: **Deprecated.** The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;trash&#x60;: Automatically contains resources that have been deleted  The following virtual collections are supported: - &#x60;allScores&#x60;: All the scores contained in the user account - &#x60;collaborations&#x60;: All shared scores by the user or someone else - &#x60;likes&#x60;: Liked scores  | 
 **body** | [**CollectionModification**](CollectionModification.md)|  | 

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
> Collection get_collection(collection, sharing_key=sharing_key)

Get collection details

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.collection import Collection
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
    api_instance = flat_api.CollectionApi(api_client)
    collection = 'collection_example' # str | Unique identifier of the collection.  The following collection aliases are supported: - `root`: **Deprecated.** The root collection of the account - `app`: Alias for the current app collection - `trash`: Automatically contains resources that have been deleted  The following virtual collections are supported: - `allScores`: All the scores contained in the user account - `collaborations`: All shared scores by the user or someone else - `likes`: Liked scores 
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # Get collection details
        api_response = api_instance.get_collection(collection, sharing_key=sharing_key)
        print("The response of CollectionApi->get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection.  The following collection aliases are supported: - &#x60;root&#x60;: **Deprecated.** The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;trash&#x60;: Automatically contains resources that have been deleted  The following virtual collections are supported: - &#x60;allScores&#x60;: All the scores contained in the user account - &#x60;collaborations&#x60;: All shared scores by the user or someone else - &#x60;likes&#x60;: Liked scores  | 
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
> List[ScoreDetails] list_collection_scores(collection, sort=sort, direction=direction, limit=limit, next=next, previous=previous, sharing_key=sharing_key)

List the scores contained in a collection

Use this method to list the scores contained in a collection.
If no sort option is provided, the scores are sorted by `modificationDate` `desc`.

For example, to list the scores contained in your app collection, you can use `GET /v2/collections/app/scores`.


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
    api_instance = flat_api.CollectionApi(api_client)
    collection = 'collection_example' # str | Unique identifier of the collection.  The following collection aliases are supported: - `root`: **Deprecated.** The root collection of the account - `app`: Alias for the current app collection - `trash`: Automatically contains resources that have been deleted  The following virtual collections are supported: - `allScores`: All the scores contained in the user account - `collaborations`: All shared scores by the user or someone else - `likes`: Liked scores 
    sort = 'sort_example' # str | Sort (optional)
    direction = 'direction_example' # str | Sort direction (optional)
    limit = 25 # int | This is the maximum number of objects that may be returned (optional) (default to 25)
    next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    sharing_key = 'sharing_key_example' # str | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document.  (optional)

    try:
        # List the scores contained in a collection
        api_response = api_instance.list_collection_scores(collection, sort=sort, direction=direction, limit=limit, next=next, previous=previous, sharing_key=sharing_key)
        print("The response of CollectionApi->list_collection_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->list_collection_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection.  The following collection aliases are supported: - &#x60;root&#x60;: **Deprecated.** The root collection of the account - &#x60;app&#x60;: Alias for the current app collection - &#x60;trash&#x60;: Automatically contains resources that have been deleted  The following virtual collections are supported: - &#x60;allScores&#x60;: All the scores contained in the user account - &#x60;collaborations&#x60;: All shared scores by the user or someone else - &#x60;likes&#x60;: Liked scores  | 
 **sort** | **str**| Sort | [optional] 
 **direction** | **str**| Sort direction | [optional] 
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] [default to 25]
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **sharing_key** | **str**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] 

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
**200** | List of scores |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections**
> List[Collection] list_collections(parent=parent, sort=sort, direction=direction, limit=limit, next=next, previous=previous)

List the collections

Use this method to list the user's collections.
If no sort option is provided, the collections are sorted by `creationDate` `desc`.

By default (`parent=user`), this returns all user account collections with virtual collections on the first page.

To fetch your app collection details, you can use `GET /v2/collections/app`.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.collection import Collection
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
    api_instance = flat_api.CollectionApi(api_client)
    parent = 'user' # str | List the collections contained in this `parent` collection.  When set to `user` (default), returns the user's own collections as well as collections shared with the user.  Using `root` or `sharedWithMe` is **deprecated** and will be treated as `user`.  (optional) (default to 'user')
    sort = 'sort_example' # str | Sort (optional)
    direction = 'direction_example' # str | Sort direction (optional)
    limit = 25 # int | This is the maximum number of objects that may be returned (optional) (default to 25)
    next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)

    try:
        # List the collections
        api_response = api_instance.list_collections(parent=parent, sort=sort, direction=direction, limit=limit, next=next, previous=previous)
        print("The response of CollectionApi->list_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->list_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| List the collections contained in this &#x60;parent&#x60; collection.  When set to &#x60;user&#x60; (default), returns the user&#39;s own collections as well as collections shared with the user.  Using &#x60;root&#x60; or &#x60;sharedWithMe&#x60; is **deprecated** and will be treated as &#x60;user&#x60;.  | [optional] [default to &#39;user&#39;]
 **sort** | **str**| Sort | [optional] 
 **direction** | **str**| Sort direction | [optional] 
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] [default to 25]
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 

### Return type

[**List[Collection]**](Collection.md)

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
> FlatErrorResponse untrash_collection(collection)

Untrash a collection

**DEPRECATED** This method will restore the collection by removing it from the `trash` and add it back to the `root` collection.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.flat_error_response import FlatErrorResponse
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
    api_instance = flat_api.CollectionApi(api_client)
    collection = 'collection_example' # str | Unique identifier of the collection.

    try:
        # Untrash a collection
        api_response = api_instance.untrash_collection(collection)
        print("The response of CollectionApi->untrash_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->untrash_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection. | 

### Return type

[**FlatErrorResponse**](FlatErrorResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request - Operation no longer supported |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

