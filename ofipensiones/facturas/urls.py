from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.factura_view, name='factura_view'),
    path('delete/<int:id>', views.facturas_view, name='factura_view')
]
