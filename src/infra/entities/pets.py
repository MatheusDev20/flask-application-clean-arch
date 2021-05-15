import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining animals types"""

    dog = ("dog",)
    cat = ("cat",)
    fish = "fish"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __rep__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}"
