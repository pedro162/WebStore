from WebStoreApp.Application.Handlers.CreateReviewHandler import CreateReviewHandler
from WebStoreApp.Application.Commands.CreateReviewCommand import CreateReviewCommand

class ReviewApplicationService:
    __create_review_handler:CreateReviewHandler

    @property
    def create_review_handler(self)->CreateReviewHandler:
        return self.__create_review_handler
    
    @create_review_handler.setter
    def create_review_handler(self, create_review_handler:CreateReviewHandler)->"ReviewApplicationService":
        self.__create_review_handler = create_review_handler
        return self
    
    def create_review(self, crate_review_command:CreateReviewCommand):
        return self.__create_review_handler.handler(crate_review_command)