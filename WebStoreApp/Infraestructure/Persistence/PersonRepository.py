from Domain.Person.Repositories.PersonRepositoryInterface import PersonRepositoryInterface
from WebStoreApp.Domain.Person.Entities.Person import Person
from WebStoreApp.Domain.Person.ValueObjects.PersonId import PersonId

class PersonRepository(PersonRepositoryInterface):
    def save(person: Person) -> Person:
        #TODO
        return Person()
    
    def findById(id: PersonId) -> Person:
        #TODO
        return Person()