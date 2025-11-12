from django.urls import path
from . import views

urlpatterns = [
    # --- INICIO ---
    path('', views.inicio_paleteria, name='inicio_paleteria'),

    # --- CLIENTE ---
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_cliente, name='ver_cliente'),
    path('cliente/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # --- PRODUCTO ---
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/ver/', views.ver_producto, name='ver_producto'),
    path('producto/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),

    # --- VENTA ---
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/ver/', views.ver_venta, name='ver_venta'),
    path('venta/actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta'),
    path('venta/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('venta/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),
]

