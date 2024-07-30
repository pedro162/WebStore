class CreateReviewCommand:

    __id:str
    __content:str
    __rating:str
    __product_id:str
    __created_by_user_id:str

    def __init__(self) -> None:
        self.__id = None
        self.__content=None
        self.__rating=None
        self.__product_id=None
        self.__created_by_user_id=None

    @property
    def id(self)->str:
        return self.__id
    
    @id.setter
    def id(self, id:str)->None:
        self.__id = id

    @property
    def content(self)->str:
        return self.__content
    
    @content.setter
    def content(self, content:str)->None:
        self.__content = content

    @property
    def rating(self)->str:
        return self.__rating
    
    @rating.setter
    def rating(self, rating:str)->None:
        self.__rating = rating
    
    @property
    def product_id(self)->str:
        return self.__product_id
    
    @product_id.setter
    def product_id(self, product_id:str)->None:
        self.__product_id = product_id
    
    @property
    def created_by_user_id(self)->str:
        return self.__created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id:str)->None:
        self.__created_by_user_id = created_by_user_id