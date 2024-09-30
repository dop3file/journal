from profiles.controllers import ProfileControllers
from users.models import CustomUser, StudentGroup


def get_users_choices() -> list:
    groups = StudentGroup.objects.all()
    result_form_choices = []
    for group in groups:
        users_from_group = CustomUser.objects.filter(group=group).all()
        result_form_choices.append(
            (
                group.title,
                (
                    [(user.id, f"{user.last_name} {user.first_name}") for user in users_from_group]
                ),
            )
        )

    return result_form_choices


class GroupControllers:
    def __init__(
            self, profile_controllers: ProfileControllers
    ):
        self.profile_controllers = profile_controllers

    def get_group_context(self, group_id: int) -> dict:
        users = CustomUser.objects.filter(group_id=group_id).all()
        context = {}
        for user in users:
            if not context:
                antropometric_data = self.profile_controllers.anthropometric_table_controllers.get_table(user)
                context.update(antropometric_data)
                context.update(
                    self.profile_controllers.anthropometric_table_controllers.calculate_indexes_physical_development(
                        antropometric_data,
                        user.get_age()))
                functional_data = self.profile_controllers.functional_table_controllers.get_table(user)
                context.update(functional_data)
                physicals_data = self.profile_controllers.physicals_standards.get_table(user)
                context.update(physicals_data)
            else:
                antropometric_data = self.profile_controllers.anthropometric_table_controllers.get_table(user)
                self.merge_tables(context, antropometric_data)
                self.merge_tables(
                    context,
                    self.profile_controllers.anthropometric_table_controllers.calculate_indexes_physical_development(
                        antropometric_data, user.get_age())
                )
                functional_data = self.profile_controllers.functional_table_controllers.get_table(user)
                self.merge_tables(context, functional_data)
                physicals_data = self.profile_controllers.physicals_standards.get_table(user)
                self.merge_tables(context, physicals_data)

        self.divide_table(context, len(users))

        return context

    def merge_tables(self, table1: dict, table2: dict) -> dict:
        for key, value in table2.items():
            table1[key] = [x + y if x is not None and y is not None else y if x is None else x for (x, y) in zip(table1[key], table2[key])]
        return table1

    def divide_table(self, table: dict[str, float | None], count: int) -> dict:
        for key, value in table.items():
            table[key] = [x / count if x is not None else None for x in table[key]]
        return table
