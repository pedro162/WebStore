class ProductBrandId:
    __value:str

    def __init__(self, value:str) -> None:
        if len(str(value)) == 0:
            raise ValueError("The product brand's ID informed is not valid")
        self.__value = value

    @property
    def value(self)->str:
        return self.__value
    
    @value.setter
    def value(self, value:str)->None:
        self.__value = value

    def __str__(self) -> str:
        return self.__value