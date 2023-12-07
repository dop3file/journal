import math
from copy import deepcopy
from typing import Type, Tuple

from django.db.models import Model
from django.http import HttpRequest

from journal import settings
from .models import Anthropometric, Functional
from users.models import CustomUser


class PhysicalTableControllers:
    def __init__(self, table_class: Type[Model], not_exists_fields: tuple[str]):
        self.table_class = table_class
        self.fields: list[str] = [field.name for field in table_class._meta.fields if field.name not in not_exists_fields]
        self.count_semester = settings.COUNT_SEMESTER

    def get_table(self, user: CustomUser) -> dict[str, list[Model]]:
        result = {
            field: [] for field in self.fields
        }
        for field in self.fields:
            for semester in range(1, self.count_semester + 1):
                result[field].append(
                    getattr(self.table_class.objects.filter(user=user, semester=semester).first(), field))

        return result

    def update_table(self, table_data: dict, user: CustomUser):
        for parameter, semester_value_list in table_data["data"].items():
            for semester, semester_value in enumerate(semester_value_list):
                if semester_value:
                    try:
                        semester_value = float(semester_value)
                    except ValueError:
                        return
                    record = self.table_class.objects.filter(user=user, semester=semester + 1).first()
                    setattr(record, parameter, semester_value if semester_value else None)
                    record.save()


class AnthropometricTableControllers(PhysicalTableControllers):
    def __init__(self, table_class: Type[Model], not_exists_fields: Tuple[str]):
        super().__init__(table_class, not_exists_fields)

    def calculate_indexes_physical_development(self, anthropometric_data: dict[str, list[Model] | list[int] | list[float]], user_age: int) -> dict[str, list[float]]:
        anthropometric_data = deepcopy(anthropometric_data)
        anthropometric_data["age"] = [user_age] * self.count_semester
        result = {
            "height_index": [],
            "life_index": [],
            "strength_index": [],
            "stan_index": [],
            "apsk_index": [],
            "krempton_index": [],
            "vik_index": [],
            "endurance_index": [],
            "ufs_index": [],
            "robinson_index": [],
            "weight_index": []
        }
        formulas = {
            "height_index": lambda weight, height: weight * 1000 / height,
            "life_index": lambda vital_capacity, weight: vital_capacity / weight,
            "strength_index": lambda left_hand_strength, right_hand_strength, weight: ((left_hand_strength + right_hand_strength) / 2) / weight * 100,
            "stan_index": lambda strength, weight: strength / weight * 100,
            "apsk_index": lambda chs, ads, add, weight, height, age: (0.011 * chs) + (0.014 * ads) + (0.008 * add) + (0.009 * weight) - (0.009 * height) + (0.014 * age) - 0.27,
            "krempton_index": lambda ads, chs: 3.15 + ads - (chs / 20),
            "vik_index": lambda add, chs: (1 - add / chs) * 100,
            "endurance_index": lambda chs, ads, add: (chs * 100) / (ads - add),
            "ufs_index": lambda chs, age, height, add: 700 - (3 * chs) - (2.5 * add) - (2.7 * age) + (0.28 * age) / 350 - (2.6 * age) + (0.21 * height),
            "robinson_index": lambda chs, ads: chs * ads / 100,
            "weight_index": lambda weight, height: weight / (height / 100 * height * 100)
        }
        needs_parameters = {
            "height_index": ("weight", "height"),
            "life_index": ("vital_capacity", "weight"),
            "strength_index": ("left_hand_strength", "right_hand_strength", "weight"),
            "stan_index": ("strength", "weight"),
            "apsk_index": ("chs", "ads", "add", "weight", "height", "age"),
            "krempton_index": ("ads", "chs"),
            "vik_index": ("add", "chs"),
            "endurance_index": ("chs", "ads", "add"),
            "ufs_index": ("chs", "age", "height", "add"),
            "robinson_index": ("chs", "ads"),
            "weight_index": ("weight", "height")
        }
        for key in result:
            for semester in range(1, self.count_semester + 1):
                try:
                    parameters = (anthropometric_data[parameter][semester - 1] for parameter in needs_parameters[key])
                    result[key].append(round(formulas[key](*parameters), 2))
                except Exception:
                    result[key].append(None)

        return result


class FunctionalTableControllers(PhysicalTableControllers):
    def __init__(self, table_class: Type[Model], not_exists_fields: Tuple[str]):
        super().__init__(table_class, not_exists_fields)


class ProfileControllers:
    def __init__(self, anthropometric_table_controllers: AnthropometricTableControllers, functional_table_controllers: FunctionalTableControllers):
        self.anthropometric_table_controllers = anthropometric_table_controllers
        self.functional_table_controllers = functional_table_controllers


    def get_profile_context(self, user: CustomUser, request: HttpRequest) -> dict:
        context = {
            "is_own": user.id == request.user.id,
            "profile_user": user,
            "course": user.get_course(),
            "age": user.get_age_caption(),
            "count": range(1, 9),
            "user": request.user,
            "title": f"{user.last_name} {user.first_name}",
            "gender": "Мужской" if user.gender == "male" else "Женский"
        }
        antropometric_data = self.anthropometric_table_controllers.get_table(user)
        context.update(antropometric_data)
        context.update(self.anthropometric_table_controllers.calculate_indexes_physical_development(antropometric_data, user.get_age()))
        functional_data = self.functional_table_controllers.get_table(user)
        context.update(functional_data)
        return context
