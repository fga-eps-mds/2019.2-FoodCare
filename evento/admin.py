from django.contrib import admin
from .models import Evento, Alimento, Categoria

admin.site.register(Evento)
admin.site.register(Alimento)
admin.site.register(Categoria)