from WebStoreApp.Domain.Review.Repositories.ReviewRepositoryInterface import ReviewRepositoryInterface
from WebStoreApp.Application.Commands.CreateReviewCommand import CreateReviewCommand
from WebStoreApp.Domain.Review.Entities.Review import Review
from WebStoreApp.Domain.Review.ValueObjects.ReviewId import ReviewId
from WebStoreApp.Domain.Review.ValueObjects.ReviewContent import ReviewContent
from WebStoreApp.Domain.Review.ValueObjects.ReviewCreatedByUserId import ReviewCreatedByUserId
from WebStoreApp.Domain.Review.ValueObjects.ReviewProductId import ReviewProductId
from WebStoreApp.Domain.Review.ValueObjects.ReviewRating import ReviewRating

class CreateReviewHandler:
    __repository:ReviewRepositoryInterface

    def __init__(self, repository:ReviewRepositoryInterface) -> None:
        self.__repository = repository

    @property
    def repository(self)->ReviewRepositoryInterface:
        return self.__repository
    
    @repository.setter
    def repository(self , repository)->None:
        self.__repository = repository

    def handler(self, command:CreateReviewCommand)->Review:
        p_brand = Review()
        p_brand.id = ReviewId(command.id)
        p_brand.content = ReviewContent(command.content)
        p_brand.rating = ReviewRating(command.rating)
        p_brand.product_id = ReviewProductId(command.product_id)
        p_brand.created_by_user_id = ReviewCreatedByUserId(command.created_by_user_id)
        
        return self.__repository.save(p_brand)