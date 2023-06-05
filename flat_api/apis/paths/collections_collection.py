from flat_api.paths.collections_collection.get import ApiForget
from flat_api.paths.collections_collection.put import ApiForput
from flat_api.paths.collections_collection.delete import ApiFordelete


class CollectionsCollection(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
