# OmrDetectedInstrument

One detected part.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | 0-based position of the part in the score. | 
**part_name** | **str** | Verbatim part name read from the score. | [optional] 
**instrument_id** | **str** | Flat instrument ID in dotted &#x60;&lt;group&gt;.&lt;instrument&gt;&#x60; form, for example &#x60;brass.horn&#x60; or &#x60;vocals.voice-oohs&#x60;. See the [Instrument IDs reference](https://flat.io/developers/docs/api/instruments). Always the canonical (non-premium) ID. | [optional] 
**instrument_name** | **str** | Localized display name, resolved server-side so the client needs no instruments dictionary. | [optional] 
**midi_program** | **int** | General MIDI program number. | [optional] 
**transpose_key** | **str** | Transposition or written key shown in the UI, for example &#x60;F&#x60; for Horn in F. | [optional] 
**resolved_confidence** | **str** | Server confidence in the resolved instrument match. | [optional] 

## Example

```python
from flat_api.models.omr_detected_instrument import OmrDetectedInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of OmrDetectedInstrument from a JSON string
omr_detected_instrument_instance = OmrDetectedInstrument.from_json(json)
# print the JSON string representation of the object
print(OmrDetectedInstrument.to_json())

# convert the object into a dict
omr_detected_instrument_dict = omr_detected_instrument_instance.to_dict()
# create an instance of OmrDetectedInstrument from a dict
omr_detected_instrument_from_dict = OmrDetectedInstrument.from_dict(omr_detected_instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


