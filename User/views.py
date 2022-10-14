from pyexpat import model

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from User.form import UserChangePasswordForm, UserForm
from User.models import User


class UserChangePasswordView(LoginRequiredMixin,FormView):
    model = User
    form_class = UserChangePasswordForm
    template_name = 'changePassword.html'
    success_url = reverse_lazy('template_login')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Cambio de contraseña'
        return context

class UserProfileEditView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserForm
    template_name = 'profile.html'
    success_url = reverse_lazy('template_home')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)


    def get_context_data(self, **kwargs):
        print(self.request)

        context=super().get_context_data(**kwargs)
        context['title']='Editar Perfil'
        return context
