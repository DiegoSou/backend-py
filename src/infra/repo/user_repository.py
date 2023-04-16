from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """Class to manage User Repository"""

    def insert_user(self, name: str, password: str) -> Users:
        """insert data in user entity
        :params - name: person name
                - password: user password
        :return - tuple with new user inserted
        """

        InsertData = namedtuple("Users", "id name, password")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return InsertData(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    def delete_user(self, user_id: int):
        """delete user data
        :params - user_id: the id of user record
        :return - user record deleted
        """

        DeletedData = namedtuple("Users", "id name, password")

        with DBConnectionHandler() as db_connection:
            try:
                removed_user = (
                    db_connection.session.query(Users)
                    .filter(Users.id == user_id)
                    .first()
                )
                db_connection.session.delete(removed_user)
                db_connection.session.commit()

                return DeletedData(
                    removed_user.id, removed_user.name, removed_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None