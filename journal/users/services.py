from typing import Any

from users.models import CustomUser, StudentGroup


class UserService:
    EDITABLE_FIELDS = ("group",)

    @staticmethod
    def get(id: int) -> CustomUser:
        return CustomUser.objects.filter(id=id).first()

    @classmethod
    def edit_group(cls, id: int, group_id: int):
        user = CustomUser.objects.filter(id=id).first()
        user.group = StudentGroup.objects.filter(id=group_id).first()
        user.save()
