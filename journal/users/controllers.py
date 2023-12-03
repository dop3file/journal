from profiles.models import Anthropometric
from .models import CustomUser


def generate_anthropometric(user: CustomUser) -> None:
    for semester in range(1, 9):
        anthropometric_record = Anthropometric(user=user, semester=semester)
        anthropometric_record.save()