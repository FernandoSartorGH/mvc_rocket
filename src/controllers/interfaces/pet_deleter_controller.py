from abc import ABC, abstractclassmethod

class PetDeleterControllerInterface(ABC):
    
    @abstractclassmethod
    def delete(self, name: str) -> None:
        pass
