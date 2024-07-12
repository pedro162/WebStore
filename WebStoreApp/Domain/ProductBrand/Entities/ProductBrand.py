from WebStoreApp.Domain.ProductBrand.ValueObjects.ProductBrandId import ProductBrandId
from WebStoreApp.Domain.ProductBrand.ValueObjects.ProductBrandName import ProductBrandName
from WebStoreApp.models import ProductBrand as ProductBrandModel

class ProductBrand:
    __id:ProductBrandId
    __name:ProductBrandName

    def __init__(self) -> None:
        self.__id = None
        self.__name = None

    @property
    def id(self)->ProductBrandId:
        return self.__id
    
    @id.setter
    def id(self, id:ProductBrandId)->'ProductBrand':
        self.__id = id
        return self

    @property
    def name(self)->ProductBrandName:
        return self.__name
    
    @name.setter
    def name(self, name:ProductBrandName)->'ProductBrand':
        self.__name=name
        return self
    
    def builder(self)->ProductBrandModel:
        return ProductBrandModel(
            id=self.id,
            name=self.name,
        )


    