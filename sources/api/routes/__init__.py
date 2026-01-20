"""API routes package."""

from sources.api.routes.abandoned_problems import AbandonedProblemsController
from sources.api.routes.base import BaseMetricController
from sources.api.routes.difficulty_distribution import DifficultyDistributionController
from sources.api.routes.tags import TagsController

routes = [
    AbandonedProblemsController,
    DifficultyDistributionController,
    TagsController,
]

__all__ = [
    "AbandonedProblemsController",
    "BaseMetricController",
    "DifficultyDistributionController",
    "TagsController",
    "routes",
]
