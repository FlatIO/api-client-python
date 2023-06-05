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
from flat_api.apis.tags import account_api
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
    host = "https://api.flat.io/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with flat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    only_id = False # bool | Only return the user id (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='onlyId', paramName='only_id', dataType='bool', datatypeWithEnum='null', dataFormat='null', collectionFormat='null', description='Only return the user id', unescapedDescription='Only return the user id', baseType='null', defaultValue='False', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='False', jsonSchema='{
  "name" : "onlyId",
  "in" : "query",
  "description" : "Only return the user id",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "type" : "boolean",
    "default" : false
  }
}', isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=true, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=false, isEnumRef=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, isVoid=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='boolean', baseName='OnlyIdSchema', complexType='null', getter='getOnlyId', setter='setOnlyId', description='null', dataType='bool', datatypeWithEnum='bool', dataFormat='null', name='only_id', min='null', max='null', defaultValue='False', defaultValueWithParam=' = data.onlyId;', baseType='bool', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='False', jsonSchema='{
  "type" : "boolean",
  "default" : false
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=true, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isPassword=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=false, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, isOverridden=null, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='OnlyId', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, isVoid=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})

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
*AccountApi* | [**get_authenticated_user**](docs/apis/tags/AccountApi.md#get_authenticated_user) | **get** /me | Get current user account
*ModelClassApi* | [**activate_class**](docs/apis/tags/ModelClassApi.md#activate_class) | **post** /classes/{class}/activate | Activate the class
*ModelClassApi* | [**add_class_user**](docs/apis/tags/ModelClassApi.md#add_class_user) | **put** /classes/{class}/users/{user} | Add a user to the class
*ModelClassApi* | [**archive_assignment**](docs/apis/tags/ModelClassApi.md#archive_assignment) | **post** /classes/{class}/assignments/{assignment}/archive | Archive the assignment
*ModelClassApi* | [**archive_class**](docs/apis/tags/ModelClassApi.md#archive_class) | **post** /classes/{class}/archive | Archive the class
*ModelClassApi* | [**copy_assignment**](docs/apis/tags/ModelClassApi.md#copy_assignment) | **post** /classes/{class}/assignments/{assignment}/copy | Copy an assignment
*ModelClassApi* | [**create_class**](docs/apis/tags/ModelClassApi.md#create_class) | **post** /classes | Create a new class
*ModelClassApi* | [**create_class_assignment**](docs/apis/tags/ModelClassApi.md#create_class_assignment) | **post** /classes/{class}/assignments | Assignment creation
*ModelClassApi* | [**create_submission**](docs/apis/tags/ModelClassApi.md#create_submission) | **put** /classes/{class}/assignments/{assignment}/submissions | Create or edit a submission
*ModelClassApi* | [**create_test_student_account**](docs/apis/tags/ModelClassApi.md#create_test_student_account) | **post** /classes/{class}/testStudent | Create a test student account
*ModelClassApi* | [**delete_class_user**](docs/apis/tags/ModelClassApi.md#delete_class_user) | **delete** /classes/{class}/users/{user} | Remove a user from the class
*ModelClassApi* | [**delete_submission**](docs/apis/tags/ModelClassApi.md#delete_submission) | **delete** /classes/{class}/assignments/{assignment}/submissions/{submission} | Reset a submission
*ModelClassApi* | [**delete_submission_comment**](docs/apis/tags/ModelClassApi.md#delete_submission_comment) | **delete** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Delete a feedback comment to a submission
*ModelClassApi* | [**edit_submission**](docs/apis/tags/ModelClassApi.md#edit_submission) | **put** /classes/{class}/assignments/{assignment}/submissions/{submission} | Edit a submission
*ModelClassApi* | [**enroll_class**](docs/apis/tags/ModelClassApi.md#enroll_class) | **post** /classes/enroll/{enrollmentCode} | Join a class
*ModelClassApi* | [**export_submissions_reviews_as_csv**](docs/apis/tags/ModelClassApi.md#export_submissions_reviews_as_csv) | **get** /classes/{class}/assignments/{assignment}/submissions/csv | CSV Grades exports
*ModelClassApi* | [**export_submissions_reviews_as_excel**](docs/apis/tags/ModelClassApi.md#export_submissions_reviews_as_excel) | **get** /classes/{class}/assignments/{assignment}/submissions/excel | Excel Grades exports
*ModelClassApi* | [**get_class**](docs/apis/tags/ModelClassApi.md#get_class) | **get** /classes/{class} | Get the details of a single class
*ModelClassApi* | [**get_score_submissions**](docs/apis/tags/ModelClassApi.md#get_score_submissions) | **get** /scores/{score}/submissions | List submissions related to the score
*ModelClassApi* | [**get_submission**](docs/apis/tags/ModelClassApi.md#get_submission) | **get** /classes/{class}/assignments/{assignment}/submissions/{submission} | Get a student submission
*ModelClassApi* | [**get_submission_comments**](docs/apis/tags/ModelClassApi.md#get_submission_comments) | **get** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | List the feedback comments of a submission
*ModelClassApi* | [**get_submission_history**](docs/apis/tags/ModelClassApi.md#get_submission_history) | **get** /classes/{class}/assignments/{assignment}/submissions/{submission}/history | Get the history of the submission
*ModelClassApi* | [**get_submissions**](docs/apis/tags/ModelClassApi.md#get_submissions) | **get** /classes/{class}/assignments/{assignment}/submissions | List the students&#x27; submissions
*ModelClassApi* | [**list_assignments**](docs/apis/tags/ModelClassApi.md#list_assignments) | **get** /classes/{class}/assignments | Assignments listing
*ModelClassApi* | [**list_class_student_submissions**](docs/apis/tags/ModelClassApi.md#list_class_student_submissions) | **get** /classes/{class}/students/{user}/submissions | List the submissions for a student
*ModelClassApi* | [**list_classes**](docs/apis/tags/ModelClassApi.md#list_classes) | **get** /classes | List the classes available for the current user
*ModelClassApi* | [**post_submission_comment**](docs/apis/tags/ModelClassApi.md#post_submission_comment) | **post** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | Add a feedback comment to a submission
*ModelClassApi* | [**unarchive_assignment**](docs/apis/tags/ModelClassApi.md#unarchive_assignment) | **delete** /classes/{class}/assignments/{assignment}/archive | Unarchive the assignment.
*ModelClassApi* | [**unarchive_class**](docs/apis/tags/ModelClassApi.md#unarchive_class) | **delete** /classes/{class}/archive | Unarchive the class
*ModelClassApi* | [**update_class**](docs/apis/tags/ModelClassApi.md#update_class) | **put** /classes/{class} | Update the class
*ModelClassApi* | [**update_submission_comment**](docs/apis/tags/ModelClassApi.md#update_submission_comment) | **put** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Update a feedback comment to a submission
*CollectionApi* | [**add_score_to_collection**](docs/apis/tags/CollectionApi.md#add_score_to_collection) | **put** /collections/{collection}/scores/{score} | Add a score to the collection
*CollectionApi* | [**create_collection**](docs/apis/tags/CollectionApi.md#create_collection) | **post** /collections | Create a new collection
*CollectionApi* | [**delete_collection**](docs/apis/tags/CollectionApi.md#delete_collection) | **delete** /collections/{collection} | Delete the collection
*CollectionApi* | [**delete_score_from_collection**](docs/apis/tags/CollectionApi.md#delete_score_from_collection) | **delete** /collections/{collection}/scores/{score} | Delete a score from the collection
*CollectionApi* | [**edit_collection**](docs/apis/tags/CollectionApi.md#edit_collection) | **put** /collections/{collection} | Update a collection&#x27;s metadata
*CollectionApi* | [**get_collection**](docs/apis/tags/CollectionApi.md#get_collection) | **get** /collections/{collection} | Get collection details
*CollectionApi* | [**list_collection_scores**](docs/apis/tags/CollectionApi.md#list_collection_scores) | **get** /collections/{collection}/scores | List the scores contained in a collection
*CollectionApi* | [**list_collections**](docs/apis/tags/CollectionApi.md#list_collections) | **get** /collections | List the collections
*CollectionApi* | [**untrash_collection**](docs/apis/tags/CollectionApi.md#untrash_collection) | **post** /collections/{collection}/untrash | Untrash a collection
*EduResourcesApi* | [**copy_edu_resource**](docs/apis/tags/EduResourcesApi.md#copy_edu_resource) | **post** /eduResources/{resource}/copy | Copy an education resource to a Resource Library
*EduResourcesApi* | [**copy_edu_resource_to_demo_class**](docs/apis/tags/EduResourcesApi.md#copy_edu_resource_to_demo_class) | **post** /eduResources/{resource}/copyToDemoClass | Copy an education assignment to a teacher demo class
*EduResourcesApi* | [**create_edu_resource**](docs/apis/tags/EduResourcesApi.md#create_edu_resource) | **post** /eduResources | Create a new education resource
*EduResourcesApi* | [**delete_edu_resource**](docs/apis/tags/EduResourcesApi.md#delete_edu_resource) | **delete** /eduResources/{resource} | Delete an education resource
*EduResourcesApi* | [**get_edu_resource**](docs/apis/tags/EduResourcesApi.md#get_edu_resource) | **get** /eduResources/{resource} | Get an education resource
*EduResourcesApi* | [**list_edu_libraries**](docs/apis/tags/EduResourcesApi.md#list_edu_libraries) | **get** /eduResources/libraries | List the education libraries
*EduResourcesApi* | [**list_edu_resources**](docs/apis/tags/EduResourcesApi.md#list_edu_resources) | **get** /eduResources | List education resources in a library or folder
*EduResourcesApi* | [**move_edu_resource**](docs/apis/tags/EduResourcesApi.md#move_edu_resource) | **post** /eduResources/{resource}/move | Move an education resource
*EduResourcesApi* | [**update_edu_resource**](docs/apis/tags/EduResourcesApi.md#update_edu_resource) | **put** /eduResources/{resource} | Update an education resource metadata
*EduResourcesApi* | [**update_edu_resource_assignment**](docs/apis/tags/EduResourcesApi.md#update_edu_resource_assignment) | **put** /eduResources/{resource}/assignment | Update an education resource assignment
*EduResourcesApi* | [**use_edu_resource_in_class**](docs/apis/tags/EduResourcesApi.md#use_edu_resource_in_class) | **post** /eduResources/{resource}/useInClass | Use an education resource in a class
*GroupApi* | [**get_group_details**](docs/apis/tags/GroupApi.md#get_group_details) | **get** /groups/{group} | Get group information
*GroupApi* | [**get_group_scores**](docs/apis/tags/GroupApi.md#get_group_scores) | **get** /groups/{group}/scores | List group&#x27;s scores
*GroupApi* | [**list_group_users**](docs/apis/tags/GroupApi.md#list_group_users) | **get** /groups/{group}/users | List group&#x27;s users
*OrganizationApi* | [**count_orga_users**](docs/apis/tags/OrganizationApi.md#count_orga_users) | **get** /organizations/users/count | Count the organization users using the provided filters
*OrganizationApi* | [**create_lti_credentials**](docs/apis/tags/OrganizationApi.md#create_lti_credentials) | **post** /organizations/lti/credentials | Create a new couple of LTI 1.x credentials
*OrganizationApi* | [**create_organization_invitation**](docs/apis/tags/OrganizationApi.md#create_organization_invitation) | **post** /organizations/invitations | Create a new invitation to join the organization
*OrganizationApi* | [**create_organization_user**](docs/apis/tags/OrganizationApi.md#create_organization_user) | **post** /organizations/users | Create a new user account
*OrganizationApi* | [**create_organization_user_access_token**](docs/apis/tags/OrganizationApi.md#create_organization_user_access_token) | **post** /organizations/users/{user}/accessToken | Create a delegated API access token for an organization user
*OrganizationApi* | [**create_organization_user_signin_link**](docs/apis/tags/OrganizationApi.md#create_organization_user_signin_link) | **post** /organizations/users/{user}/signinLink | Create a sign in link for an organization user
*OrganizationApi* | [**list_lti_credentials**](docs/apis/tags/OrganizationApi.md#list_lti_credentials) | **get** /organizations/lti/credentials | List LTI 1.x credentials
*OrganizationApi* | [**list_organization_invitations**](docs/apis/tags/OrganizationApi.md#list_organization_invitations) | **get** /organizations/invitations | List the organization invitations
*OrganizationApi* | [**list_organization_users**](docs/apis/tags/OrganizationApi.md#list_organization_users) | **get** /organizations/users | List the organization users
*OrganizationApi* | [**remove_organization_invitation**](docs/apis/tags/OrganizationApi.md#remove_organization_invitation) | **delete** /organizations/invitations/{invitation} | Remove an organization invitation
*OrganizationApi* | [**remove_organization_user**](docs/apis/tags/OrganizationApi.md#remove_organization_user) | **delete** /organizations/users/{user} | Remove an account from Flat
*OrganizationApi* | [**revoke_lti_credentials**](docs/apis/tags/OrganizationApi.md#revoke_lti_credentials) | **delete** /organizations/lti/credentials/{credentials} | Revoke LTI 1.x credentials
*OrganizationApi* | [**update_organization_user**](docs/apis/tags/OrganizationApi.md#update_organization_user) | **put** /organizations/users/{user} | Update account information
*ScoreApi* | [**add_score_collaborator**](docs/apis/tags/ScoreApi.md#add_score_collaborator) | **post** /scores/{score}/collaborators | Add a new collaborator
*ScoreApi* | [**add_score_track**](docs/apis/tags/ScoreApi.md#add_score_track) | **post** /scores/{score}/tracks | Add a new video or audio track to the score
*ScoreApi* | [**create_export_task**](docs/apis/tags/ScoreApi.md#create_export_task) | **post** /scores/{score}/revisions/{revision}/{format}/task | Create a new score export task
*ScoreApi* | [**create_score**](docs/apis/tags/ScoreApi.md#create_score) | **post** /scores | Create a new score
*ScoreApi* | [**create_score_revision**](docs/apis/tags/ScoreApi.md#create_score_revision) | **post** /scores/{score}/revisions | Create a new revision
*ScoreApi* | [**delete_score**](docs/apis/tags/ScoreApi.md#delete_score) | **delete** /scores/{score} | Delete a score
*ScoreApi* | [**delete_score_comment**](docs/apis/tags/ScoreApi.md#delete_score_comment) | **delete** /scores/{score}/comments/{comment} | Delete a comment
*ScoreApi* | [**delete_score_track**](docs/apis/tags/ScoreApi.md#delete_score_track) | **delete** /scores/{score}/tracks/{track} | Remove an audio or video track linked to the score
*ScoreApi* | [**edit_score**](docs/apis/tags/ScoreApi.md#edit_score) | **put** /scores/{score} | Edit a score&#x27;s metadata
*ScoreApi* | [**fork_score**](docs/apis/tags/ScoreApi.md#fork_score) | **post** /scores/{score}/fork | Fork a score
*ScoreApi* | [**ger_user_likes**](docs/apis/tags/ScoreApi.md#ger_user_likes) | **get** /users/{user}/likes | List liked scores
*ScoreApi* | [**get_group_scores**](docs/apis/tags/ScoreApi.md#get_group_scores) | **get** /groups/{group}/scores | List group&#x27;s scores
*ScoreApi* | [**get_score**](docs/apis/tags/ScoreApi.md#get_score) | **get** /scores/{score} | Get a score&#x27;s metadata
*ScoreApi* | [**get_score_collaborator**](docs/apis/tags/ScoreApi.md#get_score_collaborator) | **get** /scores/{score}/collaborators/{collaborator} | Get a collaborator
*ScoreApi* | [**get_score_collaborators**](docs/apis/tags/ScoreApi.md#get_score_collaborators) | **get** /scores/{score}/collaborators | List the collaborators
*ScoreApi* | [**get_score_comments**](docs/apis/tags/ScoreApi.md#get_score_comments) | **get** /scores/{score}/comments | List comments
*ScoreApi* | [**get_score_revision**](docs/apis/tags/ScoreApi.md#get_score_revision) | **get** /scores/{score}/revisions/{revision} | Get a score revision
*ScoreApi* | [**get_score_revision_data**](docs/apis/tags/ScoreApi.md#get_score_revision_data) | **get** /scores/{score}/revisions/{revision}/{format} | Get a score revision data
*ScoreApi* | [**get_score_revisions**](docs/apis/tags/ScoreApi.md#get_score_revisions) | **get** /scores/{score}/revisions | List the revisions
*ScoreApi* | [**get_score_submissions**](docs/apis/tags/ScoreApi.md#get_score_submissions) | **get** /scores/{score}/submissions | List submissions related to the score
*ScoreApi* | [**get_score_track**](docs/apis/tags/ScoreApi.md#get_score_track) | **get** /scores/{score}/tracks/{track} | Retrieve the details of an audio or video track linked to a score
*ScoreApi* | [**get_user_scores**](docs/apis/tags/ScoreApi.md#get_user_scores) | **get** /users/{user}/scores | List user&#x27;s scores
*ScoreApi* | [**list_score_tracks**](docs/apis/tags/ScoreApi.md#list_score_tracks) | **get** /scores/{score}/tracks | List the audio or video tracks linked to a score
*ScoreApi* | [**mark_score_comment_resolved**](docs/apis/tags/ScoreApi.md#mark_score_comment_resolved) | **put** /scores/{score}/comments/{comment}/resolved | Mark the comment as resolved
*ScoreApi* | [**mark_score_comment_unresolved**](docs/apis/tags/ScoreApi.md#mark_score_comment_unresolved) | **delete** /scores/{score}/comments/{comment}/resolved | Mark the comment as unresolved
*ScoreApi* | [**post_score_comment**](docs/apis/tags/ScoreApi.md#post_score_comment) | **post** /scores/{score}/comments | Post a new comment
*ScoreApi* | [**remove_score_collaborator**](docs/apis/tags/ScoreApi.md#remove_score_collaborator) | **delete** /scores/{score}/collaborators/{collaborator} | Delete a collaborator
*ScoreApi* | [**untrash_score**](docs/apis/tags/ScoreApi.md#untrash_score) | **post** /scores/{score}/untrash | Untrash a score
*ScoreApi* | [**update_score_comment**](docs/apis/tags/ScoreApi.md#update_score_comment) | **put** /scores/{score}/comments/{comment} | Update an existing comment
*ScoreApi* | [**update_score_track**](docs/apis/tags/ScoreApi.md#update_score_track) | **put** /scores/{score}/tracks/{track} | Update an audio or video track linked to a score
*TaskApi* | [**get_task**](docs/apis/tags/TaskApi.md#get_task) | **get** /tasks/{task} | Get a task details
*UserApi* | [**ger_user_likes**](docs/apis/tags/UserApi.md#ger_user_likes) | **get** /users/{user}/likes | List liked scores
*UserApi* | [**get_user**](docs/apis/tags/UserApi.md#get_user) | **get** /users/{user} | Get a public user profile
*UserApi* | [**get_user_scores**](docs/apis/tags/UserApi.md#get_user_scores) | **get** /users/{user}/scores | List user&#x27;s scores

## Documentation For Models

 - [ApiAccessToken](docs/models/ApiAccessToken.md)
 - [AppScopes](docs/models/AppScopes.md)
 - [Assignment](docs/models/Assignment.md)
 - [AssignmentCopy](docs/models/AssignmentCopy.md)
 - [AssignmentCopyResponse](docs/models/AssignmentCopyResponse.md)
 - [AssignmentSubmission](docs/models/AssignmentSubmission.md)
 - [AssignmentSubmissionComment](docs/models/AssignmentSubmissionComment.md)
 - [AssignmentSubmissionCommentCreation](docs/models/AssignmentSubmissionCommentCreation.md)
 - [AssignmentSubmissionHistory](docs/models/AssignmentSubmissionHistory.md)
 - [AssignmentSubmissionHistoryState](docs/models/AssignmentSubmissionHistoryState.md)
 - [AssignmentSubmissionState](docs/models/AssignmentSubmissionState.md)
 - [AssignmentSubmissionUpdate](docs/models/AssignmentSubmissionUpdate.md)
 - [AssignmentType](docs/models/AssignmentType.md)
 - [AssignmentUpdate](docs/models/AssignmentUpdate.md)
 - [ClassAssignment](docs/models/ClassAssignment.md)
 - [ClassAssignmentUpdate](docs/models/ClassAssignmentUpdate.md)
 - [ClassAttachmentCreation](docs/models/ClassAttachmentCreation.md)
 - [ClassCreation](docs/models/ClassCreation.md)
 - [ClassDetails](docs/models/ClassDetails.md)
 - [ClassGradeLevel](docs/models/ClassGradeLevel.md)
 - [ClassRoles](docs/models/ClassRoles.md)
 - [ClassState](docs/models/ClassState.md)
 - [ClassUpdate](docs/models/ClassUpdate.md)
 - [Collection](docs/models/Collection.md)
 - [CollectionApp](docs/models/CollectionApp.md)
 - [CollectionCreation](docs/models/CollectionCreation.md)
 - [CollectionModification](docs/models/CollectionModification.md)
 - [CollectionPrivacy](docs/models/CollectionPrivacy.md)
 - [CollectionType](docs/models/CollectionType.md)
 - [EduLibrary](docs/models/EduLibrary.md)
 - [EduResource](docs/models/EduResource.md)
 - [EduResourceCopy](docs/models/EduResourceCopy.md)
 - [EduResourceCreation](docs/models/EduResourceCreation.md)
 - [EduResourceMove](docs/models/EduResourceMove.md)
 - [EduResourcePrivacy](docs/models/EduResourcePrivacy.md)
 - [EduResourceType](docs/models/EduResourceType.md)
 - [EduResourceUpdate](docs/models/EduResourceUpdate.md)
 - [EduResourceUseInClass](docs/models/EduResourceUseInClass.md)
 - [EduSkillsFocused](docs/models/EduSkillsFocused.md)
 - [FlatErrorResponse](docs/models/FlatErrorResponse.md)
 - [FlatLocales](docs/models/FlatLocales.md)
 - [GoogleClassroomCoursework](docs/models/GoogleClassroomCoursework.md)
 - [GoogleClassroomSubmission](docs/models/GoogleClassroomSubmission.md)
 - [Group](docs/models/Group.md)
 - [GroupDetails](docs/models/GroupDetails.md)
 - [GroupType](docs/models/GroupType.md)
 - [LicenseMode](docs/models/LicenseMode.md)
 - [LicenseSources](docs/models/LicenseSources.md)
 - [LmsName](docs/models/LmsName.md)
 - [LtiCredentials](docs/models/LtiCredentials.md)
 - [LtiCredentialsCreation](docs/models/LtiCredentialsCreation.md)
 - [MediaAttachment](docs/models/MediaAttachment.md)
 - [MediaScoreSharingMode](docs/models/MediaScoreSharingMode.md)
 - [MicrosoftGraphAssignment](docs/models/MicrosoftGraphAssignment.md)
 - [MicrosoftGraphSubmission](docs/models/MicrosoftGraphSubmission.md)
 - [OrganizationInvitation](docs/models/OrganizationInvitation.md)
 - [OrganizationInvitationCreation](docs/models/OrganizationInvitationCreation.md)
 - [OrganizationRoles](docs/models/OrganizationRoles.md)
 - [OrganizationUserAccessTokenCreation](docs/models/OrganizationUserAccessTokenCreation.md)
 - [ResourceCollaborator](docs/models/ResourceCollaborator.md)
 - [ResourceCollaboratorCreation](docs/models/ResourceCollaboratorCreation.md)
 - [ResourceRights](docs/models/ResourceRights.md)
 - [ScoreComment](docs/models/ScoreComment.md)
 - [ScoreCommentContext](docs/models/ScoreCommentContext.md)
 - [ScoreCommentCreation](docs/models/ScoreCommentCreation.md)
 - [ScoreCommentUpdate](docs/models/ScoreCommentUpdate.md)
 - [ScoreCommentsCounts](docs/models/ScoreCommentsCounts.md)
 - [ScoreCreation](docs/models/ScoreCreation.md)
 - [ScoreCreationType](docs/models/ScoreCreationType.md)
 - [ScoreDetails](docs/models/ScoreDetails.md)
 - [ScoreFork](docs/models/ScoreFork.md)
 - [ScoreLicense](docs/models/ScoreLicense.md)
 - [ScoreLikesCounts](docs/models/ScoreLikesCounts.md)
 - [ScoreModification](docs/models/ScoreModification.md)
 - [ScorePlaysCounts](docs/models/ScorePlaysCounts.md)
 - [ScorePrivacy](docs/models/ScorePrivacy.md)
 - [ScoreRevision](docs/models/ScoreRevision.md)
 - [ScoreRevisionCreation](docs/models/ScoreRevisionCreation.md)
 - [ScoreRevisionStatistics](docs/models/ScoreRevisionStatistics.md)
 - [ScoreSource](docs/models/ScoreSource.md)
 - [ScoreTrack](docs/models/ScoreTrack.md)
 - [ScoreTrackCreation](docs/models/ScoreTrackCreation.md)
 - [ScoreTrackPoint](docs/models/ScoreTrackPoint.md)
 - [ScoreTrackState](docs/models/ScoreTrackState.md)
 - [ScoreTrackType](docs/models/ScoreTrackType.md)
 - [ScoreTrackUpdate](docs/models/ScoreTrackUpdate.md)
 - [ScoreViewsCounts](docs/models/ScoreViewsCounts.md)
 - [Task](docs/models/Task.md)
 - [TaskExportOptions](docs/models/TaskExportOptions.md)
 - [UserAdminUpdate](docs/models/UserAdminUpdate.md)
 - [UserAzureDetails](docs/models/UserAzureDetails.md)
 - [UserCommunityProfileLinks](docs/models/UserCommunityProfileLinks.md)
 - [UserCreation](docs/models/UserCreation.md)
 - [UserDetails](docs/models/UserDetails.md)
 - [UserDetailsAdmin](docs/models/UserDetailsAdmin.md)
 - [UserPublic](docs/models/UserPublic.md)
 - [UserPublicSummary](docs/models/UserPublicSummary.md)
 - [UserSigninLink](docs/models/UserSigninLink.md)
 - [UserSigninLinkCreation](docs/models/UserSigninLinkCreation.md)

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="OAuth2"></a>
### OAuth2

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
developers@flat.io
developers@flat.io
developers@flat.io
developers@flat.io
developers@flat.io
developers@flat.io
developers@flat.io
developers@flat.io

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in flat_api.apis and flat_api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from flat_api.apis.default_api import DefaultApi`
- `from flat_api.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import flat_api
from flat_api.apis import *
from flat_api.models import *
```
