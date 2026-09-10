# OmrJobRetention

Data-retention state of the job.  Present only on jobs whose `output` is `musicxml`. Jobs imported into the Flat library are part of your library content, are not covered by this policy, and omit this object entirely.  Erasure is performed by a periodic cleanup pass, so the files are removed shortly after `expiryDate` rather than exactly on it. Plan for the deadline, not the instant. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** | When this job&#39;s uploaded files and recognition results become eligible for erasure. Fixed when the job is created: changing the account&#39;s retention period does not move the deadline of jobs that already exist.  | 
**expired_date** | **datetime** | When the job&#39;s stored files were actually erased. Present only once that happened.  An expired job keeps the &#x60;status&#x60; it finished with and stays listable, but its &#x60;result&#x60; is no longer served and downloads fail with &#x60;OMR_JOB_EXPIRED&#x60;.  | [optional] 

## Example

```python
from flat_api.models.omr_job_retention import OmrJobRetention

# TODO update the JSON string below
json = "{}"
# create an instance of OmrJobRetention from a JSON string
omr_job_retention_instance = OmrJobRetention.from_json(json)
# print the JSON string representation of the object
print(OmrJobRetention.to_json())

# convert the object into a dict
omr_job_retention_dict = omr_job_retention_instance.to_dict()
# create an instance of OmrJobRetention from a dict
omr_job_retention_from_dict = OmrJobRetention.from_dict(omr_job_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


