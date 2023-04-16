# pylint: disable= E1101

from src.domain.models import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel

class PetRepository:
    """ Manage Pet repository """

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """
        Insert data in pets entity
        :params - name: name of the pet
                - specie: Enum with species accepted
                - age: Pet age
                - user_id: id of the owner (FK)
        :return - tuple with the new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
