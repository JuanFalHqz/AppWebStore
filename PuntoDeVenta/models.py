from django.db import models
from django.db.models import ManyToOneRel
from django.forms import model_to_dict

from Tienda.settings import MEDIA_URL, STATIC_URL
from User.models import User
# Create your models here.

class ModelProducto(models.Model):
    name=models.CharField(verbose_name="Nombre ",max_length=100,null=True,blank=True)
    descriptions=models.TextField(verbose_name='Descripción ',max_length=300,null=True,blank=True)
    bar_code=models.TextField(verbose_name='Código de barras', unique=True)
    price=models.FloatField(verbose_name='Precio ',null=True, blank=True)
    price_max = models.FloatField(verbose_name='Precio máximo: ', null=True, blank=True)
    price_min=models.FloatField(verbose_name='Precio mínimo ',null=True, blank=True)
    stock=models.PositiveIntegerField(verbose_name='Cantidad')
    exist=models.PositiveBigIntegerField(verbose_name='Existencia',default=0)
    image=models.ImageField(verbose_name='Imágenes',upload_to="product/%Y/%m/%d",null=False,blank=True)
    def getImage(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL,self.image)
        return '{}{}'.format(STATIC_URL,'dist/img/AdminLTELogo.png')
    class Meta:
        verbose_name="Producto"
        verbose_name_plural='Productos'
    def __str__(self):
        return self.name

    def toJSON(self):#Retorna el modelo en formato json
        return model_to_dict(self)

class ModelPuntoDeVenta(models.Model):
    name=models.CharField(verbose_name="Nombre ",max_length=100,null=True,blank=True)
    addres=models.CharField(verbose_name='Dirección ',max_length=150,null=True,blank=True)
    productos = models.ManyToManyField(ModelProducto)
    class Meta:
        verbose_name="Punto de venta"
        verbose_name_plural='Puntos de venta'
    def toJSON(self):
        return model_to_dict(self)
    def __str__(self):
        return self.name
'''class ProductoTienda(models.Model):
    products=models.ManyToManyField(ModelProducto)
    punto_de_venta=models.ManyToManyField(ModelPuntoDeVenta)
    stock=models.PositiveIntegerField(verbose_name='Cantidad')
    class Meta:
        verbose_name="Productos por punto de venta"
    def toJSON(self):
        return model_to_dict(self)'''
class Cliente(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100)
    address = models.CharField(verbose_name='Dirección', null=True, blank=True, max_length=100)
    movil = models.PositiveIntegerField(verbose_name='Teléfono')

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.name


class Venta(models.Model):
    total_price=models.FloatField(verbose_name='Precio total')
    pago=models.FloatField(verbose_name="Pago")
    date=models.DateField(verbose_name='Fecha')
    time=models.TimeField(verbose_name='Tiempo')
    cajero=models.ForeignKey(User,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    productos=models.ManyToManyField(
                                    ModelProducto,
                                     through="Productos_por_ventas",
                                     )

class Productos_por_ventas(models.Model):
    id_producto=models.ForeignKey(ModelProducto,on_delete=models.CASCADE)
    id_venta=models.ForeignKey(Venta,on_delete=models.CASCADE)
    cantidad=models.PositiveIntegerField(verbose_name="Cantidad",blank=False,null=False)
