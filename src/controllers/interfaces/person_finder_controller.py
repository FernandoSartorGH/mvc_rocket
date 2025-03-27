from typing import Dict
from abc import ABC, abstractclassmethod

class PersonFinderControllerInterface(ABC):
      
   @abstractclassmethod
   def find(self, person_id: int) -> Dict:
        pass