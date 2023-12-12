from profiles.models import Anthropometric, Functional, PhysicalStandards
from .models import CustomUser

from journal.settings import FIRST_SEMESTER, COUNT_SEMESTER


def generate_physical_tables(user: CustomUser) -> None:
    for semester in range(FIRST_SEMESTER, COUNT_SEMESTER + 1):
        anthropometric_record = Anthropometric(user=user, semester=semester)
        anthropometric_record.save()
        functional_record = Functional(user=user, semester=semester)
        functional_record.save()
        physical_record = PhysicalStandards(user=user, semester=semester)
        physical_record.save()