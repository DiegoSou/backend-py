# pylint: disable= E1101

from typing import List
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel


class PetRepository(PetRepositoryInterface):
    """Manage Pet repository"""

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
                    user_id=new_pet.user_id,
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_pet(
        cls, pet_id: int = None, user_id: int = None, name: str = None
    ) -> List[Pets]:
        """
        Select in PetsEntity entity by id, user id or name
        :params - pet_id: Id of the pet registry
                - user_id: Id of the owner
                - name: Name of the pet registry
        :return - List with pets selected
        """

        try:
            query_data = None

            if pet_id and not user_id:
                # pet by id
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id)
                        .one()
                    )
                    query_data = [data]

            elif not pet_id and user_id:
                # pet by user id
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data

            elif not pet_id and not user_id and name:
                # pet by name
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(name=name)
                        .all()
                    )
                    query_data = data

            elif not pet_id and user_id and name:
                # pet by user and name
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(user_id=user_id, name=name)
                        .all()
                    )
                    query_data = data

            return query_data

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
