from django.urls import path
from appsecundaria import views

urlpatterns = [
    path("", views.Index_vista,name="Index_vista"),
]