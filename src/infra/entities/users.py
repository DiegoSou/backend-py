from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


# Herança
class Users(Base):
    """Users Entity - base declarativa"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pets")  # será formatado mais pra frente

    def __repr__(self):
        return f"Usr [name={self.name}]"
