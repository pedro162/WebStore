from Domain.Person.Repositories.PersonRepositoryInterface import PersonRepositoryInterface
from Application.Commands.CreatePersonCommand import CreatePersonCommand
from Domain.Person.Entities.Person import Person
from Domain.Person.ValueObjects.PersonId import PersonId

class CreatePersonHandler:
    __repository:PersonRepositoryInterface

    def __init__(self, repository:PersonRepositoryInterface) -> None:
        self.__repository = repository

    @property
    def repository(self)->PersonRepositoryInterface:
        return self.__repository
    
    @repository.setter
    def repository(self , repository)->None:
        self.__repository = repository

    def handler(self, command:CreatePersonCommand)->Person:
        person = Person()
        person.id(PersonId(command.person_id))
        return self.repository.save(person)