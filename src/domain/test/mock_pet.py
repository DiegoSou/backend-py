from faker import Faker
from src.domain.models import Pets

faker = Faker()


def mock_pets(pet_id: int = None) -> Pets:
    """mock instance of Pets model"""

    if pet_id:
        return Pets(
            id=pet_id,
            name=faker.name(),
            age=faker.random_number(digits=1),
            user_id=faker.random_number(digits=2),
            specie="FISH",
        )

    else:
        return Pets(
            id=faker.random_number(digits=5),
            name=faker.name(),
            age=faker.random_number(digits=1),
            user_id=faker.random_number(digits=2),
            specie="FISH",
        )
