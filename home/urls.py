from django.urls import path
from . import views

urlpatterns = [
    path('kathan', views.index, name='index'),
    path('scaler/translate', views.translate)
]