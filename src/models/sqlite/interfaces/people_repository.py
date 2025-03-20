from abc import ABC, abstractclassmethod
from src.models.sqlite.entities.people import PeopleTable

class PeopleRepostoryInterface(ABC):

    @abstractclassmethod
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

    @abstractclassmethod
    def get_person(self, person_id: int) -> PeopleTable:
        pass
