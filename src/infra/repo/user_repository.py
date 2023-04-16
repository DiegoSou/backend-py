from typing import List
from src.data.interfaces import UserRepositoryInterface
from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
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

    @classmethod
    def delete_user(cls, user_id: int = None) -> Users:
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

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """
        Select data in user entity by id and/or name
        :param - user_id: Id of registry
               - name: User name
        :return - List with Users selected
        """

        try:
            query_data = None

            if user_id and not name:
                # Select user by id
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

            elif not user_id and name:
                # Select user by name
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif user_id and name:
                # Select user by id and name
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
