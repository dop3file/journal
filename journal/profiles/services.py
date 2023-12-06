from users.models import CustomUser


class UserService:
    @staticmethod
    def get(id: int) -> CustomUser:
        return CustomUser.objects.filter(id=id).first()
