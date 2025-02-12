from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.logar, name='login'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('social/', include('allauth.socialaccount.urls')),
]