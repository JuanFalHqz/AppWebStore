from django.urls import path
from User.views import *
urlpatterns = [
    path('change_pass/',UserChangePasswordView.as_view(), name = 'template_chang_pass'),
    path('profile_edit/<int:pk>/',UserProfileEditView.as_view(), name = 'template_proofile_edit'),
]