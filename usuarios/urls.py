from django.urls import path
from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login_qr, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
  
]
