from django.urls import path
from . import views

app_name = 'focal'

urlpatterns = [
    path('', views.home, name='home'),
]
