from abc import ABC, abstractmethod
from WebStoreApp.Domain.Review.Entities.Review import Review
from WebStoreApp.Domain.Review.ValueObjects.ReviewId import ReviewId

class ReviewRepositoryInterface(ABC):
    def save(review: Review)->Review:
        pass

    def findById(id: ReviewId)->Review:
        pass