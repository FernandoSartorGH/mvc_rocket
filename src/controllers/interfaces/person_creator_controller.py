from typing import Dict
from abc import ABC, abstractclassmethod

class PersonCreatorControllerInterface(ABC):

    @abstractclassmethod
    def create(self, person_info: Dict) -> Dict:
        pass
        