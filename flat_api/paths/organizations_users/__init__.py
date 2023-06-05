# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from flat_api.paths.organizations_users import Api

from flat_api.paths import PathValues

path = PathValues.ORGANIZATIONS_USERS