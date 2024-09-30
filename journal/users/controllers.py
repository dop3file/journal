from profiles.models import Anthropometric, Functional, PhysicalStandards, Health
from .models import CustomUser

from journal.settings import FIRST_SEMESTER, COUNT_SEMESTER, COUNT_LESSONS


def generate_physical_tables(user: CustomUser) -> None:
    for semester in range(FIRST_SEMESTER, COUNT_SEMESTER + 1):
        anthropometric_record = Anthropometric(user=user, semester=semester)
        anthropometric_record.save()
        functional_record = Functional(user=user, semester=semester)
        functional_record.save()
        physical_record = PhysicalStandards(user=user, semester=semester)
        physical_record.save()
    for lesson in range(1, COUNT_LESSONS + 1):
        health = Health(user=user, lesson_number=lesson)
        health.save()