from django.urls import path
from .views import home, gallery, carrito, index, tienda, registro
urlpatterns = [

    path('', index, name="index"),
    path('', home, name="home"),
    path('gallery', gallery, name="gallery"),
    path('carrito', carrito, name="carrito"),
    path('tienda', tienda, name="tienda"),
    path('registro', registro, name="registro"),

    #metodos
]