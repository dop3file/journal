from profiles.models import Anthropometric, Functional
from .models import CustomUser


def generate_physical_tables(user: CustomUser) -> None:
    for semester in range(1, 9):
        anthropometric_record = Anthropometric(user=user, semester=semester)
        anthropometric_record.save()
        functional_record = Functional(user=user, semester=semester)
        functional_record.save()