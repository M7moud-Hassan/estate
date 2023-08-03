from django.shortcuts import render

from projects.models import Projects


# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def projects(request):
    return render(request, 'home/projects.html',context={'projects':Projects.objects.all()})
