from django.contrib import admin
from .models import Cliente, Producto, Venta

# ==============================
# ADMIN CLIENTE
# ==============================
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'telefono', 'email', 'direccion', 'ciudad', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'telefono', 'email', 'ciudad')


# ==============================
# ADMIN PRODUCTO
# ==============================
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'sabor', 'precio', 'stock', 'tipo', 'fecha_elaboracion', 'descripcion')
    search_fields = ('nombre', 'sabor', 'tipo')


# ==============================
# ADMIN VENTA
# ==============================
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'fecha_venta', 'cantidad', 'total', 'metodo_pago', 'estado', 'id_cliente', 'id_producto')
    search_fields = ('id_cliente__nombre', 'id_producto__nombre', 'metodo_pago', 'estado')
