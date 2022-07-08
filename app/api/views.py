from django.contrib.auth import get_user_model

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


class PhotoViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с фотографиями."""
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
