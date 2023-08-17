from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('cadastrar/', views.signup, name='signup'),
    path('validate_signup/', views.validate_signup, name='validate_signup'),
    path('login/', views.login, name='login'),
    path('validate_login/', views.validate_login, name='validate_login'),
    path('sair/', views.sair, name='sair')
]