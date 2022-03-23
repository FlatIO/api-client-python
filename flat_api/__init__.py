# coding: utf-8

# flake8: noqa

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and introduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    The version of the OpenAPI document: 2.17.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.7.0"

# import apis into sdk package
from flat_api.api.account_api import AccountApi
from flat_api.api.class_api import ClassApi
from flat_api.api.collection_api import CollectionApi
from flat_api.api.group_api import GroupApi
from flat_api.api.organization_api import OrganizationApi
from flat_api.api.score_api import ScoreApi
from flat_api.api.task_api import TaskApi
from flat_api.api.user_api import UserApi

# import ApiClient
from flat_api.api_client import ApiClient
from flat_api.configuration import Configuration
from flat_api.exceptions import OpenApiException
from flat_api.exceptions import ApiTypeError
from flat_api.exceptions import ApiValueError
from flat_api.exceptions import ApiKeyError
from flat_api.exceptions import ApiException
# import models into sdk package
from flat_api.models.api_access_token import ApiAccessToken
from flat_api.models.app_scopes import AppScopes
from flat_api.models.assignment import Assignment
from flat_api.models.assignment_canvas import AssignmentCanvas
from flat_api.models.assignment_copy import AssignmentCopy
from flat_api.models.assignment_creation import AssignmentCreation
from flat_api.models.assignment_creation_google_classroom import AssignmentCreationGoogleClassroom
from flat_api.models.assignment_creation_microsoft_graph import AssignmentCreationMicrosoftGraph
from flat_api.models.assignment_lti import AssignmentLti
from flat_api.models.assignment_mfc import AssignmentMfc
from flat_api.models.assignment_submission import AssignmentSubmission
from flat_api.models.assignment_submission_comment import AssignmentSubmissionComment
from flat_api.models.assignment_submission_comment_creation import AssignmentSubmissionCommentCreation
from flat_api.models.assignment_submission_history import AssignmentSubmissionHistory
from flat_api.models.assignment_submission_history_attachment import AssignmentSubmissionHistoryAttachment
from flat_api.models.assignment_submission_state import AssignmentSubmissionState
from flat_api.models.assignment_submission_update import AssignmentSubmissionUpdate
from flat_api.models.assignment_submission_update_comments import AssignmentSubmissionUpdateComments
from flat_api.models.assignment_type import AssignmentType
from flat_api.models.class_attachment_creation import ClassAttachmentCreation
from flat_api.models.class_creation import ClassCreation
from flat_api.models.class_details import ClassDetails
from flat_api.models.class_details_canvas import ClassDetailsCanvas
from flat_api.models.class_details_clever import ClassDetailsClever
from flat_api.models.class_details_google_classroom import ClassDetailsGoogleClassroom
from flat_api.models.class_details_google_drive import ClassDetailsGoogleDrive
from flat_api.models.class_details_issues import ClassDetailsIssues
from flat_api.models.class_details_issues_sync import ClassDetailsIssuesSync
from flat_api.models.class_details_lti import ClassDetailsLti
from flat_api.models.class_details_mfc import ClassDetailsMfc
from flat_api.models.class_details_microsoft_graph import ClassDetailsMicrosoftGraph
from flat_api.models.class_roles import ClassRoles
from flat_api.models.class_state import ClassState
from flat_api.models.class_update import ClassUpdate
from flat_api.models.collection import Collection
from flat_api.models.collection_app import CollectionApp
from flat_api.models.collection_capabilities import CollectionCapabilities
from flat_api.models.collection_creation import CollectionCreation
from flat_api.models.collection_modification import CollectionModification
from flat_api.models.collection_privacy import CollectionPrivacy
from flat_api.models.collection_type import CollectionType
from flat_api.models.flat_error_response import FlatErrorResponse
from flat_api.models.flat_locales import FlatLocales
from flat_api.models.google_classroom_coursework import GoogleClassroomCoursework
from flat_api.models.google_classroom_submission import GoogleClassroomSubmission
from flat_api.models.group import Group
from flat_api.models.group_details import GroupDetails
from flat_api.models.group_type import GroupType
from flat_api.models.license_mode import LicenseMode
from flat_api.models.license_sources import LicenseSources
from flat_api.models.lms_name import LmsName
from flat_api.models.lti_credentials import LtiCredentials
from flat_api.models.lti_credentials_creation import LtiCredentialsCreation
from flat_api.models.media_attachment import MediaAttachment
from flat_api.models.media_score_sharing_mode import MediaScoreSharingMode
from flat_api.models.microsoft_graph_assignment import MicrosoftGraphAssignment
from flat_api.models.microsoft_graph_submission import MicrosoftGraphSubmission
from flat_api.models.organization_invitation import OrganizationInvitation
from flat_api.models.organization_invitation_creation import OrganizationInvitationCreation
from flat_api.models.organization_roles import OrganizationRoles
from flat_api.models.organization_user_access_token_creation import OrganizationUserAccessTokenCreation
from flat_api.models.organization_user_signin_link import OrganizationUserSigninLink
from flat_api.models.organization_user_signin_link_creation import OrganizationUserSigninLinkCreation
from flat_api.models.resource_collaborator import ResourceCollaborator
from flat_api.models.resource_collaborator_creation import ResourceCollaboratorCreation
from flat_api.models.resource_rights import ResourceRights
from flat_api.models.score_comment import ScoreComment
from flat_api.models.score_comment_context import ScoreCommentContext
from flat_api.models.score_comment_creation import ScoreCommentCreation
from flat_api.models.score_comment_moderation import ScoreCommentModeration
from flat_api.models.score_comment_update import ScoreCommentUpdate
from flat_api.models.score_comments_counts import ScoreCommentsCounts
from flat_api.models.score_creation import ScoreCreation
from flat_api.models.score_creation_builder_data import ScoreCreationBuilderData
from flat_api.models.score_creation_builder_data_layout_data import ScoreCreationBuilderDataLayoutData
from flat_api.models.score_creation_builder_data_score_data import ScoreCreationBuilderDataScoreData
from flat_api.models.score_creation_builder_data_score_data_instruments import ScoreCreationBuilderDataScoreDataInstruments
from flat_api.models.score_creation_type import ScoreCreationType
from flat_api.models.score_details import ScoreDetails
from flat_api.models.score_fork import ScoreFork
from flat_api.models.score_license import ScoreLicense
from flat_api.models.score_likes_counts import ScoreLikesCounts
from flat_api.models.score_modification import ScoreModification
from flat_api.models.score_plays_counts import ScorePlaysCounts
from flat_api.models.score_privacy import ScorePrivacy
from flat_api.models.score_revision import ScoreRevision
from flat_api.models.score_revision_creation import ScoreRevisionCreation
from flat_api.models.score_revision_statistics import ScoreRevisionStatistics
from flat_api.models.score_source import ScoreSource
from flat_api.models.score_track import ScoreTrack
from flat_api.models.score_track_creation import ScoreTrackCreation
from flat_api.models.score_track_point import ScoreTrackPoint
from flat_api.models.score_track_state import ScoreTrackState
from flat_api.models.score_track_type import ScoreTrackType
from flat_api.models.score_track_update import ScoreTrackUpdate
from flat_api.models.score_views_counts import ScoreViewsCounts
from flat_api.models.task import Task
from flat_api.models.task_export_options import TaskExportOptions
from flat_api.models.task_progress import TaskProgress
from flat_api.models.user_admin_update import UserAdminUpdate
from flat_api.models.user_creation import UserCreation
from flat_api.models.user_details import UserDetails
from flat_api.models.user_details_admin import UserDetailsAdmin
from flat_api.models.user_details_admin_license import UserDetailsAdminLicense
from flat_api.models.user_public import UserPublic
from flat_api.models.user_public_summary import UserPublicSummary

