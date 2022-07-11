from django.contrib.auth import get_user_model

from rest_framework import serializers

from albums.models import Album, Photo, Tag
from api.validations import validate_image

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Создать пользователя с запрошенными полями."""
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug',
        )


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Album."""
    author = serializers.StringRelatedField()

    class Meta:
        model = Album
        fields = (
            'id',
            'name',
            'author',
            'photo_count',
            'created',
        )
        read_only_fields = ('author', 'created')


class PhotoSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Photo."""
    album = serializers.StringRelatedField()
    tag = serializers.StringRelatedField()
    image = serializers.ImageField(validators=[validate_image])

    class Meta:
        model = Photo
        fields = (
            'id',
            'album',
            'name',
            'image',
            'tag',
            'created',
        )
        read_only_fields = ('album', 'created')
