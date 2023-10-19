from django.shortcuts import render, redirect

from projects.models import Projects
from .form import EngineersForm
from .models import Engineers
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def engineers(request):
    context = {
        "engineers": Engineers.objects.all()
    }
    return render(request, 'engineers/index.html', context=context)

@login_required
def add(request):
    form = EngineersForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            engineer = form.save(commit=False)
            engineer.save()
            messages.success(request, 'تم اضافة البيانات بنجاح')
            return redirect('/mtm-group/engineers/')
    context = {
        "form": form
    }

    return render(request, 'engineers/add.html', context=context)

@login_required
def edit(request, pk):
    eng = Engineers.objects.filter(id=pk).first()
    if eng:
        if request.method == 'POST':
            form = EngineersForm(request.POST, instance=eng)
            if form.is_valid():
                form.save()
                messages.success(request, 'تم تحديث البيانات بنجاح')
                return redirect('/mtm-group/engineers/')

        form = EngineersForm(instance=eng)
        return render(request, 'engineers/add.html', context={'form': form, 'engineer': eng})

    else:
        messages.error(request, 'المهندس الذي تريد تعديله ليس موجود')
        return redirect('/mtm-group/engineers/')

@login_required
def delete(request, pk):
    eng = Engineers.objects.filter(id=pk).first()
    if eng:

            eng.delete()
            messages.success(request, 'تم مسح البيانات بنجاح')
            return redirect('/mtm-group/engineers/')
       
    else:
        messages.error(request, 'المهندس الذي تريد مسحة ليس موجود')
        return redirect('/mtm-group/engineers/')

@login_required
def details(request,pk):
    engineer=Engineers.objects.filter(id=pk).first()
    if engineer:
        projects=Projects.objects.filter(Q(ahdaa__engineer_id=engineer) |Q(masourfats__bain_masrouf=engineer) | Q(mostakhlas__engineer_id=engineer) ).distinct()
        ahdaa=[]
        masrouf=[]
        moustakhlas=[]
        for project in projects:
            ahdaa=project.ahdaa.filter(engineer_id=engineer)
            masrouf=project.masourfats.filter(bain_masrouf=engineer)
            moustakhlas=project.mostakhlas.filter(engineer_id=engineer)
        return render(request,'engineers/details_engineer.html',context={"engineer":engineer,"projects":projects,"masrouf":masrouf,"ahdaa":ahdaa,"moustakhlas":moustakhlas})
    else:
        messages.error("المهندس ليس موجود")
        return  redirect("/mtm-group/engineers/")