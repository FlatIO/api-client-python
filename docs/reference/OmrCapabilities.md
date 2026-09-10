# OmrCapabilities

What the account or app can do, for client feature-detection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steps** | [**List[OmrStepName]**](OmrStepName.md) | Interactive steps this server supports. | 
**formats** | **List[str]** | Export formats available via &#x60;getOmrJobExport&#x60;. | 
**outputs** | [**List[OmrJobOutput]**](OmrJobOutput.md) | Output destinations the account can use when creating a job. | 
**max_files** | **int** | Maximum number of input files that can be added to a single job. | 
**max_pages** | **int** | Maximum number of pages allowed across all input files of a single job. | 
**max_parallel_jobs** | **int** | Maximum number of OMR jobs that can run in parallel for this account. | 
**max_file_size** | **int** | Maximum size of a single file, in bytes. | 
**accepted_mime_types** | **List[str]** | MIME types accepted for input files: PDF, plus the raster image formats.  Drive the file picker from this list rather than hardcoding it, so newly supported formats need no client release. A file is identified by its content, so its declared type and its extension do not have to match.  A multi-page input counts as several pages against &#x60;maxPages&#x60; and is charged accordingly. That covers PDFs and, among the image formats, multi-page TIFF and animated GIF/WebP.  | 
**accepted_extensions** | **List[str]** | Filename extensions the accepted types appear under, for building a file picker.  Use these alongside &#x60;acceptedMimeTypes&#x60; in an &#x60;accept&#x60; attribute: browsers and native file dialogs filter unreliably on some of the image types, so a valid file can be greyed out when only its MIME type is offered.  Longer than &#x60;acceptedMimeTypes&#x60;, because one type arrives under several extensions (&#x60;.jpg&#x60; and &#x60;.jpeg&#x60;, &#x60;.tif&#x60; and &#x60;.tiff&#x60;, &#x60;.heic&#x60; and &#x60;.heif&#x60;).  Picker metadata only. A file is identified by its content, so its extension never decides whether an upload is accepted.  | 
**cost_per_page** | **int** | Credits charged per page. | [optional] 
**remaining_credits** | **int** | OMR credits remaining for the account. | [optional] 
**retention_days** | **int** | How many days a &#x60;musicxml&#x60; job&#39;s uploaded files and results are kept before erasure.  Reflects the account&#39;s own period when one has been set, otherwise the platform default. Read-only: contact support to change it. Jobs with &#x60;output: library&#x60; are not covered by the retention policy and are unaffected by this value.  | [optional] 
**locales** | **List[str]** | Locales selectable for OCR, as BCP 47 codes sorted alphabetically.  These are the locales the recognition pipeline can actually read, which is neither the list of Flat interface locales nor a fixed set: new languages are added over time. Clients should default to the user&#39;s own locale when it appears here.  | 
**locales_details** | [**List[OmrLocaleDetails]**](OmrLocaleDetails.md) | The same locales as &#x60;locales&#x60;, each with its English display name, sorted alphabetically by &#x60;name&#x60; and ready to bind to a language picker.  Prefer this over &#x60;locales&#x60; when rendering a selector: it saves clients from shipping their own code-to-label table.  | 

## Example

```python
from flat_api.models.omr_capabilities import OmrCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of OmrCapabilities from a JSON string
omr_capabilities_instance = OmrCapabilities.from_json(json)
# print the JSON string representation of the object
print(OmrCapabilities.to_json())

# convert the object into a dict
omr_capabilities_dict = omr_capabilities_instance.to_dict()
# create an instance of OmrCapabilities from a dict
omr_capabilities_from_dict = OmrCapabilities.from_dict(omr_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


