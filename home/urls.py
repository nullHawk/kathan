from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scaler/translate', views.translate, name='translate')
]