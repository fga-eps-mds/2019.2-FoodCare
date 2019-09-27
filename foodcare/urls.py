from django.contrib import admin
from django.urls import path, include
from evento.views import EventoViewSet, AlimentoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    'evento', EventoViewSet, base_name='evento'
)

router_alimento = routers.DefaultRouter()
router_alimento.register(
    'alimento', AlimentoViewSet, base_name='alimento'
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('', include(router_alimento.urls)),
    #path('evento/', include('evento.urls'))
]
