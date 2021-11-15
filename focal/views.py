from django.shortcuts import redirect, render
from .models import Mission
from .forms import MissionForm

# Create your views here.

def home(request):
    return render(request, 'focal/home.html')


def missions(request):
    missions = Mission.objects.order_by('date_added')
    context = {'missions': missions}
    return render(request, 'focal/missions.html', context)

def new_mission(request):
    if request.method != 'POST':
        form = MissionForm()
    else:
        form = MissionForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('focal:missions')
    
    context = {'form': form}
    return render(request, 'focal/new_mission.html', context)

