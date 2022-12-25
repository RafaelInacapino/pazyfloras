from django.contrib import admin
from tienda.models import Producto, Servicio, PedidoCarrito, PedidoServicio, CarritoBoleta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(PedidoCarrito)
admin.site.register(CarritoBoleta)
admin.site.register(PedidoServicio)