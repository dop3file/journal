from users.models import CustomUser, StudentGroup


def get_group_choices() -> list:
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