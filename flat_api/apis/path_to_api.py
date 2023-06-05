import typing_extensions

from flat_api.paths import PathValues
from flat_api.apis.paths.me import Me
from flat_api.apis.paths.scores import Scores
from flat_api.apis.paths.scores_score import ScoresScore
from flat_api.apis.paths.scores_score_untrash import ScoresScoreUntrash
from flat_api.apis.paths.scores_score_submissions import ScoresScoreSubmissions
from flat_api.apis.paths.scores_score_fork import ScoresScoreFork
from flat_api.apis.paths.scores_score_collaborators import ScoresScoreCollaborators
from flat_api.apis.paths.scores_score_collaborators_collaborator import ScoresScoreCollaboratorsCollaborator
from flat_api.apis.paths.scores_score_tracks import ScoresScoreTracks
from flat_api.apis.paths.scores_score_tracks_track import ScoresScoreTracksTrack
from flat_api.apis.paths.scores_score_comments import ScoresScoreComments
from flat_api.apis.paths.scores_score_comments_comment import ScoresScoreCommentsComment
from flat_api.apis.paths.scores_score_comments_comment_resolved import ScoresScoreCommentsCommentResolved
from flat_api.apis.paths.scores_score_revisions import ScoresScoreRevisions
from flat_api.apis.paths.scores_score_revisions_revision import ScoresScoreRevisionsRevision
from flat_api.apis.paths.scores_score_revisions_revision_format import ScoresScoreRevisionsRevisionFormat
from flat_api.apis.paths.scores_score_revisions_revision_format_task import ScoresScoreRevisionsRevisionFormatTask
from flat_api.apis.paths.collections import Collections
from flat_api.apis.paths.collections_collection import CollectionsCollection
from flat_api.apis.paths.collections_collection_untrash import CollectionsCollectionUntrash
from flat_api.apis.paths.collections_collection_scores import CollectionsCollectionScores
from flat_api.apis.paths.collections_collection_scores_score import CollectionsCollectionScoresScore
from flat_api.apis.paths.tasks_task import TasksTask
from flat_api.apis.paths.users_user import UsersUser
from flat_api.apis.paths.users_user_likes import UsersUserLikes
from flat_api.apis.paths.users_user_scores import UsersUserScores
from flat_api.apis.paths.organizations_users import OrganizationsUsers
from flat_api.apis.paths.organizations_users_count import OrganizationsUsersCount
from flat_api.apis.paths.organizations_users_user import OrganizationsUsersUser
from flat_api.apis.paths.organizations_users_user_signin_link import OrganizationsUsersUserSigninLink
from flat_api.apis.paths.organizations_users_user_access_token import OrganizationsUsersUserAccessToken
from flat_api.apis.paths.organizations_invitations import OrganizationsInvitations
from flat_api.apis.paths.organizations_invitations_invitation import OrganizationsInvitationsInvitation
from flat_api.apis.paths.organizations_lti_credentials import OrganizationsLtiCredentials
from flat_api.apis.paths.organizations_lti_credentials_credentials import OrganizationsLtiCredentialsCredentials
from flat_api.apis.paths.classes import Classes
from flat_api.apis.paths.classes_class import ClassesClass
from flat_api.apis.paths.classes_class_archive import ClassesClassArchive
from flat_api.apis.paths.classes_class_activate import ClassesClassActivate
from flat_api.apis.paths.classes_class_users_user import ClassesClassUsersUser
from flat_api.apis.paths.classes_class_students_user_submissions import ClassesClassStudentsUserSubmissions
from flat_api.apis.paths.classes_class_assignments import ClassesClassAssignments
from flat_api.apis.paths.classes_class_assignments_assignment_copy import ClassesClassAssignmentsAssignmentCopy
from flat_api.apis.paths.classes_class_assignments_assignment_archive import ClassesClassAssignmentsAssignmentArchive
from flat_api.apis.paths.classes_class_assignments_assignment_submissions import ClassesClassAssignmentsAssignmentSubmissions
from flat_api.apis.paths.classes_class_assignments_assignment_submissions_csv import ClassesClassAssignmentsAssignmentSubmissionsCsv
from flat_api.apis.paths.classes_class_assignments_assignment_submissions_excel import ClassesClassAssignmentsAssignmentSubmissionsExcel
from flat_api.apis.paths.classes_class_assignments_assignment_submissions_submission import ClassesClassAssignmentsAssignmentSubmissionsSubmission
from flat_api.apis.paths.classes_class_assignments_assignment_submissions_submission_history import ClassesClassAssignmentsAssignmentSubmissionsSubmissionHistory
from flat_api.apis.paths.classes_class_assignments_assignment_submissions_submission_comments import ClassesClassAssignmentsAssignmentSubmissionsSubmissionComments
from flat_api.apis.paths.classes_class_assignments_assignment_submissions_submission_comments_comment import ClassesClassAssignmentsAssignmentSubmissionsSubmissionCommentsComment
from flat_api.apis.paths.classes_class_test_student import ClassesClassTestStudent
from flat_api.apis.paths.classes_enroll_enrollment_code import ClassesEnrollEnrollmentCode
from flat_api.apis.paths.groups_group import GroupsGroup
from flat_api.apis.paths.groups_group_users import GroupsGroupUsers
from flat_api.apis.paths.groups_group_scores import GroupsGroupScores
from flat_api.apis.paths.edu_resources import EduResources
from flat_api.apis.paths.edu_resources_libraries import EduResourcesLibraries
from flat_api.apis.paths.edu_resources_resource import EduResourcesResource
from flat_api.apis.paths.edu_resources_resource_move import EduResourcesResourceMove
from flat_api.apis.paths.edu_resources_resource_copy import EduResourcesResourceCopy
from flat_api.apis.paths.edu_resources_resource_copy_to_demo_class import EduResourcesResourceCopyToDemoClass
from flat_api.apis.paths.edu_resources_resource_use_in_class import EduResourcesResourceUseInClass
from flat_api.apis.paths.edu_resources_resource_assignment import EduResourcesResourceAssignment

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ME: Me,
        PathValues.SCORES: Scores,
        PathValues.SCORES_SCORE: ScoresScore,
        PathValues.SCORES_SCORE_UNTRASH: ScoresScoreUntrash,
        PathValues.SCORES_SCORE_SUBMISSIONS: ScoresScoreSubmissions,
        PathValues.SCORES_SCORE_FORK: ScoresScoreFork,
        PathValues.SCORES_SCORE_COLLABORATORS: ScoresScoreCollaborators,
        PathValues.SCORES_SCORE_COLLABORATORS_COLLABORATOR: ScoresScoreCollaboratorsCollaborator,
        PathValues.SCORES_SCORE_TRACKS: ScoresScoreTracks,
        PathValues.SCORES_SCORE_TRACKS_TRACK: ScoresScoreTracksTrack,
        PathValues.SCORES_SCORE_COMMENTS: ScoresScoreComments,
        PathValues.SCORES_SCORE_COMMENTS_COMMENT: ScoresScoreCommentsComment,
        PathValues.SCORES_SCORE_COMMENTS_COMMENT_RESOLVED: ScoresScoreCommentsCommentResolved,
        PathValues.SCORES_SCORE_REVISIONS: ScoresScoreRevisions,
        PathValues.SCORES_SCORE_REVISIONS_REVISION: ScoresScoreRevisionsRevision,
        PathValues.SCORES_SCORE_REVISIONS_REVISION_FORMAT: ScoresScoreRevisionsRevisionFormat,
        PathValues.SCORES_SCORE_REVISIONS_REVISION_FORMAT_TASK: ScoresScoreRevisionsRevisionFormatTask,
        PathValues.COLLECTIONS: Collections,
        PathValues.COLLECTIONS_COLLECTION: CollectionsCollection,
        PathValues.COLLECTIONS_COLLECTION_UNTRASH: CollectionsCollectionUntrash,
        PathValues.COLLECTIONS_COLLECTION_SCORES: CollectionsCollectionScores,
        PathValues.COLLECTIONS_COLLECTION_SCORES_SCORE: CollectionsCollectionScoresScore,
        PathValues.TASKS_TASK: TasksTask,
        PathValues.USERS_USER: UsersUser,
        PathValues.USERS_USER_LIKES: UsersUserLikes,
        PathValues.USERS_USER_SCORES: UsersUserScores,
        PathValues.ORGANIZATIONS_USERS: OrganizationsUsers,
        PathValues.ORGANIZATIONS_USERS_COUNT: OrganizationsUsersCount,
        PathValues.ORGANIZATIONS_USERS_USER: OrganizationsUsersUser,
        PathValues.ORGANIZATIONS_USERS_USER_SIGNIN_LINK: OrganizationsUsersUserSigninLink,
        PathValues.ORGANIZATIONS_USERS_USER_ACCESS_TOKEN: OrganizationsUsersUserAccessToken,
        PathValues.ORGANIZATIONS_INVITATIONS: OrganizationsInvitations,
        PathValues.ORGANIZATIONS_INVITATIONS_INVITATION: OrganizationsInvitationsInvitation,
        PathValues.ORGANIZATIONS_LTI_CREDENTIALS: OrganizationsLtiCredentials,
        PathValues.ORGANIZATIONS_LTI_CREDENTIALS_CREDENTIALS: OrganizationsLtiCredentialsCredentials,
        PathValues.CLASSES: Classes,
        PathValues.CLASSES_CLASS: ClassesClass,
        PathValues.CLASSES_CLASS_ARCHIVE: ClassesClassArchive,
        PathValues.CLASSES_CLASS_ACTIVATE: ClassesClassActivate,
        PathValues.CLASSES_CLASS_USERS_USER: ClassesClassUsersUser,
        PathValues.CLASSES_CLASS_STUDENTS_USER_SUBMISSIONS: ClassesClassStudentsUserSubmissions,
        PathValues.CLASSES_CLASS_ASSIGNMENTS: ClassesClassAssignments,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_COPY: ClassesClassAssignmentsAssignmentCopy,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_ARCHIVE: ClassesClassAssignmentsAssignmentArchive,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS: ClassesClassAssignmentsAssignmentSubmissions,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_CSV: ClassesClassAssignmentsAssignmentSubmissionsCsv,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_EXCEL: ClassesClassAssignmentsAssignmentSubmissionsExcel,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_SUBMISSION: ClassesClassAssignmentsAssignmentSubmissionsSubmission,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_SUBMISSION_HISTORY: ClassesClassAssignmentsAssignmentSubmissionsSubmissionHistory,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_SUBMISSION_COMMENTS: ClassesClassAssignmentsAssignmentSubmissionsSubmissionComments,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_SUBMISSION_COMMENTS_COMMENT: ClassesClassAssignmentsAssignmentSubmissionsSubmissionCommentsComment,
        PathValues.CLASSES_CLASS_TEST_STUDENT: ClassesClassTestStudent,
        PathValues.CLASSES_ENROLL_ENROLLMENT_CODE: ClassesEnrollEnrollmentCode,
        PathValues.GROUPS_GROUP: GroupsGroup,
        PathValues.GROUPS_GROUP_USERS: GroupsGroupUsers,
        PathValues.GROUPS_GROUP_SCORES: GroupsGroupScores,
        PathValues.EDU_RESOURCES: EduResources,
        PathValues.EDU_RESOURCES_LIBRARIES: EduResourcesLibraries,
        PathValues.EDU_RESOURCES_RESOURCE: EduResourcesResource,
        PathValues.EDU_RESOURCES_RESOURCE_MOVE: EduResourcesResourceMove,
        PathValues.EDU_RESOURCES_RESOURCE_COPY: EduResourcesResourceCopy,
        PathValues.EDU_RESOURCES_RESOURCE_COPY_TO_DEMO_CLASS: EduResourcesResourceCopyToDemoClass,
        PathValues.EDU_RESOURCES_RESOURCE_USE_IN_CLASS: EduResourcesResourceUseInClass,
        PathValues.EDU_RESOURCES_RESOURCE_ASSIGNMENT: EduResourcesResourceAssignment,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ME: Me,
        PathValues.SCORES: Scores,
        PathValues.SCORES_SCORE: ScoresScore,
        PathValues.SCORES_SCORE_UNTRASH: ScoresScoreUntrash,
        PathValues.SCORES_SCORE_SUBMISSIONS: ScoresScoreSubmissions,
        PathValues.SCORES_SCORE_FORK: ScoresScoreFork,
        PathValues.SCORES_SCORE_COLLABORATORS: ScoresScoreCollaborators,
        PathValues.SCORES_SCORE_COLLABORATORS_COLLABORATOR: ScoresScoreCollaboratorsCollaborator,
        PathValues.SCORES_SCORE_TRACKS: ScoresScoreTracks,
        PathValues.SCORES_SCORE_TRACKS_TRACK: ScoresScoreTracksTrack,
        PathValues.SCORES_SCORE_COMMENTS: ScoresScoreComments,
        PathValues.SCORES_SCORE_COMMENTS_COMMENT: ScoresScoreCommentsComment,
        PathValues.SCORES_SCORE_COMMENTS_COMMENT_RESOLVED: ScoresScoreCommentsCommentResolved,
        PathValues.SCORES_SCORE_REVISIONS: ScoresScoreRevisions,
        PathValues.SCORES_SCORE_REVISIONS_REVISION: ScoresScoreRevisionsRevision,
        PathValues.SCORES_SCORE_REVISIONS_REVISION_FORMAT: ScoresScoreRevisionsRevisionFormat,
        PathValues.SCORES_SCORE_REVISIONS_REVISION_FORMAT_TASK: ScoresScoreRevisionsRevisionFormatTask,
        PathValues.COLLECTIONS: Collections,
        PathValues.COLLECTIONS_COLLECTION: CollectionsCollection,
        PathValues.COLLECTIONS_COLLECTION_UNTRASH: CollectionsCollectionUntrash,
        PathValues.COLLECTIONS_COLLECTION_SCORES: CollectionsCollectionScores,
        PathValues.COLLECTIONS_COLLECTION_SCORES_SCORE: CollectionsCollectionScoresScore,
        PathValues.TASKS_TASK: TasksTask,
        PathValues.USERS_USER: UsersUser,
        PathValues.USERS_USER_LIKES: UsersUserLikes,
        PathValues.USERS_USER_SCORES: UsersUserScores,
        PathValues.ORGANIZATIONS_USERS: OrganizationsUsers,
        PathValues.ORGANIZATIONS_USERS_COUNT: OrganizationsUsersCount,
        PathValues.ORGANIZATIONS_USERS_USER: OrganizationsUsersUser,
        PathValues.ORGANIZATIONS_USERS_USER_SIGNIN_LINK: OrganizationsUsersUserSigninLink,
        PathValues.ORGANIZATIONS_USERS_USER_ACCESS_TOKEN: OrganizationsUsersUserAccessToken,
        PathValues.ORGANIZATIONS_INVITATIONS: OrganizationsInvitations,
        PathValues.ORGANIZATIONS_INVITATIONS_INVITATION: OrganizationsInvitationsInvitation,
        PathValues.ORGANIZATIONS_LTI_CREDENTIALS: OrganizationsLtiCredentials,
        PathValues.ORGANIZATIONS_LTI_CREDENTIALS_CREDENTIALS: OrganizationsLtiCredentialsCredentials,
        PathValues.CLASSES: Classes,
        PathValues.CLASSES_CLASS: ClassesClass,
        PathValues.CLASSES_CLASS_ARCHIVE: ClassesClassArchive,
        PathValues.CLASSES_CLASS_ACTIVATE: ClassesClassActivate,
        PathValues.CLASSES_CLASS_USERS_USER: ClassesClassUsersUser,
        PathValues.CLASSES_CLASS_STUDENTS_USER_SUBMISSIONS: ClassesClassStudentsUserSubmissions,
        PathValues.CLASSES_CLASS_ASSIGNMENTS: ClassesClassAssignments,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_COPY: ClassesClassAssignmentsAssignmentCopy,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_ARCHIVE: ClassesClassAssignmentsAssignmentArchive,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS: ClassesClassAssignmentsAssignmentSubmissions,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_CSV: ClassesClassAssignmentsAssignmentSubmissionsCsv,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_EXCEL: ClassesClassAssignmentsAssignmentSubmissionsExcel,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_SUBMISSION: ClassesClassAssignmentsAssignmentSubmissionsSubmission,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_SUBMISSION_HISTORY: ClassesClassAssignmentsAssignmentSubmissionsSubmissionHistory,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_SUBMISSION_COMMENTS: ClassesClassAssignmentsAssignmentSubmissionsSubmissionComments,
        PathValues.CLASSES_CLASS_ASSIGNMENTS_ASSIGNMENT_SUBMISSIONS_SUBMISSION_COMMENTS_COMMENT: ClassesClassAssignmentsAssignmentSubmissionsSubmissionCommentsComment,
        PathValues.CLASSES_CLASS_TEST_STUDENT: ClassesClassTestStudent,
        PathValues.CLASSES_ENROLL_ENROLLMENT_CODE: ClassesEnrollEnrollmentCode,
        PathValues.GROUPS_GROUP: GroupsGroup,
        PathValues.GROUPS_GROUP_USERS: GroupsGroupUsers,
        PathValues.GROUPS_GROUP_SCORES: GroupsGroupScores,
        PathValues.EDU_RESOURCES: EduResources,
        PathValues.EDU_RESOURCES_LIBRARIES: EduResourcesLibraries,
        PathValues.EDU_RESOURCES_RESOURCE: EduResourcesResource,
        PathValues.EDU_RESOURCES_RESOURCE_MOVE: EduResourcesResourceMove,
        PathValues.EDU_RESOURCES_RESOURCE_COPY: EduResourcesResourceCopy,
        PathValues.EDU_RESOURCES_RESOURCE_COPY_TO_DEMO_CLASS: EduResourcesResourceCopyToDemoClass,
        PathValues.EDU_RESOURCES_RESOURCE_USE_IN_CLASS: EduResourcesResourceUseInClass,
        PathValues.EDU_RESOURCES_RESOURCE_ASSIGNMENT: EduResourcesResourceAssignment,
    }
)
