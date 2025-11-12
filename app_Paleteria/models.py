from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    apellido = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100, unique=True)
    fecha_registro = models.DateField(auto_now_add=True)
    ciudad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: PRODUCTO
# ==========================================
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    sabor = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    tipo = models.CharField(max_length=100)
    fecha_elaboracion = models.DateField()
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.sabor})"


# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, blank=True)
    observaciones = models.CharField(max_length=200, blank=True)
    
    # Relaciones
    id_cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')

    def __str__(self):
        return f"Venta {self.id_venta} - Cliente: {self.id_cliente.nombre} - Producto: {self.id_producto.nombre}"
