from .models import Anthropometric
from users.models import CustomUser


def get_anthropometric(user: CustomUser) -> dict[str, Anthropometric]:
    return {str(i): anthro_record for (i, anthro_record) in enumerate(Anthropometric.objects.filter(user=user).all())}