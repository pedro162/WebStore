from abc import ABC, abstractmethod
from WebStoreApp.Domain.ProductBrand.Entities.ProductBrand import ProductBrand
from WebStoreApp.Domain.ProductBrand.ValueObjects.ProductBrandId import ProductBrandId

class ProductBrandRepositoryInterface(ABC):
    def save(ProductBrand: ProductBrand)->ProductBrand:
        pass

    def findById(id: ProductBrandId)->ProductBrand:
        pass