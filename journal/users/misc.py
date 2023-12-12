from dataclasses import dataclass


@dataclass
class EntityNotFound(Exception):
    db_id: int

    @property
    def message(self):
        raise NotImplementedError


class GroupNotFound(EntityNotFound):
    @property
    def message(self) -> str:
        return f"Группа с ID {self.db_id} не найдена"


class UserNotFound(EntityNotFound):
    @property
    def message(self) -> str:
        return f"Пользователь с ID {self.db_id} не найден"