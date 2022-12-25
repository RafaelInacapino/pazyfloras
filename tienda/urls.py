from django.urls import path, include
from tienda.views import *

app_name = "tienda"

urlpatterns = [
    #Public Info
    path('index', index),
    path('', index),
    path('productos', productos),
    path('vasijas', vasijas),
    path('maceteros', maceteros),
    path('plantas', plantas),
    path('servicios', servicios),
    path('quienessomos', quienessomos),
    path('contacto', contacto),

    #Accounts Session System 
    path('cuenta/', include('django.contrib.auth.urls')),
    
    #Account Info
    path('cuenta/carrito', carrito),
    path('agregarProducto/<int:id>', agregarProducto),
    path('eliminarProducto/<int:id>', eliminarProducto),
    path('pedirCarrito', pedirCarrito), 
    path('pedirServicio/<int:id>', pedirServicio), 
    path('cuenta/perfil', perfil),
    path('cuenta/registro', registro), 
    path('cuenta/mispedidos', perfilpedidos), 
    path('cuenta/verdetallepedido/<int:id>', verdetallepedido),
    path('cuenta/detallepedido', perfildetallepedido),
    path('cuenta/misservicios', perfilservicios),
    path('cuenta/verdetalleservicio/<int:id>', verdetalleservicio),
    path('cuenta/detalleservicio', perfildetalleservicio),
    path('cuenta/pagarpedidoproductos/pagar/<int:id>', perfilpagarcarritopagar),
    path('cuenta/pagarpedidoproductos/webpay/<int:id>', perfilpagarcarritowebpay),
    path('cuenta/pagarpedidoproductos/pagado/<int:id>', perfilpagarcarritopagado),
    path('cuenta/pagarpedidoservicio/pagar/<int:id>', perfilpagarserviciopagar),
    path('cuenta/pagarpedidoservicio/webpay/<int:id>', perfilpagarserviciowebpay),
    path('cuenta/pagarpedidoservicio/pagado/<int:id>', perfilpagarserviciopagado),
    
]
