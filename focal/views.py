from django.shortcuts import render
from .models import Mission

# Create your views here.

def home(request):
    return render(request, 'focal/home.html')


def missions(request):
    missions = Mission.objects.order_by('date_added')
    context = {'missions': missions}
    return render(request, 'focal/missions.html', context)
