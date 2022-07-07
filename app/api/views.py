from django.contrib.auth import get_user_model

from djoser.views import UserViewSet as DjoserUserViewSet

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(DjoserUserViewSet):
    """ViewSet для работы с пользователями."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
