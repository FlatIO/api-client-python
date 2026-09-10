# flat_api.OMRApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_omr_job_file**](OMRApi.md#add_omr_job_file) | **POST** /omr/jobs/{job}/files | Add a file to an OMR job
[**cancel_omr_job**](OMRApi.md#cancel_omr_job) | **POST** /omr/jobs/{job}/cancel | Cancel an OMR job
[**create_omr_job**](OMRApi.md#create_omr_job) | **POST** /omr/jobs | Create an OMR job
[**delete_omr_job**](OMRApi.md#delete_omr_job) | **DELETE** /omr/jobs/{job} | Delete an OMR job&#39;s data
[**get_omr_capabilities**](OMRApi.md#get_omr_capabilities) | **GET** /omr/capabilities | OMR capabilities and limits
[**get_omr_job**](OMRApi.md#get_omr_job) | **GET** /omr/jobs/{job} | Get an OMR job
[**get_omr_job_export**](OMRApi.md#get_omr_job_export) | **GET** /omr/jobs/{job}/exports/{format} | Download the finalized result
[**get_omr_job_file**](OMRApi.md#get_omr_job_file) | **GET** /omr/jobs/{job}/files/{index} | Get an input page image
[**list_billing_credits_history**](OMRApi.md#list_billing_credits_history) | **GET** /billing/credits/history | List credit history
[**list_omr_jobs**](OMRApi.md#list_omr_jobs) | **GET** /omr/jobs | List OMR jobs
[**start_omr_job**](OMRApi.md#start_omr_job) | **POST** /omr/jobs/{job}/start | Start an OMR job
[**submit_omr_job_step**](OMRApi.md#submit_omr_job_step) | **POST** /omr/jobs/{job}/steps/{step} | Submit an interactive step


# **add_omr_job_file**
> OmrJobFileUploadResult add_omr_job_file(job, omr_job_file_upload, x_flat_locale=x_flat_locale)

Add a file to an OMR job

Add one image or PDF to a draft job. Call once per file; files keep their upload order.

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_job_file_upload import OmrJobFileUpload
from flat_api.models.omr_job_file_upload_result import OmrJobFileUploadResult
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
    api_instance = flat_api.OMRApi(api_client)
    job = 'job_example' # str | Unique identifier of the OMR job
    omr_job_file_upload = flat_api.OmrJobFileUpload() # OmrJobFileUpload | 
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Add a file to an OMR job
        api_response = api_instance.add_omr_job_file(job, omr_job_file_upload, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->add_omr_job_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->add_omr_job_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Unique identifier of the OMR job | 
 **omr_job_file_upload** | [**OmrJobFileUpload**](OmrJobFileUpload.md)|  | 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**OmrJobFileUploadResult**](OmrJobFileUploadResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File added |  -  |
**409** | Job is not in draft state |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_omr_job**
> OmrJob cancel_omr_job(job, x_flat_locale=x_flat_locale)

Cancel an OMR job

Cancel a draft or in-flight job. Any charged credits are reversed.

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_job import OmrJob
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
    api_instance = flat_api.OMRApi(api_client)
    job = 'job_example' # str | Unique identifier of the OMR job
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Cancel an OMR job
        api_response = api_instance.cancel_omr_job(job, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->cancel_omr_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->cancel_omr_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Unique identifier of the OMR job | 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**OmrJob**](OmrJob.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Canceled |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_omr_job**
> OmrJob create_omr_job(omr_job_creation, x_flat_locale=x_flat_locale)

Create an OMR job

Create an Optical Music Recognition job. There are two ways to call this endpoint:

* **Draft:** send the parameters without `files` to create an empty job, then add
  files with `addOmrJobFile`, then run it with `startOmrJob`. Best for multiple
  images or incremental mobile capture.
* **One-shot:** include `files` and `autoStart: true` to import in a single request.
  Best for a single PDF or a third-party integration.

Declare the interactive steps your client supports in `interactiveSteps`: the pipeline
runs fully automatically and only pauses at the steps you list. Steps you do not list,
including ones added in the future, are auto-resolved with server defaults, so older
clients never break.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_job import OmrJob
from flat_api.models.omr_job_creation import OmrJobCreation
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
    api_instance = flat_api.OMRApi(api_client)
    omr_job_creation = flat_api.OmrJobCreation() # OmrJobCreation | 
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Create an OMR job
        api_response = api_instance.create_omr_job(omr_job_creation, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->create_omr_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->create_omr_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **omr_job_creation** | [**OmrJobCreation**](OmrJobCreation.md)|  | 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**OmrJob**](OmrJob.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Draft created |  -  |
**202** | One-shot job started (files provided with autoStart) |  -  |
**402** | Account overquota or feature not included |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_omr_job**
> OmrJob delete_omr_job(job, x_flat_locale=x_flat_locale)

Delete an OMR job's data

Erase a job's uploaded files and recognition results now, instead of waiting for its
retention deadline. Use this to serve a deletion request from your own end user.

Reaches the same end state as the scheduled cleanup: the files are gone, the job keeps
the `status` it finished with, stays listable, and reports `retention.expiredDate`.
Downloads then fail with `OMR_JOB_EXPIRED`.

Only available for jobs whose `output` is `musicxml`. Library imports are not covered
by the retention policy and are rejected with `OMR_JOB_NOT_EXPIRABLE`; delete the
resulting score instead.

The job must have finished (`done`, `error` or `canceled`). A draft or in-flight job
is rejected with `OMR_JOB_IN_PROGRESS`: cancel it first, then delete. Deleting never
cancels on your behalf, because cancellation reverses charged credits and that must
not happen as a side effect of erasing data.

Calling this again on an already-erased job succeeds and changes nothing.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_job import OmrJob
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
    api_instance = flat_api.OMRApi(api_client)
    job = 'job_example' # str | Unique identifier of the OMR job
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Delete an OMR job's data
        api_response = api_instance.delete_omr_job(job, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->delete_omr_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->delete_omr_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Unique identifier of the OMR job | 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**OmrJob**](OmrJob.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job data erased |  -  |
**403** | Not the owner of this job |  -  |
**404** | Job not found |  -  |
**409** | Job is not covered by the retention policy, or has not finished yet |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_omr_capabilities**
> OmrCapabilities get_omr_capabilities(x_flat_locale=x_flat_locale)

OMR capabilities and limits

Advertises the supported steps, export formats, limits, cost-per-page, remaining
credits and locales, so clients can feature-detect instead of hardcoding behavior.

Authentication is optional: called without an account, the limits are those of the
free plan and `remainingCredits` is omitted.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_capabilities import OmrCapabilities
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
    api_instance = flat_api.OMRApi(api_client)
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # OMR capabilities and limits
        api_response = api_instance.get_omr_capabilities(x_flat_locale=x_flat_locale)
        print("The response of OMRApi->get_omr_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->get_omr_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**OmrCapabilities**](OmrCapabilities.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Capabilities |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_omr_job**
> OmrJob get_omr_job(job, wait=wait, x_flat_locale=x_flat_locale)

Get an OMR job

Get the current state of an OMR job. This is the primary polling endpoint. Pass
`wait` to long-poll until the state changes.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_job import OmrJob
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
    api_instance = flat_api.OMRApi(api_client)
    job = 'job_example' # str | Unique identifier of the OMR job
    wait = 56 # int | Long-poll up to this many seconds for a state change before returning. (optional)
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Get an OMR job
        api_response = api_instance.get_omr_job(job, wait=wait, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->get_omr_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->get_omr_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Unique identifier of the OMR job | 
 **wait** | **int**| Long-poll up to this many seconds for a state change before returning. | [optional] 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**OmrJob**](OmrJob.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job state |  -  |
**404** | Job not found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_omr_job_export**
> bytes get_omr_job_export(job, format, x_flat_locale=x_flat_locale)

Download the finalized result

Stream the finalized result in the requested format. Available once the job is `done`.
For `output: musicxml` jobs this is the primary way to retrieve the result; no library
score is created.


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
    api_instance = flat_api.OMRApi(api_client)
    job = 'job_example' # str | Unique identifier of the OMR job
    format = 'format_example' # str | Export format. New formats may be added over time; request what your client supports.  * `musicxml`: Uncompressed MusicXML (plain text `.xml`, `application/vnd.recordare.musicxml+xml`). * `mxl`: Compressed MusicXML (zip archive `.mxl`, `application/vnd.recordare.musicxml`), the same notation as `musicxml` but smaller to download. * `midi`: Standard MIDI file (`.mid`, `audio/midi`). * `thumbnail.png`: PNG preview of the first page (`image/png`). 
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Download the finalized result
        api_response = api_instance.get_omr_job_export(job, format, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->get_omr_job_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->get_omr_job_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Unique identifier of the OMR job | 
 **format** | **str**| Export format. New formats may be added over time; request what your client supports.  * &#x60;musicxml&#x60;: Uncompressed MusicXML (plain text &#x60;.xml&#x60;, &#x60;application/vnd.recordare.musicxml+xml&#x60;). * &#x60;mxl&#x60;: Compressed MusicXML (zip archive &#x60;.mxl&#x60;, &#x60;application/vnd.recordare.musicxml&#x60;), the same notation as &#x60;musicxml&#x60; but smaller to download. * &#x60;midi&#x60;: Standard MIDI file (&#x60;.mid&#x60;, &#x60;audio/midi&#x60;). * &#x60;thumbnail.png&#x60;: PNG preview of the first page (&#x60;image/png&#x60;).  | 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

**bytes**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exported file (content type depends on the requested format) |  * Content-Disposition - Attachment disposition carrying the recommended filename, derived from the score&#39;s resolved work title (RFC 5987 encoded for non-ASCII titles). Clients should use this filename when saving the download. <br>  |
**404** | Format not available for this job |  -  |
**409** | Job is not finished yet (&#x60;OMR_JOB_NOT_DONE&#x60;), or its files have been erased by the data retention policy (&#x60;OMR_JOB_EXPIRED&#x60;).  |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_omr_job_file**
> bytes get_omr_job_file(job, index, x_flat_locale=x_flat_locale)

Get an input page image

Fetch one of the job's input files (a page image or PDF) by index, for the review UI.

Once data retention has erased the job, this returns 409 `OMR_JOB_EXPIRED`. Read
`retention.expiredDate` on the job to tell that case apart before requesting a file.


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
    api_instance = flat_api.OMRApi(api_client)
    job = 'job_example' # str | Unique identifier of the OMR job
    index = 56 # int | 0-based index of the input file (page) to fetch.
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Get an input page image
        api_response = api_instance.get_omr_job_file(job, index, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->get_omr_job_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->get_omr_job_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Unique identifier of the OMR job | 
 **index** | **int**| 0-based index of the input file (page) to fetch. | 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

**bytes**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Page image |  -  |
**404** | Not found |  -  |
**409** | The job&#39;s files have been erased by the data retention policy |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_billing_credits_history**
> List[CreditTransaction] list_billing_credits_history(limit=limit, next=next, previous=previous)

List credit history

The credit ledger of the authenticated account, sorted by creation date descending
(most recent entry first).

Every entry that moved the balance is listed: the deductions taken when an import
runs, and the top-ups added by a credit pack.

Reversing a deduction does not add an entry, it flips the original one's `state` to
`canceled`. Canceled entries stay in the list, so an import that was charged and then
failed still shows its deduction rather than disappearing. Read `state` to tell the two
apart, and sum only `active` entries. A refund can additionally add a positive entry
when cancelling alone could not restore the full cost, for instance because the plan's
allowance has since reset.

The current balance is not computed from this list: read it from `getOmrCapabilities`.


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.credit_transaction import CreditTransaction
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
    api_instance = flat_api.OMRApi(api_client)
    limit = 50 # int | This is the maximum number of objects that may be returned (optional) (default to 50)
    next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)

    try:
        # List credit history
        api_response = api_instance.list_billing_credits_history(limit=limit, next=next, previous=previous)
        print("The response of OMRApi->list_billing_credits_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->list_billing_credits_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] [default to 50]
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 

### Return type

[**List[CreditTransaction]**](CreditTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of credit transactions |  * Link - Pagination links (next, previous) <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_omr_jobs**
> List[OmrJob] list_omr_jobs(status=status, expired=expired, limit=limit, next=next, previous=previous, x_flat_locale=x_flat_locale)

List OMR jobs

List the caller's OMR jobs, for resuming work or cleaning up abandoned drafts.

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_job import OmrJob
from flat_api.models.omr_job_status import OmrJobStatus
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
    api_instance = flat_api.OMRApi(api_client)
    status = flat_api.OmrJobStatus() # OmrJobStatus | Filter jobs by status (optional)
    expired = True # bool | Filter by data-retention state, independently of `status`.  * `true`: only jobs whose files have been erased. * `false`: only jobs that still hold their files.  Omit to get both. A job keeps the `status` it finished with after erasure, so this is the only way to tell the two apart.  (optional)
    limit = 50 # int | This is the maximum number of objects that may be returned (optional) (default to 50)
    next = 'next_example' # str | An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    previous = 'previous_example' # str | An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the `Link` header when requesting the API. These URLs will contain a `next` and `previous` cursor based on the available data.  (optional)
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # List OMR jobs
        api_response = api_instance.list_omr_jobs(status=status, expired=expired, limit=limit, next=next, previous=previous, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->list_omr_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->list_omr_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**OmrJobStatus**](.md)| Filter jobs by status | [optional] 
 **expired** | **bool**| Filter by data-retention state, independently of &#x60;status&#x60;.  * &#x60;true&#x60;: only jobs whose files have been erased. * &#x60;false&#x60;: only jobs that still hold their files.  Omit to get both. A job keeps the &#x60;status&#x60; it finished with after erasure, so this is the only way to tell the two apart.  | [optional] 
 **limit** | **int**| This is the maximum number of objects that may be returned | [optional] [default to 50]
 **next** | **str**| An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **previous** | **str**| An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data.  | [optional] 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**List[OmrJob]**](OmrJob.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of OMR jobs |  * Link - Pagination links (next, previous) <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_omr_job**
> OmrJob start_omr_job(job, x_flat_locale=x_flat_locale)

Start an OMR job

Validate the attached files, run the permission, quota and credit checks, then queue the job for processing.

### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_job import OmrJob
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
    api_instance = flat_api.OMRApi(api_client)
    job = 'job_example' # str | Unique identifier of the OMR job
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Start an OMR job
        api_response = api_instance.start_omr_job(job, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->start_omr_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->start_omr_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Unique identifier of the OMR job | 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**OmrJob**](OmrJob.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Processing started |  -  |
**400** | No files attached |  -  |
**402** | Insufficient credits or quota |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_omr_job_step**
> OmrJob submit_omr_job_step(job, step, body, x_flat_locale=x_flat_locale)

Submit an interactive step

Resolve the step the job is currently awaiting and resume the pipeline. The request
body shape depends on `step` (a `oneOf` discriminated by the step name).


### Example

* OAuth Authentication (OAuth2):

```python
import flat_api
from flat_api.models.omr_details_submission import OmrDetailsSubmission
from flat_api.models.omr_job import OmrJob
from flat_api.models.omr_step_name import OmrStepName
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
    api_instance = flat_api.OMRApi(api_client)
    job = 'job_example' # str | Unique identifier of the OMR job
    step = flat_api.OmrStepName() # OmrStepName | The pending step being submitted
    body = flat_api.OmrDetailsSubmission() # OmrDetailsSubmission | 
    x_flat_locale = 'fr' # str | Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to `en`).  Supported normalized locales: `da`, `de`, `en`, `en-GB`, `es`, `fi`, `fil`, `fr`, `fr-CA`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `nl`, `nb`, `pl`, `pt`, `pt-BR`, `ro`, `ru`, `sv`, `tr`, `zh-Hans`, `zh-HK`, `zh-TW`.  Precedence (highest first): this `X-Flat-Locale` header, the authenticated user's account locale, the `Accept-Language` header, then `en`.  (optional)

    try:
        # Submit an interactive step
        api_response = api_instance.submit_omr_job_step(job, step, body, x_flat_locale=x_flat_locale)
        print("The response of OMRApi->submit_omr_job_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OMRApi->submit_omr_job_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Unique identifier of the OMR job | 
 **step** | [**OmrStepName**](.md)| The pending step being submitted | 
 **body** | **OmrDetailsSubmission**|  | 
 **x_flat_locale** | **str**| Preferred locale for localized content in the response (translated error messages, emails, etc.).  Accepts any IETF language tag. The API best-matches the value to a supported locale and never rejects an unknown one (it falls back to the closest match, then to &#x60;en&#x60;).  Supported normalized locales: &#x60;da&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;en-GB&#x60;, &#x60;es&#x60;, &#x60;fi&#x60;, &#x60;fil&#x60;, &#x60;fr&#x60;, &#x60;fr-CA&#x60;, &#x60;hi&#x60;, &#x60;id&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;ko&#x60;, &#x60;ms&#x60;, &#x60;nl&#x60;, &#x60;nb&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;pt-BR&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sv&#x60;, &#x60;tr&#x60;, &#x60;zh-Hans&#x60;, &#x60;zh-HK&#x60;, &#x60;zh-TW&#x60;.  Precedence (highest first): this &#x60;X-Flat-Locale&#x60; header, the authenticated user&#39;s account locale, the &#x60;Accept-Language&#x60; header, then &#x60;en&#x60;.  | [optional] 

### Return type

[**OmrJob**](OmrJob.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Step accepted, processing resumed |  -  |
**409** | Job is not awaiting this step |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

