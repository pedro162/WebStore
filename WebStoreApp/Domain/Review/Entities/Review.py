from WebStoreApp.Domain.Review.ValueObjects.ReviewId import ReviewId
from WebStoreApp.Domain.Review.ValueObjects.ReviewContent import ReviewContent
from WebStoreApp.Domain.Review.ValueObjects.ReviewProductId import ReviewProductId
from WebStoreApp.Domain.Review.ValueObjects.ReviewRating import ReviewRating
from WebStoreApp.Domain.Review.ValueObjects.ReviewCreatedByUserId import ReviewCreatedByUserId
from WebStoreApp.models import Review as ReviewModel

class Review:
    __id:ReviewId
    __content:ReviewContent
    __rating:ReviewRating
    __product_id:ReviewProductId
    __created_by_user_id:ReviewCreatedByUserId

    def __init__(self) -> None:
        self.__id = None
        self.__content = None
        self.__rating = None
        self.__product_id = None
        self.__created_by_user_id = None

    @property
    def id(self)->ReviewId:
        return self.__id
    
    @id.setter
    def id(self, id:ReviewId)->'Review':
        self.__id = id
        return self

    @property
    def content(self)->ReviewContent:
        return self.__content
    
    @content.setter
    def content(self, content:ReviewContent)->'Review':
        self.__content=content
        return self
    
    @property
    def rating(self)->ReviewRating:
        return self.__rating
    
    @rating.setter
    def rating(self, rating)->'Review':
        self.__rating = rating
        return self

    @property
    def product_id(self)->ReviewProductId:
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id)->'Review':
        self.__product_id = product_id
        return self

    @property
    def created_by_user_id(self)->ReviewCreatedByUserId:
        return self.__created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id)->'Review':
        self.__created_by_user_id = created_by_user_id
        return self

    def builder(self)->ReviewModel:
        return ReviewModel(
            id=self.id,
            content=self.content,
        )


    