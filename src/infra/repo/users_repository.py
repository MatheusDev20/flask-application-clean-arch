from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UsersRepository:
    """Repositório de usuários"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """Insert data in user tables
        :return - tuple with new user
        :params - name, password

        """

        insert_data = namedtuple("Users", "id name, password")
        with DBConnectionHandler() as db_conn:
            try:
                new_user = Users(name=name, password=password)
                db_conn.session.add(new_user)
                db_conn.session.commit()

                return insert_data(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )

            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()

        return None
