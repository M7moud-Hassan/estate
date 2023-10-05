from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render

from projects.models import Projects


# Create your views here.
def reports(request):
    projects = []
    if request.method == 'POST':
        
        start_date = request.POST.get('start')
        end_date = request.POST.get('end')
        try:
            start_date = datetime.strptime(start_date, '%d-%m-%Y').strftime('%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%d-%m-%Y').strftime('%Y-%m-%d')
        except ValueError:
            return render(request, 'error_template.html', {'error_message': 'Invalid date format'})

        projects = Projects.objects.filter(date_work__range=[start_date, end_date])
    else:
        projects = Projects.objects.all()
        for p in projects:
           p.sum_price_mostakhlas_after= p.mostakhlas.all().aggregate(sum=Sum('price_mostakhlas_after'))['sum']
           p.sum_actual_extract_value= p.mostakhlas.all().aggregate(sum=Sum('actual_extract_value'))['sum']
           p.sum_discount= p.mostakhlas.all().aggregate(sum=Sum('discount'))['sum']
    return render(request,'reports/index.html', context={"projects": projects})


def mos_report(request):
    #projects = []
    # if request.method == 'POST':
    #     start_date = request.POST.get('start')
    #     end_date = request.POST.get('end')
    #     try:
    #         start_date = datetime.strptime(start_date, '%d %b, %Y').strftime('%Y-%m-%d')
    #         end_date = datetime.strptime(end_date, '%d %b, %Y').strftime('%Y-%m-%d')
    #     except ValueError:
    #         return render(request, 'error_template.html', {'error_message': 'Invalid date format'})

    #     projects = Projects.objects.filter(date_work__range=[start_date, end_date])

    # else:
    projects = Projects.objects.all()
    for p in projects:
           p.sum_price_mostakhlas_after= p.mostakhlas.all().aggregate(sum=Sum('price_mostakhlas_after'))['sum']
           p.sum_actual_extract_value= p.mostakhlas.all().aggregate(sum=Sum('actual_extract_value'))['sum']
           p.sum_discount= p.mostakhlas.all().aggregate(sum=Sum('discount'))['sum']
    return render(request, 'reports/deductions.html', context={"projects": projects})
