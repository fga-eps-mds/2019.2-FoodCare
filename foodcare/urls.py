from django.contrib import admin
from django.urls import path, include
from evento.views import EventoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    'evento', EventoViewSet, base_name='evento'
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
