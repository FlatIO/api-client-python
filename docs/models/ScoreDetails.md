# flat_api.model.score_details.ScoreDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier of the score | [optional] 
**sharingKey** | str,  | str,  | The private sharing key of the score (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) | [optional] 
**title** | str,  | str,  | The title of the score | [optional] 
**privacy** | [**ScorePrivacy**](ScorePrivacy.md) | [**ScorePrivacy**](ScorePrivacy.md) |  | [optional] 
**user** | [**UserPublicSummary**](UserPublicSummary.md) | [**UserPublicSummary**](UserPublicSummary.md) |  | [optional] 
**htmlUrl** | str,  | str,  | The url where the score can be viewed in a web browser | [optional] 
**subtitle** | str,  | str,  | Subtitle of the score | [optional] 
**lyricist** | str,  | str,  | Lyricist of the score | [optional] 
**arranger** | str,  | str,  | Arranger of the score | [optional] 
**composer** | str,  | str,  | Composer of the score | [optional] 
**description** | str,  | str,  | Description of the creation | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | Tags describing the score | [optional] 
**creationType** | [**ScoreCreationType**](ScoreCreationType.md) | [**ScoreCreationType**](ScoreCreationType.md) |  | [optional] 
**license** | [**ScoreLicense**](ScoreLicense.md) | [**ScoreLicense**](ScoreLicense.md) |  | [optional] 
**licenseText** | str,  | str,  | Additional license text written on the exported/printed score | [optional] 
**durationTime** | decimal.Decimal, int, float,  | decimal.Decimal,  | In seconds, an approximative duration of the score | [optional] 
**numberMeasures** | decimal.Decimal, int,  | decimal.Decimal,  | The number of measures in the score | [optional] 
**mainTempoQpm** | decimal.Decimal, int, float,  | decimal.Decimal,  | The main tempo of the score (in QPM) | [optional] 
**rights** | [**ResourceRights**](ResourceRights.md) | [**ResourceRights**](ResourceRights.md) |  | [optional] 
**[collaborators](#collaborators)** | list, tuple,  | tuple,  | The list of the collaborators of the score | [optional] 
**creationDate** | str, datetime,  | str,  | The date when the score was created | [optional] value must conform to RFC-3339 date-time
**modificationDate** | str, datetime,  | str,  | The date of the last revision of the score | [optional] value must conform to RFC-3339 date-time
**publicationDate** | str, datetime,  | str,  | The date when the score was published on Flat | [optional] value must conform to RFC-3339 date-time
**organization** | str,  | str,  | If the score has been created in an organization, the identifier of this organization. This property is especially used with the score privacy &#x60;organizationPublic&#x60;.  | [optional] 
**parentScore** | str,  | str,  | If the score has been forked, the unique identifier of the parent score.  | [optional] 
**[instruments](#instruments)** | list, tuple,  | tuple,  | An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat&#x27;s UI or instruments icons. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  | [optional] 
**[samples](#samples)** | list, tuple,  | tuple,  | An array of the audio samples identifiers used the different score parts. The format of the strings is &#x60;{instrument-group}.{sample-id}&#x60;.  | [optional] 
**googleDriveFileId** | str,  | str,  | If the user uses Google Drive and the score exists on Google Drive, this field will contain the unique identifier of the Flat score on Google Drive. You can access the document using the url: &#x60;https://drive.google.com/open?id&#x3D;{googleDriveFileId}&#x60;  | [optional] 
**likes** | [**ScoreLikesCounts**](ScoreLikesCounts.md) | [**ScoreLikesCounts**](ScoreLikesCounts.md) |  | [optional] 
**comments** | [**ScoreCommentsCounts**](ScoreCommentsCounts.md) | [**ScoreCommentsCounts**](ScoreCommentsCounts.md) |  | [optional] 
**views** | [**ScoreViewsCounts**](ScoreViewsCounts.md) | [**ScoreViewsCounts**](ScoreViewsCounts.md) |  | [optional] 
**plays** | [**ScorePlaysCounts**](ScorePlaysCounts.md) | [**ScorePlaysCounts**](ScorePlaysCounts.md) |  | [optional] 
**[collections](#collections)** | list, tuple,  | tuple,  | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Tags describing the score

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tags describing the score | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# collaborators

The list of the collaborators of the score

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of the collaborators of the score | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResourceCollaborator**](ResourceCollaborator.md) | [**ResourceCollaborator**](ResourceCollaborator.md) | [**ResourceCollaborator**](ResourceCollaborator.md) |  | 

# instruments

An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat's UI or instruments icons. The format of the strings is `{instrument-group}.{instrument-id}`. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat&#x27;s UI or instruments icons. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# samples

An array of the audio samples identifiers used the different score parts. The format of the strings is `{instrument-group}.{sample-id}`. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of the audio samples identifiers used the different score parts. The format of the strings is &#x60;{instrument-group}.{sample-id}&#x60;.  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# collections

The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

