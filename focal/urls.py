from django.urls import path
from . import views

app_name = 'focal'

urlpatterns = [
    path('', views.home, name='home'),
    path('missions', views.missions, name='missions' ),
    path('new_mission', views.new_mission, name="new_mission"),
]
