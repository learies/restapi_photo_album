from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import AlbumViewSet, UserViewSet

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, 'user')
router_v1.register('albums', AlbumViewSet, 'album')

urlpatterns = (
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
)
