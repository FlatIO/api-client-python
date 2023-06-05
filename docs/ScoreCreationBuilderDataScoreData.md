# ScoreCreationBuilderDataScoreData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruments** | [**[ScoreCreationBuilderDataScoreDataInstrumentsInner]**](ScoreCreationBuilderDataScoreDataInstrumentsInner.md) | The list of instruments to add to the score. See https://prod.flat-cdn.com/fixtures/instruments_en.json for the possible values for &#x60;group&#x60; and &#x60;instrument&#x60;.  | 
**use_tab_staff** | **bool** | true if the TAB staff is displayed with fretted instruments | [optional] 
**use_chord_grid** | **bool** | true if the chord grid must be displayed with fretted instruments | [optional] 
**fifths** | **float** | The key signature of the score (expressed between -7 and 7). Major C is used when the value is not provided. | [optional] 
**nb_beats** | **float** | The number of beats in the measure | [optional] 
**beat_type** | **float** | The duration of a beat in the measure | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


