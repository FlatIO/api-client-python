from flat_api.paths.edu_resources_resource.get import ApiForget
from flat_api.paths.edu_resources_resource.put import ApiForput
from flat_api.paths.edu_resources_resource.delete import ApiFordelete


class EduResourcesResource(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
