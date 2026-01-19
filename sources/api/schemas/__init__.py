"""API schemas package."""

from .rating_distribution import RatingDistributionResponse, RatingPointSchema
from .tags import TagsResponse, TagInfoSchema, WeakTagsResponse
from .common import APIResponse, ErrorResponse

__all__ = [
    "RatingDistributionResponse",
    "RatingPointSchema",
    "TagsResponse",
    "TagInfoSchema",
    "WeakTagsResponse",
    "APIResponse",
    "ErrorResponse"
]