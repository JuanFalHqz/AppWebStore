from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from PuntoDeVenta.form import *
from PuntoDeVenta.models import ModelPuntoDeVenta, ModelProducto

 
class PuntoDeVentaList(ListView):
    template_name = 'puntosDeVenta.html'
    model = ModelPuntoDeVenta
    @method_decorator(csrf_exempt,login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    '''def post(self,request,*args,**kwargs):
        print(request.POST)
        data={}
        try:
            data=ModelPuntoDeVenta.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
             data['err']= str(e)
        print(JsonResponse(data))
        return JsonResponse(data)'''

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Puntos de venta'
        context['button_new']= 'Punto de venta'
        lista={}
        data1=ModelPuntoDeVenta.objects.all()
        return context

class PuntoDeVentaDetail(DetailView):
    template_name = 'detailPuntoDeVenta.html'
    model = ModelPuntoDeVenta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Punto de venta'
        context['button_new'] = 'Punto de venta'
        context['success_url'] = reverse_lazy('puntos_de_venta')
        return context

class PuntoDeVentaCreateView(CreateView):
    model = ModelPuntoDeVenta
    template_name = 'createPuntoDeVenta.html'
    form_class = FormPuntoDeVenta
    success_url = reverse_lazy('puntos_de_venta')

    def post(self, request, *args, **kwargs):
        form=FormPuntoDeVenta(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            context=self.get_context_data(**kwargs)
            context['form']=form
            render(request,self.template_name,context)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Nuevo punto de venta'
        context['button_new']= 'Punto de venta'
        context['action'] = 'add'
        context['var_url'] ='puntos_de_venta_create'#pendiente a cambiar nombre de variable
        context['success_url'] = reverse_lazy('puntos_de_venta')
        return context

class PuntoDeVentaUpdateView(UpdateView):
    model = ModelPuntoDeVenta
    template_name = 'createPuntoDeVenta.html'
    form_class = FormPuntoDeVenta
    success_url = reverse_lazy('puntos_de_venta')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Actualización del punto de venta'
        context['button_new']= 'Punto de venta'
        return context

class PuntoDeVentaDeleteView(DeleteView):
    model = ModelPuntoDeVenta
    template_name = 'delete.html'
    success_url = reverse_lazy('puntos_de_venta')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Eliminar punto de venta'
        context['button_new']= 'Punto de venta'
        context['success_url'] = reverse_lazy('puntos_de_venta')
        return context


class ProductosList(ListView):
    template_name = 'listProductos.html'
    model = ModelProducto

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Todos los productos'
        context['button_new']="Producto"
        context['productos']=ModelProducto.objects.all()
        return context

class ProductoCreateView(CreateView):
    model = ModelProducto
    template_name = 'createProducto.html'
    form_class = FormProductos
    success_url = reverse_lazy('products')


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Nuevo producto'
        context['button_new']= 'Producto'
        context['success_url'] = reverse_lazy('products')
        return context

class ProductoUpdateView(UpdateView):
    model = ModelProducto
    template_name = 'createProducto.html'
    form_class = FormProductos
    success_url = reverse_lazy('products')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Actualización del producto'
        context['button_new']= 'Producto'
        return context

class ProductDeleteView(DeleteView):
    model = ModelProducto
    template_name = 'delete.html'
    success_url = reverse_lazy('products')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Eliminar producto'
        context['button_new']= 'Producto'
        context['success_url'] = reverse_lazy('products')
        return context

class VentaCreate(CreateView):
    model = Venta
    template_name = 'createVenta.html'
    form_class = FormVenta
