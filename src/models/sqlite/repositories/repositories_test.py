import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()

# teste de integração com o banco de dados
@pytest.mark.skip(reason="interação com o banco")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)

# teste de integração com o banco de dados
@pytest.mark.skip(reason="interação com o banco")
def test_delte_pet():
    name = 'belinha'

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)
