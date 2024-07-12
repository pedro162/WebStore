from WebStoreApp.Domain.ProductBrand.Repositories.ProductBrandRepositoryInterface import ProductBrandRepositoryInterface
from WebStoreApp.Domain.ProductBrand.Entities.ProductBrand import ProductBrand
from WebStoreApp.Domain.ProductBrand.ValueObjects.ProductBrandId import ProductBrandId
from WebStoreApp.models import ProductBrand as ProductBrandModel
from datetime import datetime

class ProductBrandRepository(ProductBrandRepositoryInterface):
    def save(self, product_brand: ProductBrand) -> ProductBrand:
        pb_model = ProductBrandModel(
            id = product_brand.id.value,
            name=str(product_brand.name.value), 
            active='1',
            created_at=datetime.now()
        )
        pb_model.save()
        return self.findById(ProductBrandId(pb_model.id))
    
    def findById(self, id: ProductBrandId) -> ProductBrand:
        pb_model = ProductBrandModel.objects.get(id=id.value)
        prod_brand = ProductBrand()
        prod_brand.name = pb_model.name
        prod_brand.id = pb_model.id
        return prod_brand
