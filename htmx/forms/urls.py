from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form/email", views.email, name="email"),
    path("form/phone", views.phone, name="phone"),
]
