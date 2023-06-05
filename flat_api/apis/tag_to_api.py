import typing_extensions

from flat_api.apis.tags import TagValues
from flat_api.apis.tags.account_api import AccountApi
from flat_api.apis.tags.score_api import ScoreApi
from flat_api.apis.tags.collection_api import CollectionApi
from flat_api.apis.tags.user_api import UserApi
from flat_api.apis.tags.organization_api import OrganizationApi
from flat_api.apis.tags.model_class_api import ModelClassApi
from flat_api.apis.tags.edu_resources_api import EduResourcesApi
from flat_api.apis.tags.group_api import GroupApi
from flat_api.apis.tags.task_api import TaskApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.SCORE: ScoreApi,
        TagValues.COLLECTION: CollectionApi,
        TagValues.USER: UserApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.CLASS: ModelClassApi,
        TagValues.EDU_RESOURCES: EduResourcesApi,
        TagValues.GROUP: GroupApi,
        TagValues.TASK: TaskApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.SCORE: ScoreApi,
        TagValues.COLLECTION: CollectionApi,
        TagValues.USER: UserApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.CLASS: ModelClassApi,
        TagValues.EDU_RESOURCES: EduResourcesApi,
        TagValues.GROUP: GroupApi,
        TagValues.TASK: TaskApi,
    }
)
