from WebStoreApp.Domain.ProductBrand.Repositories.ProductBrandRepositoryInterface import ProductBrandRepositoryInterface
from WebStoreApp.Application.Commands.CreateProductBrandCommand import CreateProductBrandCommand
from WebStoreApp.Domain.ProductBrand.Entities.ProductBrand import ProductBrand
from WebStoreApp.Domain.ProductBrand.ValueObjects.ProductBrandId import ProductBrandId
from WebStoreApp.Domain.ProductBrand.ValueObjects.ProductBrandName import ProductBrandName

class CreateProductBrandHandler:
    __repository:ProductBrandRepositoryInterface

    def __init__(self, repository:ProductBrandRepositoryInterface) -> None:
        self.__repository = repository

    @property
    def repository(self)->ProductBrandRepositoryInterface:
        return self.__repository
    
    @repository.setter
    def repository(self , repository)->None:
        self.__repository = repository

    def handler(self, command:CreateProductBrandCommand)->ProductBrand:
        p_brand = ProductBrand()
        p_brand.id = ProductBrandId(command.id)
        p_brand.name = ProductBrandName(command.name)
        return self.repository.save(p_brand)