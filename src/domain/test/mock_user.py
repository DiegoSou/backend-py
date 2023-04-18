from faker import Faker
from src.domain.models import Users

faker = Faker()


def mock_users(user_id: int = None) -> Users:
    """mock instance of Users Model"""

    if user_id:
        return Users(id=user_id, name=faker.name(), password=faker.name())

    else:
        return Users(
            id=faker.random_number(digits=5), name=faker.name(), password=faker.name()
        )
