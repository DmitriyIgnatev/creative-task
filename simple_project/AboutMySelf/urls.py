from django.urls import path
from . import views

app_name = 'name'

urlpatterns = [
    path(r'', views.index, name='index'),
]