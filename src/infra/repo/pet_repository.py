from src.domain.models import Pets
from src.infra.entities import Pets as PetsModel
from src.infra.config import DBConnectionHandler


class PetRepository:
    """Class manage pets repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Insert data Pet Entiyy"""
        with DBConnectionHandler() as db_conn:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_conn.session.add(new_pet)
                db_conn.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()
