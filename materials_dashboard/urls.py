
from django.urls import path

from materials_dashboard import views

urlpatterns = [
    path('', views.index, name='index')
]
