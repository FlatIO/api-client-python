# OmrJobStatus

Public, client-facing status of the job, derived from the internal job and task state.  * `draft`: created, files can still be added; not yet started or charged. * `processing`: the pipeline is running. * `awaitingInput`: paused on the `currentStep`, waiting for the client to submit it. * `done`: finished. See `result`. * `error`: failed. See `errorCode`. * `canceled`: canceled by the client. 

## Enum

* `DRAFT` (value: `'draft'`)

* `PROCESSING` (value: `'processing'`)

* `AWAITINGINPUT` (value: `'awaitingInput'`)

* `DONE` (value: `'done'`)

* `ERROR` (value: `'error'`)

* `CANCELED` (value: `'canceled'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


