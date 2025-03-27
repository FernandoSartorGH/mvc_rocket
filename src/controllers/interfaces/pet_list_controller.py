from typing import Dict
from abc import ABC, abstractclassmethod

class PetListControllerInterface(ABC):
    
    @abstractclassmethod
    def list(self) -> Dict:
      pass
        