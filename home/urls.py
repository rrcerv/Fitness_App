from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='main_page'),
    path('fitness_app/', views.home, name='home'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('fitness_app/?status=1', views.gerar_treinoa, name='gerar_treinoa'),
    path('fitness_app/?status=2', views.gerar_treinob, name='gerar_treinob'),
    path('fitness_app/?status=3', views.gerar_treinoc, name='gerar_treinoc'),
]