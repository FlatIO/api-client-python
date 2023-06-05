
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from flat_api.api.account_api import AccountApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from flat_api.api.account_api import AccountApi
from flat_api.api.class_api import ClassApi
from flat_api.api.collection_api import CollectionApi
from flat_api.api.edu_resources_api import EduResourcesApi
from flat_api.api.group_api import GroupApi
from flat_api.api.organization_api import OrganizationApi
from flat_api.api.score_api import ScoreApi
from flat_api.api.task_api import TaskApi
from flat_api.api.user_api import UserApi
