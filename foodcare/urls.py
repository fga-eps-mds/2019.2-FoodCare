from django.contrib import admin
from django.urls import path, include
from evento.views import EventoViewSet
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from doadores.views import DoadoresViewSet
from evento.views import EventoViewSet

router = routers.DefaultRouter()
router.register(
    'evento', EventoViewSet, base_name='evento'
)

router_doador = routers.DefaultRouter()
router_doador.register(
    'doadores',DoadoresViewSet, base_name='doadores'
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
    path('', include(router_doador.urls)),

]
