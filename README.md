# Python Client for the Flat REST API

[![Build Status](https://travis-ci.org/FlatIO/api-client-python.svg?branch=master)](https://travis-ci.org/FlatIO/api-client-python)

The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:
- Creating and importing new music scores using MusicXML or MIDI files
- Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI)
- Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.

You can find the API reference including code samples and our OpenAPI Specification at the following url: [https://flat.io/developers/api/reference](https://flat.io/developers/api/reference).

To request some API credentials, please visit [https://flat.io/developers](https://flat.io/developers).

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project.

## Requirements.

Python 2.7 to 3.5+

## Installation & Usage
### pip install

```sh
pip install flat_api
```

```sh
pip install git+https://github.com/FlatIO/api-client-python.git
```

Then import the package:
```python
import flat_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flat_api
```

## Getting Started

Please follow the installation procedure above and then run the following:

```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
flat_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = flat_api.AccountApi()

try:
    # Get current user profile
    api_response = api_instance.get_authenticated_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_authenticated_user: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.flat.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**get_authenticated_user**](docs/AccountApi.md#get_authenticated_user) | **GET** /me | Get current user profile
*ClassApi* | [**activate_class**](docs/ClassApi.md#activate_class) | **POST** /classes/{class}/activate | Activate the class
*ClassApi* | [**add_class_user**](docs/ClassApi.md#add_class_user) | **PUT** /classes/{class}/users/{user} | Add a user to the class
*ClassApi* | [**archive_class**](docs/ClassApi.md#archive_class) | **POST** /classes/{class}/archive | Archive the class
*ClassApi* | [**copy_assignment**](docs/ClassApi.md#copy_assignment) | **POST** /classes/{class}/assignments/{assignment}/copy | Copy an assignment
*ClassApi* | [**create_assignment**](docs/ClassApi.md#create_assignment) | **POST** /classes/{class}/assignments | Assignment creation
*ClassApi* | [**create_class**](docs/ClassApi.md#create_class) | **POST** /classes | Create a new class
*ClassApi* | [**create_submission**](docs/ClassApi.md#create_submission) | **PUT** /classes/{class}/assignments/{assignment}/submissions | Create or edit a submission
*ClassApi* | [**delete_class_user**](docs/ClassApi.md#delete_class_user) | **DELETE** /classes/{class}/users/{user} | Remove a user from the class
*ClassApi* | [**edit_submission**](docs/ClassApi.md#edit_submission) | **PUT** /classes/{class}/assignments/{assignment}/submissions/{submission} | Edit a submission
*ClassApi* | [**enroll_class**](docs/ClassApi.md#enroll_class) | **POST** /classes/enroll/{enrollmentCode} | Join a class
*ClassApi* | [**get_class**](docs/ClassApi.md#get_class) | **GET** /classes/{class} | Get the details of a single class
*ClassApi* | [**get_score_submissions**](docs/ClassApi.md#get_score_submissions) | **GET** /scores/{score}/submissions | List submissions related to the score
*ClassApi* | [**get_submission**](docs/ClassApi.md#get_submission) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission} | Get a student submission
*ClassApi* | [**get_submissions**](docs/ClassApi.md#get_submissions) | **GET** /classes/{class}/assignments/{assignment}/submissions | List the students&#39; submissions
*ClassApi* | [**list_assignments**](docs/ClassApi.md#list_assignments) | **GET** /classes/{class}/assignments | Assignments listing
*ClassApi* | [**list_class_student_submissions**](docs/ClassApi.md#list_class_student_submissions) | **GET** /classes/{class}/students/{user}/submissions | List the submissions for a student
*ClassApi* | [**list_classes**](docs/ClassApi.md#list_classes) | **GET** /classes | List the classes available for the current user
*ClassApi* | [**unarchive_class**](docs/ClassApi.md#unarchive_class) | **DELETE** /classes/{class}/archive | Unarchive the class
*ClassApi* | [**update_class**](docs/ClassApi.md#update_class) | **PUT** /classes/{class} | Update the class
*CollectionApi* | [**add_score_to_collection**](docs/CollectionApi.md#add_score_to_collection) | **PUT** /collections/{collection}/scores/{score} | Add a score to the collection
*CollectionApi* | [**create_collection**](docs/CollectionApi.md#create_collection) | **POST** /collections | Create a new collection
*CollectionApi* | [**delete_collection**](docs/CollectionApi.md#delete_collection) | **DELETE** /collections/{collection} | Delete the collection
*CollectionApi* | [**delete_score_from_collection**](docs/CollectionApi.md#delete_score_from_collection) | **DELETE** /collections/{collection}/scores/{score} | Delete a score from the collection
*CollectionApi* | [**edit_collection**](docs/CollectionApi.md#edit_collection) | **PUT** /collections/{collection} | Update a collection&#39;s metadata
*CollectionApi* | [**get_collection**](docs/CollectionApi.md#get_collection) | **GET** /collections/{collection} | Get collection details
*CollectionApi* | [**list_collection_scores**](docs/CollectionApi.md#list_collection_scores) | **GET** /collections/{collection}/scores | List the scores contained in a collection
*CollectionApi* | [**list_collections**](docs/CollectionApi.md#list_collections) | **GET** /collections | List the collections
*CollectionApi* | [**untrash_collection**](docs/CollectionApi.md#untrash_collection) | **POST** /collections/{collection}/untrash | Untrash a collection
*GroupApi* | [**get_group_details**](docs/GroupApi.md#get_group_details) | **GET** /groups/{group} | Get group information
*GroupApi* | [**get_group_scores**](docs/GroupApi.md#get_group_scores) | **GET** /groups/{group}/scores | List group&#39;s scores
*GroupApi* | [**list_group_users**](docs/GroupApi.md#list_group_users) | **GET** /groups/{group}/users | List group&#39;s users
*OrganizationApi* | [**create_lti_credentials**](docs/OrganizationApi.md#create_lti_credentials) | **POST** /organizations/lti/credentials | Create a new couple of LTI 1.x credentials
*OrganizationApi* | [**create_organization_invitation**](docs/OrganizationApi.md#create_organization_invitation) | **POST** /organizations/invitations | Create a new invitation to join the organization
*OrganizationApi* | [**create_organization_user**](docs/OrganizationApi.md#create_organization_user) | **POST** /organizations/users | Create a new user account
*OrganizationApi* | [**list_lti_credentials**](docs/OrganizationApi.md#list_lti_credentials) | **GET** /organizations/lti/credentials | List LTI 1.x credentials
*OrganizationApi* | [**list_organization_invitations**](docs/OrganizationApi.md#list_organization_invitations) | **GET** /organizations/invitations | List the organization invitations
*OrganizationApi* | [**list_organization_users**](docs/OrganizationApi.md#list_organization_users) | **GET** /organizations/users | List the organization users
*OrganizationApi* | [**remove_organization_invitation**](docs/OrganizationApi.md#remove_organization_invitation) | **DELETE** /organizations/invitations/{invitation} | Remove an organization invitation
*OrganizationApi* | [**remove_organization_user**](docs/OrganizationApi.md#remove_organization_user) | **DELETE** /organizations/users/{user} | Remove an account from Flat
*OrganizationApi* | [**revoke_lti_credentials**](docs/OrganizationApi.md#revoke_lti_credentials) | **DELETE** /organizations/lti/credentials/{credentials} | Revoke LTI 1.x credentials
*OrganizationApi* | [**update_organization_user**](docs/OrganizationApi.md#update_organization_user) | **PUT** /organizations/users/{user} | Update account information
*ScoreApi* | [**add_score_collaborator**](docs/ScoreApi.md#add_score_collaborator) | **POST** /scores/{score}/collaborators | Add a new collaborator
*ScoreApi* | [**add_score_track**](docs/ScoreApi.md#add_score_track) | **POST** /scores/{score}/tracks | Add a new video or audio track to the score
*ScoreApi* | [**create_score**](docs/ScoreApi.md#create_score) | **POST** /scores | Create a new score
*ScoreApi* | [**create_score_revision**](docs/ScoreApi.md#create_score_revision) | **POST** /scores/{score}/revisions | Create a new revision
*ScoreApi* | [**delete_score**](docs/ScoreApi.md#delete_score) | **DELETE** /scores/{score} | Delete a score
*ScoreApi* | [**delete_score_comment**](docs/ScoreApi.md#delete_score_comment) | **DELETE** /scores/{score}/comments/{comment} | Delete a comment
*ScoreApi* | [**delete_score_track**](docs/ScoreApi.md#delete_score_track) | **DELETE** /scores/{score}/tracks/{track} | Remove an audio or video track linked to the score
*ScoreApi* | [**edit_score**](docs/ScoreApi.md#edit_score) | **PUT** /scores/{score} | Edit a score&#39;s metadata
*ScoreApi* | [**fork_score**](docs/ScoreApi.md#fork_score) | **POST** /scores/{score}/fork | Fork a score
*ScoreApi* | [**ger_user_likes**](docs/ScoreApi.md#ger_user_likes) | **GET** /users/{user}/likes | List liked scores
*ScoreApi* | [**get_group_scores**](docs/ScoreApi.md#get_group_scores) | **GET** /groups/{group}/scores | List group&#39;s scores
*ScoreApi* | [**get_score**](docs/ScoreApi.md#get_score) | **GET** /scores/{score} | Get a score&#39;s metadata
*ScoreApi* | [**get_score_collaborator**](docs/ScoreApi.md#get_score_collaborator) | **GET** /scores/{score}/collaborators/{collaborator} | Get a collaborator
*ScoreApi* | [**get_score_collaborators**](docs/ScoreApi.md#get_score_collaborators) | **GET** /scores/{score}/collaborators | List the collaborators
*ScoreApi* | [**get_score_comments**](docs/ScoreApi.md#get_score_comments) | **GET** /scores/{score}/comments | List comments
*ScoreApi* | [**get_score_revision**](docs/ScoreApi.md#get_score_revision) | **GET** /scores/{score}/revisions/{revision} | Get a score revision
*ScoreApi* | [**get_score_revision_data**](docs/ScoreApi.md#get_score_revision_data) | **GET** /scores/{score}/revisions/{revision}/{format} | Get a score revision data
*ScoreApi* | [**get_score_revisions**](docs/ScoreApi.md#get_score_revisions) | **GET** /scores/{score}/revisions | List the revisions
*ScoreApi* | [**get_score_submissions**](docs/ScoreApi.md#get_score_submissions) | **GET** /scores/{score}/submissions | List submissions related to the score
*ScoreApi* | [**get_score_track**](docs/ScoreApi.md#get_score_track) | **GET** /scores/{score}/tracks/{track} | Retrieve the details of an audio or video track linked to a score
*ScoreApi* | [**get_user_scores**](docs/ScoreApi.md#get_user_scores) | **GET** /users/{user}/scores | List user&#39;s scores
*ScoreApi* | [**list_score_tracks**](docs/ScoreApi.md#list_score_tracks) | **GET** /scores/{score}/tracks | List the audio or video tracks linked to a score
*ScoreApi* | [**mark_score_comment_resolved**](docs/ScoreApi.md#mark_score_comment_resolved) | **PUT** /scores/{score}/comments/{comment}/resolved | Mark the comment as resolved
*ScoreApi* | [**mark_score_comment_unresolved**](docs/ScoreApi.md#mark_score_comment_unresolved) | **DELETE** /scores/{score}/comments/{comment}/resolved | Mark the comment as unresolved
*ScoreApi* | [**post_score_comment**](docs/ScoreApi.md#post_score_comment) | **POST** /scores/{score}/comments | Post a new comment
*ScoreApi* | [**remove_score_collaborator**](docs/ScoreApi.md#remove_score_collaborator) | **DELETE** /scores/{score}/collaborators/{collaborator} | Delete a collaborator
*ScoreApi* | [**untrash_score**](docs/ScoreApi.md#untrash_score) | **POST** /scores/{score}/untrash | Untrash a score
*ScoreApi* | [**update_score_comment**](docs/ScoreApi.md#update_score_comment) | **PUT** /scores/{score}/comments/{comment} | Update an existing comment
*ScoreApi* | [**update_score_track**](docs/ScoreApi.md#update_score_track) | **PUT** /scores/{score}/tracks/{track} | Update an audio or video track linked to a score
*UserApi* | [**ger_user_likes**](docs/UserApi.md#ger_user_likes) | **GET** /users/{user}/likes | List liked scores
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /users/{user} | Get a public user profile
*UserApi* | [**get_user_scores**](docs/UserApi.md#get_user_scores) | **GET** /users/{user}/scores | List user&#39;s scores


## Documentation For Models

 - [Assignment](docs/Assignment.md)
 - [AssignmentCopy](docs/AssignmentCopy.md)
 - [AssignmentCreation](docs/AssignmentCreation.md)
 - [AssignmentSubmission](docs/AssignmentSubmission.md)
 - [AssignmentSubmissionUpdate](docs/AssignmentSubmissionUpdate.md)
 - [ClassAttachmentCreation](docs/ClassAttachmentCreation.md)
 - [ClassCreation](docs/ClassCreation.md)
 - [ClassDetails](docs/ClassDetails.md)
 - [ClassDetailsCanvas](docs/ClassDetailsCanvas.md)
 - [ClassDetailsClever](docs/ClassDetailsClever.md)
 - [ClassDetailsGoogleClassroom](docs/ClassDetailsGoogleClassroom.md)
 - [ClassDetailsGoogleDrive](docs/ClassDetailsGoogleDrive.md)
 - [ClassDetailsLti](docs/ClassDetailsLti.md)
 - [ClassRoles](docs/ClassRoles.md)
 - [ClassState](docs/ClassState.md)
 - [ClassUpdate](docs/ClassUpdate.md)
 - [Collection](docs/Collection.md)
 - [CollectionCapabilities](docs/CollectionCapabilities.md)
 - [CollectionCreation](docs/CollectionCreation.md)
 - [CollectionModification](docs/CollectionModification.md)
 - [CollectionPrivacy](docs/CollectionPrivacy.md)
 - [CollectionTitle](docs/CollectionTitle.md)
 - [CollectionType](docs/CollectionType.md)
 - [FlatErrorResponse](docs/FlatErrorResponse.md)
 - [FlatLocales](docs/FlatLocales.md)
 - [GoogleClassroomCoursework](docs/GoogleClassroomCoursework.md)
 - [GoogleClassroomSubmission](docs/GoogleClassroomSubmission.md)
 - [Group](docs/Group.md)
 - [GroupDetails](docs/GroupDetails.md)
 - [GroupType](docs/GroupType.md)
 - [LicenseMode](docs/LicenseMode.md)
 - [LicenseSources](docs/LicenseSources.md)
 - [LmsName](docs/LmsName.md)
 - [LtiCredentials](docs/LtiCredentials.md)
 - [LtiCredentialsCreation](docs/LtiCredentialsCreation.md)
 - [MediaAttachment](docs/MediaAttachment.md)
 - [MediaScoreSharingMode](docs/MediaScoreSharingMode.md)
 - [OrganizationInvitation](docs/OrganizationInvitation.md)
 - [OrganizationInvitationCreation](docs/OrganizationInvitationCreation.md)
 - [OrganizationRoles](docs/OrganizationRoles.md)
 - [ResourceCollaboratorCreation](docs/ResourceCollaboratorCreation.md)
 - [ResourceRights](docs/ResourceRights.md)
 - [ResourceSharingKey](docs/ResourceSharingKey.md)
 - [ScoreComment](docs/ScoreComment.md)
 - [ScoreCommentContext](docs/ScoreCommentContext.md)
 - [ScoreCommentCreation](docs/ScoreCommentCreation.md)
 - [ScoreCommentUpdate](docs/ScoreCommentUpdate.md)
 - [ScoreCommentsCounts](docs/ScoreCommentsCounts.md)
 - [ScoreCreation](docs/ScoreCreation.md)
 - [ScoreCreationType](docs/ScoreCreationType.md)
 - [ScoreData](docs/ScoreData.md)
 - [ScoreDataEncoding](docs/ScoreDataEncoding.md)
 - [ScoreFork](docs/ScoreFork.md)
 - [ScoreLicense](docs/ScoreLicense.md)
 - [ScoreLikesCounts](docs/ScoreLikesCounts.md)
 - [ScoreModification](docs/ScoreModification.md)
 - [ScorePrivacy](docs/ScorePrivacy.md)
 - [ScoreRevision](docs/ScoreRevision.md)
 - [ScoreRevisionCreation](docs/ScoreRevisionCreation.md)
 - [ScoreRevisionStatistics](docs/ScoreRevisionStatistics.md)
 - [ScoreSource](docs/ScoreSource.md)
 - [ScoreSummary](docs/ScoreSummary.md)
 - [ScoreTrack](docs/ScoreTrack.md)
 - [ScoreTrackCreation](docs/ScoreTrackCreation.md)
 - [ScoreTrackPoint](docs/ScoreTrackPoint.md)
 - [ScoreTrackState](docs/ScoreTrackState.md)
 - [ScoreTrackType](docs/ScoreTrackType.md)
 - [ScoreTrackUpdate](docs/ScoreTrackUpdate.md)
 - [ScoreViewsCounts](docs/ScoreViewsCounts.md)
 - [UserAdminUpdate](docs/UserAdminUpdate.md)
 - [UserBasics](docs/UserBasics.md)
 - [UserCreation](docs/UserCreation.md)
 - [UserDetailsAdminLicense](docs/UserDetailsAdminLicense.md)
 - [UserInstruments](docs/UserInstruments.md)
 - [ResourceCollaborator](docs/ResourceCollaborator.md)
 - [ScoreDetails](docs/ScoreDetails.md)
 - [UserPublicSummary](docs/UserPublicSummary.md)
 - [UserDetailsAdmin](docs/UserDetailsAdmin.md)
 - [UserPublic](docs/UserPublic.md)
 - [UserDetails](docs/UserDetails.md)


## Documentation For Authorization


## OAuth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://flat.io/auth/oauth
- **Scopes**: 
 - **account.public_profile**: Provides access to the basic person's public profile. Education profiles may be anonymized with this scope, you can request the scope `education_profile` to access to the a basic education account profile. 
 - **account.education_profile**: Provides access to the basic person's education profile and public organization information. 
 - **scores.readonly**: Allows read-only access to all a user's scores. You won't need this scope to read public scores. 
 - **scores.social**: Allow to post comments and like scores 
 - **scores**: Full, permissive scope to access all of a user's scores. 
 - **collections.readonly**: Allow read-only access to a user's collections.
 - **collections.add_scores**: Allow to add scores to a user's collections.
 - **collections**: Full, permissive scope to access all of a user's collections.
 - **edu.classes**: Full, permissive scope to manage the classes.
 - **edu.classes.readonly**: Read-only access to the classes.
 - **edu.assignments**: Read-write access to the assignments and submissions.
 - **edu.assignments.readonly**: Read-only access to the assignments and submissions.
 - **edu.admin**: Full, permissive scope to manage all the admin of an organization.
 - **edu.admin.lti**: Access and manage the LTI Credentials for an organization.
 - **edu.admin.lti.readonly**: Read-only access to the LTI Credentials of an organization.
 - **edu.admin.users**: Access and manage the users and invitations of the organization.
 - **edu.admin.users.readonly**: Read-only access to the users and invitations of the organization.


## Author

developers@flat.io

