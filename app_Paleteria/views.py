from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Producto, Venta
from django.utils import timezone

# =====================================
# INICIO
# =====================================
def inicio_paleteria(request):
    return render(request, 'inicio.html')


# =====================================
# CRUD CLIENTE
# =====================================
def agregar_cliente(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']
        fecha_registro = timezone.now().date()

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            direccion=direccion,
            ciudad=ciudad,
            fecha_registro=fecha_registro
        )
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')


def ver_cliente(request):
    clientes = Cliente.objects.all().order_by('id_cliente')
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})


def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})


def realizar_actualizacion_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == "POST":
        # Usar get() evita KeyError si falta el campo
        cliente.nombre = request.POST.get('nombre', cliente.nombre).strip()
        cliente.apellido = request.POST.get('apellido', cliente.apellido).strip()
        cliente.telefono = request.POST.get('telefono', cliente.telefono).strip()
        cliente.email = request.POST.get('email', cliente.email).strip()
        cliente.direccion = request.POST.get('direccion', cliente.direccion).strip()

        # **IMPORTANTE**: asignar la ciudad al cliente (era lo que faltaba)
        cliente.ciudad = request.POST.get('ciudad', cliente.ciudad).strip()

        fecha_registro = request.POST.get('fecha_registro', '').strip()
        if fecha_registro:
            cliente.fecha_registro = fecha_registro  # Solo si no está vacío
        # Guardar cambios
        cliente.save()
        return redirect('ver_cliente')

    return redirect('ver_cliente')

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# =====================================
# CRUD PRODUCTO
# =====================================
def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        sabor = request.POST['sabor']
        precio = request.POST['precio']
        stock = request.POST['stock']
        tipo = request.POST['tipo']
        fecha_elaboracion = request.POST['fecha_elaboracion']
        

        Producto.objects.create(
            nombre=nombre,
            sabor=sabor,
            precio=precio,
            stock=stock,
            tipo=tipo,
            fecha_elaboracion=fecha_elaboracion,
           
        )
        return redirect('ver_producto')
    return render(request, 'producto/agregar_producto.html')


def ver_producto(request):
    productos = Producto.objects.all().order_by('id_producto')
    return render(request, 'producto/ver_producto.html', {'productos': productos})


def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    return render(request, 'producto/actualizar_producto.html', {'producto': producto})


def realizar_actualizacion_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == "POST":
        producto.nombre = request.POST['nombre']
        producto.sabor = request.POST['sabor']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.tipo = request.POST['tipo']

        fecha_elaboracion = request.POST.get('fecha_elaboracion', '').strip()
        # Si el campo viene vacío, no se intenta guardar como fecha
        if fecha_elaboracion:
            producto.fecha_elaboracion = fecha_elaboracion  

        producto.save()
        return redirect('ver_producto')
    return redirect('ver_producto')

def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


# =====================================
# CRUD VENTA
# =====================================
def agregar_venta(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    if request.method == "POST":
        fecha_venta = timezone.now().date()
        cantidad = int(request.POST['cantidad'])
        metodo_pago = request.POST['metodo_pago']
        estado = request.POST['estado']
        observaciones = request.POST['observaciones']
        id_cliente = request.POST['id_cliente']
        id_producto = request.POST['id_producto']

        cliente = Cliente.objects.get(id_cliente=id_cliente)
        producto = Producto.objects.get(id_producto=id_producto)
        total = producto.precio * cantidad

        Venta.objects.create(
            fecha_venta=fecha_venta,
            cantidad=cantidad,
            total=total,
            metodo_pago=metodo_pago,
            estado=estado,
            observaciones=observaciones,
            id_cliente=cliente,
            id_producto=producto
        )
        return redirect('ver_venta')
    return render(request, 'venta/agregar_venta.html', {'clientes': clientes, 'productos': productos})


def ver_venta(request):
    ventas = Venta.objects.select_related('id_cliente', 'id_producto').all().order_by('id_venta')
    return render(request, 'venta/ver_venta.html', {'ventas': ventas})


def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'venta/actualizar_venta.html', {'venta': venta, 'clientes': clientes, 'productos': productos})


def realizar_actualizacion_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    if request.method == "POST":
        venta.cantidad = int(request.POST['cantidad'])
        venta.metodo_pago = request.POST['metodo_pago']
        venta.estado = request.POST['estado']
        venta.observaciones = request.POST['observaciones']
        id_cliente = request.POST['id_cliente']
        id_producto = request.POST['id_producto']

        venta.id_cliente = Cliente.objects.get(id_cliente=id_cliente)
        venta.id_producto = Producto.objects.get(id_producto=id_producto)
        venta.total = venta.id_producto.precio * venta.cantidad
        venta.save()
        return redirect('ver_venta')
    return redirect('ver_venta')


def borrar_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_venta')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})
