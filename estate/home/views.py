from django.shortcuts import redirect, render

from projects.models import Projects
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
@login_required
def home(request):
    return render(request, 'home/index.html')

@login_required
def projects(request):
    return render(request, 'home/projects.html',context={'projects':Projects.objects.all()})
@login_required

def log_out(request):
    logout(request)
    return redirect('/mtm-group/account/login_view/')
    
def mos_report(request):
    pass