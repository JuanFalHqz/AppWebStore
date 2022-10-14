from django.urls import path
from PuntoDeVenta.views import *

urlpatterns = [
    path('puntos/', PuntoDeVentaList.as_view(), name='puntos_de_venta'),
    path('puntos/<int:pk>/', PuntoDeVentaDetail.as_view(), name='punto_de_venta'),
    path('puntos/create/', PuntoDeVentaCreateView.as_view(), name='puntos_de_venta_create'),
    path('puntos/edit/<int:pk>/',PuntoDeVentaUpdateView.as_view(),name='puntos_de_venta_edit'),
    path('puntos/delete/<int:pk>',PuntoDeVentaDeleteView.as_view(),name='puntos_de_venta_delete'),

    path('productos/',ProductosList.as_view(),name='products'),
    path('productos/create',ProductoCreateView.as_view(),name='products_crate'),
    path('productos/edit/<int:pk>',ProductoUpdateView.as_view(),name='products_edit'),
    path('productos/delete/<int:pk>',ProductDeleteView.as_view(),name='products_delete'),

    path('venta/', VentaCreate.as_view(), name="venta_create")

]
