from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from evento.views import EventoViewSet
from users.views import UsuarioSerializerViewSet

router = routers.DefaultRouter()
router.register(
    'evento', EventoViewSet, base_name='evento'
)

router2 = routers.DefaultRouter()
router2.register(
    'user', UsuarioSerializerViewSet, base_name='usuario'
)


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
    path('',include('emailfood.urls')),
    path('', include(router.urls)),
    path('', include(router2.urls)),

]