from django.urls import path,include
from Home.views import homeView

urlpatterns = [
    path('', homeView.as_view(),name='template_home'),
]
