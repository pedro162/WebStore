from WebStoreApp.Application.Handlers.CreateProductBrandHandler import CreateProductBrandHandler
from WebStoreApp.Application.Commands.CreateProductBrandCommand import CreateProductBrandCommand

class ProductBrandApplicationService:
    __create_brand_handler:CreateProductBrandHandler

    @property
    def create_brand_handler(self)->CreateProductBrandHandler:
        return self.__create_brand_handler
    
    @create_brand_handler.setter
    def create_brand_handler(self, create_brand_handler:CreateProductBrandHandler)->"ProductBrandApplicationService":
        self.__create_brand_handler = create_brand_handler
        return self
    
    def create_brand(self, crate_brand_command:CreateProductBrandCommand):
        return self.__create_brand_handler.handler(crate_brand_command)