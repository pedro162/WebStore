class BasePersonCommand:
    __person_id:str
    __first_name:str
    __last_name:str
    __social_name:str
    __document:str
    __gender_id:str

    @property
    def person_id(self)->str:
        return self.__person_id

    @person_id.setter
    def person_id(self, person_id:str)->None:
        self.person_id = person_id

    @property
    def last_name(self)->str:
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name:str)->None:
        self.__last_name = last_name
    
    @property
    def social_name(self)->str:
        return self.__last_name
    
    @social_name.setter
    def social_name(self, social_name:str)->None:
        self.__social_name = social_name

    @property
    def document(self)->str:
        return self.__last_name
    
    @document.setter
    def document(self, document:str)->None:
        self.__document = document
        
    @property
    def gender_id(self)->str:
        return self.__last_name
    
    @gender_id.setter
    def gender_id(self, gender_id:str)->None:
        self.__gender_id = gender_id