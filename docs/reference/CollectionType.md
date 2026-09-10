# CollectionType

Type of the collection. The type will influence the capabilitied available on the collections and how this collection is/can be populated.  - `root`: **Deprecated.** Previously the root collection of the user. The `allScores` virtual collection should be used instead. - `regular`: A regular collection created by the user. This collection can be deleted and modified by the user. - `app`: An automatically created collection containing the scores created by an app (e.g. Music Snippet) - `trash`: An automatically created collection containing the trashed scores.  Virtual collections:  - `allScores`: All the scores contained in the user account - `collaborations`: All shared scores by the user or someone else - `likes`: Liked scores 

## Enum

* `ROOT` (value: `'root'`)

* `REGULAR` (value: `'regular'`)

* `APP` (value: `'app'`)

* `TRASH` (value: `'trash'`)

* `ALLSCORES` (value: `'allScores'`)

* `COLLABORATIONS` (value: `'collaborations'`)

* `LIKES` (value: `'likes'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


