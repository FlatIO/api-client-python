# OmrInstrumentOverride

Override for a single detected part, matched by `index`. Omitted fields keep the detected value.  To set the instrument you may use **either** `instrumentId` (Flat's instrument id) **or** `midiProgram` (a standard General MIDI program) — whichever your integration prefers; you do not need both. If both are sent, `instrumentId` wins; otherwise `midiProgram` is resolved to the matching instrument; otherwise the detected instrument is kept. `transposeKey` and `partName` apply independently on top. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | 0-based position of the part to override, matching the &#x60;index&#x60; of the detected part. | 
**instrument_id** | **str** | Override the resolved instrument with this Flat instrument id, for example &#x60;brass.horn&#x60;. See the [Instrument IDs reference](https://flat.io/developers/docs/api/instruments) for valid values. Both the dotted &#x60;&lt;group&gt;.&lt;instrument&gt;&#x60; form (&#x60;brass.horn&#x60;) and the bare instrument key (&#x60;horn&#x60;) are accepted. Use this or &#x60;midiProgram&#x60;. Takes precedence over &#x60;midiProgram&#x60; when both are set.  | [optional] 
**part_name** | **str** | Override the part name. | [optional] 
**transpose_key** | **str** | Override the transposition / written key: a pitch class as a letter &#x60;A&#x60;-&#x60;G&#x60; with an optional accidental. For example &#x60;F&#x60; for Horn in F or &#x60;Bb&#x60; for a B flat clarinet.  The accidental may be ASCII &#x60;b&#x60; (flat) or &#x60;#&#x60; (sharp), or the Unicode music glyphs &#x60;♭&#x60; (U+266D) and &#x60;♯&#x60; (U+266F). Unicode accidentals are normalized to their ASCII equivalent, so &#x60;B♭&#x60; is stored and returned as &#x60;Bb&#x60;.  | [optional] 
**midi_program** | **int** | Override the instrument with a standard General MIDI program number (0-127), resolved server-side to the matching Flat instrument. Use this when you do not want to map Flat instrument ids. Ignored if &#x60;instrumentId&#x60; is also set.  | [optional] 

## Example

```python
from flat_api.models.omr_instrument_override import OmrInstrumentOverride

# TODO update the JSON string below
json = "{}"
# create an instance of OmrInstrumentOverride from a JSON string
omr_instrument_override_instance = OmrInstrumentOverride.from_json(json)
# print the JSON string representation of the object
print(OmrInstrumentOverride.to_json())

# convert the object into a dict
omr_instrument_override_dict = omr_instrument_override_instance.to_dict()
# create an instance of OmrInstrumentOverride from a dict
omr_instrument_override_from_dict = OmrInstrumentOverride.from_dict(omr_instrument_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


