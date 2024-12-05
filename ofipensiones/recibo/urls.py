from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.recibo_view, name='recibo_view')
]