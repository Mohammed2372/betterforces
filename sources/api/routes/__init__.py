"""API routes package."""

from sources.api.routes.rating_distribution import RatingDistributionController
from sources.api.routes.tags import TagsController

routes = [
    RatingDistributionController,
    TagsController,
]