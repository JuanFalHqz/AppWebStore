from django.forms import ModelForm, ValidationError

from PuntoDeVenta.models import ModelPuntoDeVenta, ModelProducto,Venta,Cliente


class FormPuntoDeVenta(ModelForm):
    class Meta:
        model= ModelPuntoDeVenta
        fields='__all__'
        #exclude

class FormProductos(ModelForm):
    class Meta:
        model= ModelProducto
        fields='__all__'
        #exclude

class FormVenta(ModelForm):

    class Meta:
        model=Venta
        fields="__all__"

