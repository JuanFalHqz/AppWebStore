from builtins import set
from pyexpat import model

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import *
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from User.models import User


class Login_View(FormView):
    form_class = AuthenticationForm
    template_name = 'Login.html'
    success_url = reverse_lazy("template_home")


    def dispatch(self, request, *args, **kwargs):
        if (request.user.is_authenticated):#si hay un usuario autenticado
            return redirect('template_dashboard') #redirecciona a esta pag
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.success_url)

class Logout_View(LogoutView):
    next_page = 'template_login'
