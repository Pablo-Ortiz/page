from email import message
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from tienda.Carrito import Carrito
from tienda.models import Producto
from tienda.forms import CustomUserCreationForm


def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    url = 'http://127.0.0.1:8000/manage/productos/' 
    response = requests.get(url, auth = ('admin', 'duoc'))
    data = response.json()
    productos = {'productos': data}
    return render(request,'tienda.html', productos)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

# Create your views here.

def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'galeria.html')

def carrito(request):
    return render(request, 'carrito.html')

def index(request):
    return render(request, 'index.html')

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")
        data["form"]=formulario
    return render(request,'registration/registro.html',data)

def log_in(request):
    return render(request, 'registration/login.html')

