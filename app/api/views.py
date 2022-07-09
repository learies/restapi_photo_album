from django.contrib.auth import get_user_model
from django.db.models.aggregates import Count

from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import viewsets

from albums.models import Album, Photo
from api.serializers import AlbumSerializer, PhotoSerializer, UserSerializer

User = get_user_model()


class UserViewSet(DjoserUserViewSet):
    """ViewSet для работы с пользователями."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с альбомами."""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        """Метод добавит автора к альбому."""
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """Метод выведет только список альбомов автора."""
        return self.queryset.filter(
            author=self.request.user
        ).annotate(photo_count=Count('photo'))


class PhotoViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с фотографиями."""
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
