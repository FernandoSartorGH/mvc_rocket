from src.models.sqlite.interfaces.people_repository import PeopleRepostoryInterface

class PersonCreatorController:
    # Inversão da dependência: Associa models com controlers
    def __init__(self, people_repository: PeopleRepostoryInterface) -> None: 
        self.__people_repository = people_repository
        
