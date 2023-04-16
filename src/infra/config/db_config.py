# define mecanismo de Conexão (dois underscores definem o atributo como privado)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        """Construtor
        :attr - __connection_string: uma string de conexão que o sql alchemy vai requerir e vai fazer o acesso ao banco
        """

        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """Return connection engine
        :params - None
        :return - engine connection to database
        """

        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
