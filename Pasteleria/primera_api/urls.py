"""primera_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from primera_api.app_api import views
from django.conf import settings
from django.conf.urls.static import static
from tienda.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, sumar_producto ,registro

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'direccion', views.DireccionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manage/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', 
        namespace='rest_framework')),
    path('', include('tienda.urls')),
    path('gallery/', include('tienda.urls')),
    path('home/', include('tienda.urls')),
    path('', include('tienda.urls')),
    path('', include('tienda.urls')),
    path('', include('tienda.urls')),
    path('registro/', registro, name="registro"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('sumar/<int:producto_id>/', sumar_producto, name="Sumar"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)