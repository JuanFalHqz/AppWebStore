from django.contrib import admin
from PuntoDeVenta.models import *
# Register your models here.
class Prod_por_ventas(admin.TabularInline):
    model = Productos_por_ventas
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    inlines = [Prod_por_ventas,]


admin.site.register(ModelPuntoDeVenta)
admin.site.register(ModelProducto)
admin.site.register(Cliente)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Productos_por_ventas)
