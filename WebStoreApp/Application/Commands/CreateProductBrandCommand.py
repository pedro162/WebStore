class CreateProductBrandCommand:

    __id:str
    __name:str
    def __init__(self) -> None:
        self.__id = None
        self.__name=None

    @property
    def id(self)->str:
        return self.__id
    
    @id.setter
    def id(self, id:str)->None:
        self.__id = id

    @property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self, name:str)->None:
        self.__name = name