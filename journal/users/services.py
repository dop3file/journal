from typing import Any

from users.models import CustomUser, StudentGroup
from .misc import UserNotFound, GroupNotFound


class UserService:
    def get(self, id: int) -> CustomUser:
        user = CustomUser.objects.filter(id=id).first()
        if user is None:
            raise UserNotFound(db_id=id)
        return user

    def get_group(self, id: int) -> StudentGroup:
        group = StudentGroup.objects.filter(id=id).first()
        if group is None:
            raise GroupNotFound(db_id=id)
        return group

    def edit_group(self, id: int, group_id: int):
        user = self.get(id)
        group = self.get_group(group_id)
        user.group = group
        user.save()
