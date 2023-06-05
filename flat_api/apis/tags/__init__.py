# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from flat_api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNT = "Account"
    SCORE = "Score"
    COLLECTION = "Collection"
    USER = "User"
    ORGANIZATION = "Organization"
    CLASS = "Class"
    EDU_RESOURCES = "EduResources"
    GROUP = "Group"
    TASK = "Task"
