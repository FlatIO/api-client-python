# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from flat_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from flat_api.model.api_access_token import ApiAccessToken
from flat_api.model.app_scopes import AppScopes
from flat_api.model.assignment import Assignment
from flat_api.model.assignment_copy import AssignmentCopy
from flat_api.model.assignment_copy_response import AssignmentCopyResponse
from flat_api.model.assignment_submission import AssignmentSubmission
from flat_api.model.assignment_submission_comment import AssignmentSubmissionComment
from flat_api.model.assignment_submission_comment_creation import AssignmentSubmissionCommentCreation
from flat_api.model.assignment_submission_history import AssignmentSubmissionHistory
from flat_api.model.assignment_submission_history_state import AssignmentSubmissionHistoryState
from flat_api.model.assignment_submission_state import AssignmentSubmissionState
from flat_api.model.assignment_submission_update import AssignmentSubmissionUpdate
from flat_api.model.assignment_type import AssignmentType
from flat_api.model.assignment_update import AssignmentUpdate
from flat_api.model.class_assignment import ClassAssignment
from flat_api.model.class_assignment_update import ClassAssignmentUpdate
from flat_api.model.class_attachment_creation import ClassAttachmentCreation
from flat_api.model.class_creation import ClassCreation
from flat_api.model.class_details import ClassDetails
from flat_api.model.class_grade_level import ClassGradeLevel
from flat_api.model.class_roles import ClassRoles
from flat_api.model.class_state import ClassState
from flat_api.model.class_update import ClassUpdate
from flat_api.model.collection import Collection
from flat_api.model.collection_app import CollectionApp
from flat_api.model.collection_creation import CollectionCreation
from flat_api.model.collection_modification import CollectionModification
from flat_api.model.collection_privacy import CollectionPrivacy
from flat_api.model.collection_type import CollectionType
from flat_api.model.edu_library import EduLibrary
from flat_api.model.edu_resource import EduResource
from flat_api.model.edu_resource_copy import EduResourceCopy
from flat_api.model.edu_resource_creation import EduResourceCreation
from flat_api.model.edu_resource_move import EduResourceMove
from flat_api.model.edu_resource_privacy import EduResourcePrivacy
from flat_api.model.edu_resource_type import EduResourceType
from flat_api.model.edu_resource_update import EduResourceUpdate
from flat_api.model.edu_resource_use_in_class import EduResourceUseInClass
from flat_api.model.edu_skills_focused import EduSkillsFocused
from flat_api.model.flat_error_response import FlatErrorResponse
from flat_api.model.flat_locales import FlatLocales
from flat_api.model.google_classroom_coursework import GoogleClassroomCoursework
from flat_api.model.google_classroom_submission import GoogleClassroomSubmission
from flat_api.model.group import Group
from flat_api.model.group_details import GroupDetails
from flat_api.model.group_type import GroupType
from flat_api.model.license_mode import LicenseMode
from flat_api.model.license_sources import LicenseSources
from flat_api.model.lms_name import LmsName
from flat_api.model.lti_credentials import LtiCredentials
from flat_api.model.lti_credentials_creation import LtiCredentialsCreation
from flat_api.model.media_attachment import MediaAttachment
from flat_api.model.media_score_sharing_mode import MediaScoreSharingMode
from flat_api.model.microsoft_graph_assignment import MicrosoftGraphAssignment
from flat_api.model.microsoft_graph_submission import MicrosoftGraphSubmission
from flat_api.model.organization_invitation import OrganizationInvitation
from flat_api.model.organization_invitation_creation import OrganizationInvitationCreation
from flat_api.model.organization_roles import OrganizationRoles
from flat_api.model.organization_user_access_token_creation import OrganizationUserAccessTokenCreation
from flat_api.model.resource_collaborator import ResourceCollaborator
from flat_api.model.resource_collaborator_creation import ResourceCollaboratorCreation
from flat_api.model.resource_rights import ResourceRights
from flat_api.model.score_comment import ScoreComment
from flat_api.model.score_comment_context import ScoreCommentContext
from flat_api.model.score_comment_creation import ScoreCommentCreation
from flat_api.model.score_comment_update import ScoreCommentUpdate
from flat_api.model.score_comments_counts import ScoreCommentsCounts
from flat_api.model.score_creation import ScoreCreation
from flat_api.model.score_creation_type import ScoreCreationType
from flat_api.model.score_details import ScoreDetails
from flat_api.model.score_fork import ScoreFork
from flat_api.model.score_license import ScoreLicense
from flat_api.model.score_likes_counts import ScoreLikesCounts
from flat_api.model.score_modification import ScoreModification
from flat_api.model.score_plays_counts import ScorePlaysCounts
from flat_api.model.score_privacy import ScorePrivacy
from flat_api.model.score_revision import ScoreRevision
from flat_api.model.score_revision_creation import ScoreRevisionCreation
from flat_api.model.score_revision_statistics import ScoreRevisionStatistics
from flat_api.model.score_source import ScoreSource
from flat_api.model.score_track import ScoreTrack
from flat_api.model.score_track_creation import ScoreTrackCreation
from flat_api.model.score_track_point import ScoreTrackPoint
from flat_api.model.score_track_state import ScoreTrackState
from flat_api.model.score_track_type import ScoreTrackType
from flat_api.model.score_track_update import ScoreTrackUpdate
from flat_api.model.score_views_counts import ScoreViewsCounts
from flat_api.model.task import Task
from flat_api.model.task_export_options import TaskExportOptions
from flat_api.model.user_admin_update import UserAdminUpdate
from flat_api.model.user_azure_details import UserAzureDetails
from flat_api.model.user_community_profile_links import UserCommunityProfileLinks
from flat_api.model.user_creation import UserCreation
from flat_api.model.user_details import UserDetails
from flat_api.model.user_details_admin import UserDetailsAdmin
from flat_api.model.user_public import UserPublic
from flat_api.model.user_public_summary import UserPublicSummary
from flat_api.model.user_signin_link import UserSigninLink
from flat_api.model.user_signin_link_creation import UserSigninLinkCreation
