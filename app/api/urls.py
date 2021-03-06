from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import AlbumViewSet, PhotoViewSet, UserViewSet

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, 'user')
router_v1.register('albums', AlbumViewSet, 'album')
router_v1.register('photos', PhotoViewSet, 'photo')
router_v1.register(
    r'albums/(?P<album_id>\d+)/photos',
    PhotoViewSet,
    basename='photoalbum',
)

urlpatterns = (
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
)
