# Python Client for the Flat REST API

[![Python package](https://github.com/FlatIO/api-client-python/actions/workflows/python-package.yml/badge.svg)](https://github.com/FlatIO/api-client-python/actions/workflows/python-package.yml)

The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:
- Creating and importing new music scores using MusicXML or MIDI files
- Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI)
- Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.

You can find the API reference including code samples and our OpenAPI Specification at the following url: [https://flat.io/developers/api/reference](https://flat.io/developers/api/reference).

To request some API credentials, please visit [https://flat.io/developers](https://flat.io/developers).

## Requirements.

Python >= 3.7

## Installation & Usage
### pip install

```sh
pip install flat_api
```

or install from this repository

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

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import flat_api
from pprint import pprint
from flat_api.api import account_api
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.user_details import UserDetails
# Defining the host is optional and defaults to https://api.flat.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = flat_api.Configuration(
    host = "https://api.flat.io/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    only_id = False # bool | Only return the user id (optional) (default to False)

    try:
        # Get current user account
        api_response = api_instance.get_authenticated_user(only_id=only_id)
        pprint(api_response)
    except flat_api.ApiException as e:
        print("Exception when calling AccountApi->get_authenticated_user: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.flat.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**get_authenticated_user**](docs/AccountApi.md#get_authenticated_user) | **GET** /me | Get current user account
*ClassApi* | [**activate_class**](docs/ClassApi.md#activate_class) | **POST** /classes/{class}/activate | Activate the class
*ClassApi* | [**add_class_user**](docs/ClassApi.md#add_class_user) | **PUT** /classes/{class}/users/{user} | Add a user to the class
*ClassApi* | [**archive_assignment**](docs/ClassApi.md#archive_assignment) | **POST** /classes/{class}/assignments/{assignment}/archive | Archive the assignment
*ClassApi* | [**archive_class**](docs/ClassApi.md#archive_class) | **POST** /classes/{class}/archive | Archive the class
*ClassApi* | [**copy_assignment**](docs/ClassApi.md#copy_assignment) | **POST** /classes/{class}/assignments/{assignment}/copy | Copy an assignment
*ClassApi* | [**create_class**](docs/ClassApi.md#create_class) | **POST** /classes | Create a new class
*ClassApi* | [**create_class_assignment**](docs/ClassApi.md#create_class_assignment) | **POST** /classes/{class}/assignments | Assignment creation
*ClassApi* | [**create_submission**](docs/ClassApi.md#create_submission) | **PUT** /classes/{class}/assignments/{assignment}/submissions | Create or edit a submission
*ClassApi* | [**create_test_student_account**](docs/ClassApi.md#create_test_student_account) | **POST** /classes/{class}/testStudent | Create a test student account
*ClassApi* | [**delete_class_user**](docs/ClassApi.md#delete_class_user) | **DELETE** /classes/{class}/users/{user} | Remove a user from the class
*ClassApi* | [**delete_submission**](docs/ClassApi.md#delete_submission) | **DELETE** /classes/{class}/assignments/{assignment}/submissions/{submission} | Reset a submission
*ClassApi* | [**delete_submission_comment**](docs/ClassApi.md#delete_submission_comment) | **DELETE** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Delete a feedback comment to a submission
*ClassApi* | [**edit_submission**](docs/ClassApi.md#edit_submission) | **PUT** /classes/{class}/assignments/{assignment}/submissions/{submission} | Edit a submission
*ClassApi* | [**enroll_class**](docs/ClassApi.md#enroll_class) | **POST** /classes/enroll/{enrollmentCode} | Join a class
*ClassApi* | [**export_submissions_reviews_as_csv**](docs/ClassApi.md#export_submissions_reviews_as_csv) | **GET** /classes/{class}/assignments/{assignment}/submissions/csv | CSV Grades exports
*ClassApi* | [**export_submissions_reviews_as_excel**](docs/ClassApi.md#export_submissions_reviews_as_excel) | **GET** /classes/{class}/assignments/{assignment}/submissions/excel | Excel Grades exports
*ClassApi* | [**get_class**](docs/ClassApi.md#get_class) | **GET** /classes/{class} | Get the details of a single class
*ClassApi* | [**get_score_submissions**](docs/ClassApi.md#get_score_submissions) | **GET** /scores/{score}/submissions | List submissions related to the score
*ClassApi* | [**get_submission**](docs/ClassApi.md#get_submission) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission} | Get a student submission
*ClassApi* | [**get_submission_comments**](docs/ClassApi.md#get_submission_comments) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | List the feedback comments of a submission
*ClassApi* | [**get_submission_history**](docs/ClassApi.md#get_submission_history) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission}/history | Get the history of the submission
*ClassApi* | [**get_submissions**](docs/ClassApi.md#get_submissions) | **GET** /classes/{class}/assignments/{assignment}/submissions | List the students&#39; submissions
*ClassApi* | [**list_assignments**](docs/ClassApi.md#list_assignments) | **GET** /classes/{class}/assignments | Assignments listing
*ClassApi* | [**list_class_student_submissions**](docs/ClassApi.md#list_class_student_submissions) | **GET** /classes/{class}/students/{user}/submissions | List the submissions for a student
*ClassApi* | [**list_classes**](docs/ClassApi.md#list_classes) | **GET** /classes | List the classes available for the current user
*ClassApi* | [**post_submission_comment**](docs/ClassApi.md#post_submission_comment) | **POST** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | Add a feedback comment to a submission
*ClassApi* | [**unarchive_assignment**](docs/ClassApi.md#unarchive_assignment) | **DELETE** /classes/{class}/assignments/{assignment}/archive | Unarchive the assignment.
*ClassApi* | [**unarchive_class**](docs/ClassApi.md#unarchive_class) | **DELETE** /classes/{class}/archive | Unarchive the class
*ClassApi* | [**update_class**](docs/ClassApi.md#update_class) | **PUT** /classes/{class} | Update the class
*ClassApi* | [**update_submission_comment**](docs/ClassApi.md#update_submission_comment) | **PUT** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Update a feedback comment to a submission
*CollectionApi* | [**add_score_to_collection**](docs/CollectionApi.md#add_score_to_collection) | **PUT** /collections/{collection}/scores/{score} | Add a score to the collection
*CollectionApi* | [**create_collection**](docs/CollectionApi.md#create_collection) | **POST** /collections | Create a new collection
*CollectionApi* | [**delete_collection**](docs/CollectionApi.md#delete_collection) | **DELETE** /collections/{collection} | Delete the collection
*CollectionApi* | [**delete_score_from_collection**](docs/CollectionApi.md#delete_score_from_collection) | **DELETE** /collections/{collection}/scores/{score} | Delete a score from the collection
*CollectionApi* | [**edit_collection**](docs/CollectionApi.md#edit_collection) | **PUT** /collections/{collection} | Update a collection&#39;s metadata
*CollectionApi* | [**get_collection**](docs/CollectionApi.md#get_collection) | **GET** /collections/{collection} | Get collection details
*CollectionApi* | [**list_collection_scores**](docs/CollectionApi.md#list_collection_scores) | **GET** /collections/{collection}/scores | List the scores contained in a collection
*CollectionApi* | [**list_collections**](docs/CollectionApi.md#list_collections) | **GET** /collections | List the collections
*CollectionApi* | [**untrash_collection**](docs/CollectionApi.md#untrash_collection) | **POST** /collections/{collection}/untrash | Untrash a collection
*EduResourcesApi* | [**copy_edu_resource**](docs/EduResourcesApi.md#copy_edu_resource) | **POST** /eduResources/{resource}/copy | Copy an education resource to a Resource Library
*EduResourcesApi* | [**copy_edu_resource_to_demo_class**](docs/EduResourcesApi.md#copy_edu_resource_to_demo_class) | **POST** /eduResources/{resource}/copyToDemoClass | Copy an education assignment to a teacher demo class
*EduResourcesApi* | [**create_edu_resource**](docs/EduResourcesApi.md#create_edu_resource) | **POST** /eduResources | Create a new education resource
*EduResourcesApi* | [**delete_edu_resource**](docs/EduResourcesApi.md#delete_edu_resource) | **DELETE** /eduResources/{resource} | Delete an education resource
*EduResourcesApi* | [**get_edu_resource**](docs/EduResourcesApi.md#get_edu_resource) | **GET** /eduResources/{resource} | Get an education resource
*EduResourcesApi* | [**list_edu_libraries**](docs/EduResourcesApi.md#list_edu_libraries) | **GET** /eduResources/libraries | List the education libraries
*EduResourcesApi* | [**list_edu_resources**](docs/EduResourcesApi.md#list_edu_resources) | **GET** /eduResources | List education resources in a library or folder
*EduResourcesApi* | [**move_edu_resource**](docs/EduResourcesApi.md#move_edu_resource) | **POST** /eduResources/{resource}/move | Move an education resource
*EduResourcesApi* | [**update_edu_resource**](docs/EduResourcesApi.md#update_edu_resource) | **PUT** /eduResources/{resource} | Update an education resource metadata
*EduResourcesApi* | [**update_edu_resource_assignment**](docs/EduResourcesApi.md#update_edu_resource_assignment) | **PUT** /eduResources/{resource}/assignment | Update an education resource assignment
*EduResourcesApi* | [**use_edu_resource_in_class**](docs/EduResourcesApi.md#use_edu_resource_in_class) | **POST** /eduResources/{resource}/useInClass | Use an education resource in a class
*GroupApi* | [**get_group_details**](docs/GroupApi.md#get_group_details) | **GET** /groups/{group} | Get group information
*GroupApi* | [**get_group_scores**](docs/GroupApi.md#get_group_scores) | **GET** /groups/{group}/scores | List group&#39;s scores
*GroupApi* | [**list_group_users**](docs/GroupApi.md#list_group_users) | **GET** /groups/{group}/users | List group&#39;s users
*OrganizationApi* | [**count_orga_users**](docs/OrganizationApi.md#count_orga_users) | **GET** /organizations/users/count | Count the organization users using the provided filters
*OrganizationApi* | [**create_lti_credentials**](docs/OrganizationApi.md#create_lti_credentials) | **POST** /organizations/lti/credentials | Create a new couple of LTI 1.x credentials
*OrganizationApi* | [**create_organization_invitation**](docs/OrganizationApi.md#create_organization_invitation) | **POST** /organizations/invitations | Create a new invitation to join the organization
*OrganizationApi* | [**create_organization_user**](docs/OrganizationApi.md#create_organization_user) | **POST** /organizations/users | Create a new user account
*OrganizationApi* | [**create_organization_user_access_token**](docs/OrganizationApi.md#create_organization_user_access_token) | **POST** /organizations/users/{user}/accessToken | Create a delegated API access token for an organization user
*OrganizationApi* | [**create_organization_user_signin_link**](docs/OrganizationApi.md#create_organization_user_signin_link) | **POST** /organizations/users/{user}/signinLink | Create a sign in link for an organization user
*OrganizationApi* | [**list_lti_credentials**](docs/OrganizationApi.md#list_lti_credentials) | **GET** /organizations/lti/credentials | List LTI 1.x credentials
*OrganizationApi* | [**list_organization_invitations**](docs/OrganizationApi.md#list_organization_invitations) | **GET** /organizations/invitations | List the organization invitations
*OrganizationApi* | [**list_organization_users**](docs/OrganizationApi.md#list_organization_users) | **GET** /organizations/users | List the organization users
*OrganizationApi* | [**remove_organization_invitation**](docs/OrganizationApi.md#remove_organization_invitation) | **DELETE** /organizations/invitations/{invitation} | Remove an organization invitation
*OrganizationApi* | [**remove_organization_user**](docs/OrganizationApi.md#remove_organization_user) | **DELETE** /organizations/users/{user} | Remove an account from Flat
*OrganizationApi* | [**revoke_lti_credentials**](docs/OrganizationApi.md#revoke_lti_credentials) | **DELETE** /organizations/lti/credentials/{credentials} | Revoke LTI 1.x credentials
*OrganizationApi* | [**update_organization_user**](docs/OrganizationApi.md#update_organization_user) | **PUT** /organizations/users/{user} | Update account information
*ScoreApi* | [**add_score_collaborator**](docs/ScoreApi.md#add_score_collaborator) | **POST** /scores/{score}/collaborators | Add a new collaborator
*ScoreApi* | [**add_score_track**](docs/ScoreApi.md#add_score_track) | **POST** /scores/{score}/tracks | Add a new video or audio track to the score
*ScoreApi* | [**create_export_task**](docs/ScoreApi.md#create_export_task) | **POST** /scores/{score}/revisions/{revision}/{format}/task | Create a new score export task
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
*TaskApi* | [**get_task**](docs/TaskApi.md#get_task) | **GET** /tasks/{task} | Get a task details
*UserApi* | [**ger_user_likes**](docs/UserApi.md#ger_user_likes) | **GET** /users/{user}/likes | List liked scores
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /users/{user} | Get a public user profile
*UserApi* | [**get_user_scores**](docs/UserApi.md#get_user_scores) | **GET** /users/{user}/scores | List user&#39;s scores


## Documentation For Models

 - [ApiAccessToken](docs/ApiAccessToken.md)
 - [AppScopes](docs/AppScopes.md)
 - [Assignment](docs/Assignment.md)
 - [AssignmentCopy](docs/AssignmentCopy.md)
 - [AssignmentCopyResponse](docs/AssignmentCopyResponse.md)
 - [AssignmentCopyResponseCapabilities](docs/AssignmentCopyResponseCapabilities.md)
 - [AssignmentCopyResponseCapabilitiesCanPublishInClassError](docs/AssignmentCopyResponseCapabilitiesCanPublishInClassError.md)
 - [AssignmentSubmission](docs/AssignmentSubmission.md)
 - [AssignmentSubmissionComment](docs/AssignmentSubmissionComment.md)
 - [AssignmentSubmissionCommentCreation](docs/AssignmentSubmissionCommentCreation.md)
 - [AssignmentSubmissionHistory](docs/AssignmentSubmissionHistory.md)
 - [AssignmentSubmissionHistoryAttachment](docs/AssignmentSubmissionHistoryAttachment.md)
 - [AssignmentSubmissionHistoryState](docs/AssignmentSubmissionHistoryState.md)
 - [AssignmentSubmissionState](docs/AssignmentSubmissionState.md)
 - [AssignmentSubmissionUpdate](docs/AssignmentSubmissionUpdate.md)
 - [AssignmentSubmissionUpdateComments](docs/AssignmentSubmissionUpdateComments.md)
 - [AssignmentType](docs/AssignmentType.md)
 - [AssignmentUpdate](docs/AssignmentUpdate.md)
 - [ClassAssignment](docs/ClassAssignment.md)
 - [ClassAssignmentCanvas](docs/ClassAssignmentCanvas.md)
 - [ClassAssignmentLti](docs/ClassAssignmentLti.md)
 - [ClassAssignmentMfc](docs/ClassAssignmentMfc.md)
 - [ClassAssignmentUpdate](docs/ClassAssignmentUpdate.md)
 - [ClassAssignmentUpdateGoogleClassroom](docs/ClassAssignmentUpdateGoogleClassroom.md)
 - [ClassAssignmentUpdateMicrosoftGraph](docs/ClassAssignmentUpdateMicrosoftGraph.md)
 - [ClassAttachmentCreation](docs/ClassAttachmentCreation.md)
 - [ClassCreation](docs/ClassCreation.md)
 - [ClassDetails](docs/ClassDetails.md)
 - [ClassDetailsCanvas](docs/ClassDetailsCanvas.md)
 - [ClassDetailsClever](docs/ClassDetailsClever.md)
 - [ClassDetailsGoogleClassroom](docs/ClassDetailsGoogleClassroom.md)
 - [ClassDetailsGoogleDrive](docs/ClassDetailsGoogleDrive.md)
 - [ClassDetailsIssues](docs/ClassDetailsIssues.md)
 - [ClassDetailsIssuesSyncInner](docs/ClassDetailsIssuesSyncInner.md)
 - [ClassDetailsLti](docs/ClassDetailsLti.md)
 - [ClassDetailsMfc](docs/ClassDetailsMfc.md)
 - [ClassDetailsMicrosoftGraph](docs/ClassDetailsMicrosoftGraph.md)
 - [ClassGradeLevel](docs/ClassGradeLevel.md)
 - [ClassRoles](docs/ClassRoles.md)
 - [ClassState](docs/ClassState.md)
 - [ClassUpdate](docs/ClassUpdate.md)
 - [Collection](docs/Collection.md)
 - [CollectionApp](docs/CollectionApp.md)
 - [CollectionCapabilities](docs/CollectionCapabilities.md)
 - [CollectionCreation](docs/CollectionCreation.md)
 - [CollectionModification](docs/CollectionModification.md)
 - [CollectionPrivacy](docs/CollectionPrivacy.md)
 - [CollectionType](docs/CollectionType.md)
 - [EduLibrary](docs/EduLibrary.md)
 - [EduResource](docs/EduResource.md)
 - [EduResourceCapabilities](docs/EduResourceCapabilities.md)
 - [EduResourceCopy](docs/EduResourceCopy.md)
 - [EduResourceCreation](docs/EduResourceCreation.md)
 - [EduResourceMove](docs/EduResourceMove.md)
 - [EduResourcePrivacy](docs/EduResourcePrivacy.md)
 - [EduResourceResource](docs/EduResourceResource.md)
 - [EduResourceType](docs/EduResourceType.md)
 - [EduResourceUpdate](docs/EduResourceUpdate.md)
 - [EduResourceUseInClass](docs/EduResourceUseInClass.md)
 - [EduSkillsFocused](docs/EduSkillsFocused.md)
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
 - [MicrosoftGraphAssignment](docs/MicrosoftGraphAssignment.md)
 - [MicrosoftGraphSubmission](docs/MicrosoftGraphSubmission.md)
 - [OrganizationInvitation](docs/OrganizationInvitation.md)
 - [OrganizationInvitationCreation](docs/OrganizationInvitationCreation.md)
 - [OrganizationRoles](docs/OrganizationRoles.md)
 - [OrganizationUserAccessTokenCreation](docs/OrganizationUserAccessTokenCreation.md)
 - [ResourceCollaborator](docs/ResourceCollaborator.md)
 - [ResourceCollaboratorCreation](docs/ResourceCollaboratorCreation.md)
 - [ResourceRights](docs/ResourceRights.md)
 - [ScoreComment](docs/ScoreComment.md)
 - [ScoreCommentContext](docs/ScoreCommentContext.md)
 - [ScoreCommentCreation](docs/ScoreCommentCreation.md)
 - [ScoreCommentModeration](docs/ScoreCommentModeration.md)
 - [ScoreCommentUpdate](docs/ScoreCommentUpdate.md)
 - [ScoreCommentsCounts](docs/ScoreCommentsCounts.md)
 - [ScoreCreation](docs/ScoreCreation.md)
 - [ScoreCreationBuilderData](docs/ScoreCreationBuilderData.md)
 - [ScoreCreationBuilderDataLayoutData](docs/ScoreCreationBuilderDataLayoutData.md)
 - [ScoreCreationBuilderDataScoreData](docs/ScoreCreationBuilderDataScoreData.md)
 - [ScoreCreationBuilderDataScoreDataInstrumentsInner](docs/ScoreCreationBuilderDataScoreDataInstrumentsInner.md)
 - [ScoreCreationType](docs/ScoreCreationType.md)
 - [ScoreDetails](docs/ScoreDetails.md)
 - [ScoreFork](docs/ScoreFork.md)
 - [ScoreLicense](docs/ScoreLicense.md)
 - [ScoreLikesCounts](docs/ScoreLikesCounts.md)
 - [ScoreModification](docs/ScoreModification.md)
 - [ScorePlaysCounts](docs/ScorePlaysCounts.md)
 - [ScorePrivacy](docs/ScorePrivacy.md)
 - [ScoreRevision](docs/ScoreRevision.md)
 - [ScoreRevisionCreation](docs/ScoreRevisionCreation.md)
 - [ScoreRevisionStatistics](docs/ScoreRevisionStatistics.md)
 - [ScoreSource](docs/ScoreSource.md)
 - [ScoreTrack](docs/ScoreTrack.md)
 - [ScoreTrackCreation](docs/ScoreTrackCreation.md)
 - [ScoreTrackPoint](docs/ScoreTrackPoint.md)
 - [ScoreTrackState](docs/ScoreTrackState.md)
 - [ScoreTrackType](docs/ScoreTrackType.md)
 - [ScoreTrackUpdate](docs/ScoreTrackUpdate.md)
 - [ScoreViewsCounts](docs/ScoreViewsCounts.md)
 - [Task](docs/Task.md)
 - [TaskExportOptions](docs/TaskExportOptions.md)
 - [TaskProgress](docs/TaskProgress.md)
 - [TaskResult](docs/TaskResult.md)
 - [UserAdminUpdate](docs/UserAdminUpdate.md)
 - [UserAzureDetails](docs/UserAzureDetails.md)
 - [UserCommunityProfileLinks](docs/UserCommunityProfileLinks.md)
 - [UserCreation](docs/UserCreation.md)
 - [UserDetails](docs/UserDetails.md)
 - [UserDetailsAdmin](docs/UserDetailsAdmin.md)
 - [UserDetailsAdminLicense](docs/UserDetailsAdminLicense.md)
 - [UserPublic](docs/UserPublic.md)
 - [UserPublicSummary](docs/UserPublicSummary.md)
 - [UserSigninLink](docs/UserSigninLink.md)
 - [UserSigninLinkCreation](docs/UserSigninLinkCreation.md)


## Documentation For Authorization


## OAuth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://flat.io/auth/oauth
- **Scopes**: 
 - **account.public_profile**: Provides access to the basic person's public profile. Education profiles may be anonymized with this scope, you can request the scope `education_profile` to access to the a basic education account profile. 
 - **account.email**: Provices access to the person's email. 
 - **account.education_profile**: Provides access to the basic person's education profile and public organization information. 
 - **scores.readonly**: Allows read-only access to all a user's scores. You won't need this scope to read public scores. 
 - **scores.social**: Allow to post comments and like scores 
 - **scores**: Full, permissive scope to access all of a user's scores. 
 - **collections.readonly**: Allow read-only access to a user's collections.
 - **collections.add_scores**: Allow to add scores to a user's collections.
 - **collections**: Full, permissive scope to access all of a user's collections.
 - **edu.resources**: Read-write access to the resource library.
 - **edu.resources.readonly**: Read-only access to the resource library.
 - **edu.classes**: Full, permissive scope to manage the classes.
 - **edu.classes.readonly**: Read-only access to the classes.
 - **edu.assignments**: Read-write access to the assignments and submissions.
 - **edu.assignments.readonly**: Read-only access to the assignments and submissions.
 - **edu.admin**: Full, permissive scope to manage all the admin of an organization.
 - **edu.admin.lti**: Access and manage the LTI Credentials for an organization.
 - **edu.admin.lti.readonly**: Read-only access to the LTI Credentials of an organization.
 - **edu.admin.users**: Access and manage the users and invitations of the organization.
 - **edu.admin.users.readonly**: Read-only access to the users and invitations of the organization.
 - **tasks.readonly**: Read-only access to export tasks created by this account.


## Author

developers@flat.io


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in flat_api.apis and flat_api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from flat_api.api.default_api import DefaultApi`
- `from flat_api.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import flat_api
from flat_api.apis import *
from flat_api.models import *
```

