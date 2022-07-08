from django.contrib.auth import get_user_model

from rest_framework import serializers

from albums.models import Album

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


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""
    author = serializers.StringRelatedField(read_only=True)
    created = serializers.DateTimeField(
        format='%d.%m.%Y %H:%M',  # out: "07.07.2022 19:06"
        read_only=True,
    )

    class Meta:
        model = Album
        fields = (
            'id',
            'name',
            'author',
            'created',
        )
