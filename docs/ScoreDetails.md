# ScoreDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the score | [optional] 
**sharing_key** | **str** | The private sharing key of the score (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) | [optional] 
**title** | **str** | The title of the score | [optional] 
**privacy** | [**ScorePrivacy**](ScorePrivacy.md) |  | [optional] 
**user** | [**UserPublicSummary**](UserPublicSummary.md) |  | [optional] 
**html_url** | **str** | The url where the score can be viewed in a web browser | [optional] 
**subtitle** | **str** | Subtitle of the score | [optional] 
**lyricist** | **str** | Lyricist of the score | [optional] 
**arranger** | **str** | Arranger of the score | [optional] 
**composer** | **str** | Composer of the score | [optional] 
**description** | **str** | Description of the creation | [optional] 
**tags** | **[str]** | Tags describing the score | [optional] 
**creation_type** | [**ScoreCreationType**](ScoreCreationType.md) |  | [optional] 
**license** | [**ScoreLicense**](ScoreLicense.md) |  | [optional] 
**license_text** | **str** | Additional license text written on the exported/printed score | [optional] 
**duration_time** | **float** | In seconds, an approximative duration of the score | [optional] 
**number_measures** | **int** | The number of measures in the score | [optional] 
**main_tempo_qpm** | **float** | The main tempo of the score (in QPM) | [optional] 
**rights** | [**ResourceRights**](ResourceRights.md) |  | [optional] 
**collaborators** | [**[ResourceCollaborator]**](ResourceCollaborator.md) | The list of the collaborators of the score | [optional] 
**creation_date** | **datetime** | The date when the score was created | [optional] 
**modification_date** | **datetime** | The date of the last revision of the score | [optional] 
**publication_date** | **datetime** | The date when the score was published on Flat | [optional] 
**organization** | **str** | If the score has been created in an organization, the identifier of this organization. This property is especially used with the score privacy &#x60;organizationPublic&#x60;.  | [optional] 
**parent_score** | **str** | If the score has been forked, the unique identifier of the parent score.  | [optional] 
**instruments** | **[str]** | An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat&#39;s UI or instruments icons. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  | [optional] 
**samples** | **[str]** | An array of the audio samples identifiers used the different score parts. The format of the strings is &#x60;{instrument-group}.{sample-id}&#x60;.  | [optional] 
**google_drive_file_id** | **str** | If the user uses Google Drive and the score exists on Google Drive, this field will contain the unique identifier of the Flat score on Google Drive. You can access the document using the url: &#x60;https://drive.google.com/open?id&#x3D;{googleDriveFileId}&#x60;  | [optional] 
**likes** | [**ScoreLikesCounts**](ScoreLikesCounts.md) |  | [optional] 
**comments** | [**ScoreCommentsCounts**](ScoreCommentsCounts.md) |  | [optional] 
**views** | [**ScoreViewsCounts**](ScoreViewsCounts.md) |  | [optional] 
**plays** | [**ScorePlaysCounts**](ScorePlaysCounts.md) |  | [optional] 
**collections** | **[str]** | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

