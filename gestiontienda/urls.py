from django.urls import path, include
from gestiontienda.views import *

urlpatterns = [
    path('admin/', include('django.contrib.auth.urls')),
    path('productos', productos),
    path('crearproducto', crearproducto),
    path('editarproducto/<int:id>', editarproducto),
    path('cambiarestadoproductos/<int:id>', cambiarestadoproductos),
    path('cambiarestadoservicios/<int:id>', cambiarestadoservicios),
    path('servicios', servicios),
    path('crearservicio', crearservicio),
    path('editarservicio/<int:id>', editarservicio),
    path('datostienda', datostienda),
    path('pedidoscarrito', pedidoscarrito),
    path('verdetallepedido/<int:id>', verdetallepedido),
    path('detallepedido', detallepedido),
    path('editarpedidocarrito/', pedidoscarrito),
    path('editarpedidocarrito/<int:id>', editarpedidocarrito),
    path('pedidosservicio', pedidosservicio),
    path('editarpedidoservicio/', pedidosservicio),
    path('editarpedidoservicio/<int:id>', editarpedidoservicio),
    path('datostienda', datostienda),
    path('editardatostienda', editardatostienda)
]
