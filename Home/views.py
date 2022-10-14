from django.contrib.auth.decorators import login_required
from django.db.models import Model
from django.shortcuts import render
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from PuntoDeVenta.models import ModelProducto, Venta
from Tienda.settings import BASE_DIR,TEMPLATES,STATIC_URL

class DashboardView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = "Dashboard.html"

class homeView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cant_prod'] = ModelProducto.objects.count()
        context['cant_vent'] = Venta.objects.count()
        #me quede aca
        context['cant_trabajadores'] = Venta.objects.count()
        return context
