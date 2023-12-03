from users.models import CustomUser


class UserService:
    @staticmethod
    def get(username: str) -> CustomUser:
        return CustomUser.objects.filter(username=username).first()
