from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("accounts/login/", views.login, name="login"),  # Custom login view
    path("accounts/register/", views.register, name="register"),
    path("accounts/logout/", views.logout, name="logout"),
]
