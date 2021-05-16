from typing import List
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
                print(new_pet)
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

    @classmethod
    def select_pet(
        cls,
        pet_id: int = None,
        user_id: int = None,
    ) -> List[Pets]:
        """Select pet entity
        :param - pet_id - Id of registered pet
        :param - user_id id of registered pet.
        """
        with DBConnectionHandler() as db_conn:
            try:
                query_data = None

                if pet_id and not user_id:
                    data = db_conn.session.query(PetsModel).filter_by(id=pet_id).one()
                    query_data = [data]
                elif not pet_id and user_id:
                    data = (
                        db_conn.session.query(PetsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data
                elif pet_id and user_id:
                    data = (
                        db_conn.session.query(PetsModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

                return query_data

            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()
