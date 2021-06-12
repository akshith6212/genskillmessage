from django.urls import path,include
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("login_genskill/", views.login_genskill, name="login_genskill"),
    path("register_genskill/", views.register_genskill, name="register_genskill"),
    path("logout/", views.logout, name="logout"),
]