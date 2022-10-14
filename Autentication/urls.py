from django.urls import path
from Autentication.views import Login_View, Logout_View

urlpatterns = [
    path('', Login_View.as_view(), name='template_login'),
    path('logout/', Logout_View.as_view(next_page='template_login'), name='template_logout'),
]
