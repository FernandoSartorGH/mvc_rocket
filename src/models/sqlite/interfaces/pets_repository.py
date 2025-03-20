from typing import List
from abc import ABC, abstractclassmethod
from src.models.sqlite.entities.pets import PetsTable

class PetsRepositoryInterface(ABC):

    @abstractclassmethod
    def list_pets(self) -> List[PetsTable]:
        pass

    @abstractclassmethod
    def delete_pets(self, name: str) -> None:
        pass