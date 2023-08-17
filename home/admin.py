from django.contrib import admin
from .models import Configuracoes, Usuario_Treinos, Exercicios, Curiosidades

admin.site.register(Configuracoes)
admin.site.register(Usuario_Treinos)
admin.site.register(Exercicios)
admin.site.register(Curiosidades)