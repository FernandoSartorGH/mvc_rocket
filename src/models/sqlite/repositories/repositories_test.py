import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepostory

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

# teste de integração com o banco de dados
@pytest.mark.skip(reason="interação com o banco")
def test_insert_person():
    first_name = "test name"
    last_name = "test last"
    age = 77
    pet_id = 2

    repo = PeopleRepostory(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)


# teste de integração com o banco de dados
@pytest.mark.skip(reason="interação com o banco")
def test_get_person():
    person_id = 1
  
    repo = PeopleRepostory(db_connection_handler)
    response = repo.get_person(person_id)

    print()
    print(person_id)
    print(response)
    print(response.pet_name)
