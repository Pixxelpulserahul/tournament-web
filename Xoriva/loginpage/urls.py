from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login/", views.login_view, name='login'),
    path("success/", views.success_view, name='success'),
    path("signup/", views.signup_view, name="signup"),
    path("signup_Home/", views.signup_home, name="signup_Home")
]
