from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciarSesion, name="Login"),
    path('home/', views.home, name="Home"),
    path('cerrarSesion/', views.cerrarSesion, name="Logout"),
]