from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository:
    """Class to manage User Repository"""

    def insert_user(self, name: str, password: str) -> Users:
        """insert data in user entity
        :params - name: person name
                - password: user password
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    def delete_user(self, user_id: int) -> Users:
        """delete user data
        :params - user_id: the id of user record
        :return - user record deleted
        """

        with DBConnectionHandler() as db_connection:
            try:
                removed_user = (
                    db_connection.session.query(UsersModel)
                    .filter(UsersModel.id == user_id)
                    .first()
                )
                db_connection.session.delete(removed_user)
                db_connection.session.commit()

                return Users(removed_user.id, removed_user.name, removed_user.password)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
