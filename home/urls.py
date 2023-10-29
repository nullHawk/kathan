from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('scaler/translate', views.translate)
]