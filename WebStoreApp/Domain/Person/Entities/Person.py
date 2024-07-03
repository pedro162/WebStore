from Domain.Person.ValueObjects.PersonId import PersonId
from Domain.Person.ValueObjects.PersonFirstName import PersonFirstName
from Domain.Person.ValueObjects.PersonLastName import PersonLastName
from Domain.Person.ValueObjects.PersonDocument import PersonDocument
from Domain.Person.ValueObjects.PersonGenderId import PersonGenderId
from Domain.Person.ValueObjects.PersonSocialName import PersonSocialName

class Person:
    __id:PersonId
    __first_name:PersonFirstName
    __last_name:PersonLastName
    __social_name:PersonSocialName
    __document:PersonDocument
    __gender_id:PersonGenderId

    @property
    def id(self)->PersonId:
        return self.__id
    
    @id.setter
    def id(self, id:PersonId)->None:
        self.__id=id

    @property
    def last_name(self)->PersonLastName:
        return self.__last_name

    @last_name.setter    
    def last_name(self, last_name:PersonLastName)->None:
        self.__last_name=last_name

    @first_name.setter
    def first_name(self, first_name:PersonFirstName)->None:
        self.__first_name=first_name
    
    @property
    def first_name(self)->PersonFirstName:
        return self.__first_name

    @social_name.setter
    def social_name(self, social_name:PersonSocialName)->None:
        self.__social_name=social_name
    
    @property
    def social_name(self)->PersonSocialName:
        return self.__social_name

    @document.setter
    def document(self, document:PersonDocument)->None:
        self.__document=document
    
    @property
    def document(self)->PersonDocument:
        return self.__document
    
    @gender_id.setter
    def gender_id(self, gender_id:PersonGenderId)->None:
        self.__gender_id=gender_id
    
    @property
    def gender_id(self)->PersonGenderId:
        return self.__gender_id

    