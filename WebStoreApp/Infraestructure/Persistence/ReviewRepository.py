from WebStoreApp.Domain.Review.Repositories.ReviewRepositoryInterface import ReviewRepositoryInterface
from WebStoreApp.Domain.Review.Entities.Review import Review as ReviewEntity
from WebStoreApp.Domain.Review.ValueObjects.ReviewId import ReviewId
from WebStoreApp.Domain.Review.ValueObjects.ReviewContent import ReviewContent
from WebStoreApp.Domain.Review.ValueObjects.ReviewCreatedByUserId import ReviewCreatedByUserId
from WebStoreApp.Domain.Review.ValueObjects.ReviewProductId import ReviewProductId
from WebStoreApp.Domain.Review.ValueObjects.ReviewRating import ReviewRating
from WebStoreApp.models import Review as ReviewModel
from WebStoreApp.models import Product as ProductModel
from WebStoreApp.models import User as UserModel
from datetime import datetime

class ReviewRepository(ReviewRepositoryInterface):
    def save(self, review: ReviewEntity) -> ReviewEntity:
        user_id = review.created_by_user_id.value
        product_id = review.product_id.value

        try:
            # Obtém a instância do usuário com base no ID fornecido
            user = UserModel.objects.get(id=user_id)
            product = ProductModel.objects.get(id=user_id)
        except User.DoesNotExist:
            # Lidar com o caso onde o usuário não é encontrado
            raise ValueError(f"User with ID {user_id} does not exist")

        #raise Exception('review.created_by_user_id: == '+str(review.product_id.value))
        rw_model = ReviewModel(
            id = review.id.value,
            comment=str(review.content.value), 
            rating=str(review.rating.value), 
            product_id=product, 
            #created_by_user_id=user, 
            active='1',
            created_at=datetime.now()
        )

        rw_model.save()
        return self.findById(ReviewId(rw_model.pk))
    
    def findById(self, id: ReviewId) -> ReviewEntity:
        rw_model = ReviewModel.objects.get(id=id.value)
        review = ReviewEntity()
        review.id = ReviewId(rw_model.id)
        review.content = ReviewContent(rw_model.comment)
        review.rating = ReviewRating(rw_model.rating)
        review.product_id = ReviewProductId(rw_model.product_id)
        review.created_by_user_id = ReviewCreatedByUserId(rw_model.created_by_user_id)
        return review
