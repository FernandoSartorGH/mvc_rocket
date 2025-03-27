from src.models.sqlite.entities.pets import PetsTable
from .pet_list_controller import PetListController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name='Flufy', type='Cat', id=4),
            PetsTable(name='Bud', type='Dog', id=11),
        ]
    
def test_list_pets():
    controller = PetListController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Flufy", "id": 4},
                {"name": "Bud", "id": 11}
            ]
        }
    }

    assert response == expected_response