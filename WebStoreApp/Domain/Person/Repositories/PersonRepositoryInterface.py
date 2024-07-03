from abc import ABC, abstractmethod
from Domain.Person.Entities.Person import Person
from Domain.Person.ValueObjects.PersonId import PersonId

class PersonRepositoryInterface(ABC):
    def save(person: Person)->Person:
        pass

    def findById(id: PersonId)->Person:
        pass