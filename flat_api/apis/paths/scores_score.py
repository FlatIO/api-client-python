from flat_api.paths.scores_score.get import ApiForget
from flat_api.paths.scores_score.put import ApiForput
from flat_api.paths.scores_score.delete import ApiFordelete


class ScoresScore(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
