import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining Anymals Types"""

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
    TURTLE = "turtle"


# Herança
class Pets(Base):
    """Pets Entity - base declarativa"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"
