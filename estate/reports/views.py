from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render

from projects.models import Projects
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
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

@login_required
def mos_report(request,pk=0):
    if pk==0:
        projects = Projects.objects.all()
    else:
        projects = Projects.objects.filter(id=pk)
    for p in projects:
           p.sum_price_mostakhlas_after= p.mostakhlas.all().aggregate(sum=Sum('price_mostakhlas_after'))['sum']
           p.sum_actual_extract_value= p.mostakhlas.all().aggregate(sum=Sum('actual_extract_value'))['sum']
           p.sum_discount= p.mostakhlas.all().aggregate(sum=Sum('discount'))['sum']
    return render(request, 'reports/deductions.html', context={"projects": projects,"all_p":Projects.objects.all()})
@login_required
def durations_report(request,pk):
    if pk==0:
        projects = Projects.objects.all()
    else:
        projects = Projects.objects.filter(id=pk)
    return render(request, 'reports/durations.html', context={"projects": projects,"all_p":Projects.objects.all()})
@login_required
def masrouf_report(request,pk):
    if pk==0:
        projects = Projects.objects.all()
    else:
        projects = Projects.objects.filter(id=pk)
    return render(request, 'reports/masrouf.html', context={"projects": projects,"all_p":Projects.objects.all()})
@login_required
def details_report(request,pk):
    if pk==0:
        projects = Projects.objects.all()
    else:
        projects = Projects.objects.filter(id=pk)
    return render(request, 'reports/details.html', context={"projects": projects,"all_p":Projects.objects.all()})
@login_required
def finance_report(request,pk):
    if pk==0:
        projects = Projects.objects.all()
    else:
        projects = Projects.objects.filter(id=pk)
    return render(request, 'reports/finance.html', context={"projects": projects,"all_p":Projects.objects.all()})
@login_required
def ahdaa_report(request,pk):
    if pk==0:
        projects = Projects.objects.all()
    else:
        projects = Projects.objects.filter(id=pk)
    return render(request, 'reports/ahdaa.html', context={"projects": projects,"all_p":Projects.objects.all()})

@login_required
def mostkhlas_report(request,pk):
    summ=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    workforce=[]
    Combined_discount_rate=[]
    bank_ratio=[]
    engineering_stamp=[]
    others=[]
    taxes=[]
    altaminat=[]
    discount=[]
    other_deductions_1=[]
    other_deductions_2=[]
    commercial_ndustrial_profits_tax=[]
    value_added_tax=[]
    stamp_tax_division=[]
    martyrs_Honor_fund=[]
    resource_development_tax=[]
    long_Live_egypt_fund=[]
    applied_tear=[]
    union_of_two_sayings=[]
    if pk==0:
        projects = Projects.objects.all()
        if projects:
            pro=projects.first()
            for mo in pro.mostakhlas.all():
                    if summ[0]:
                        summ[0]=summ[0]+mo.actual_extract_value*(mo.workforce/100)
                    else:
                        summ[0]=mo.actual_extract_value*(mo.workforce/100)
                    workforce.append(mo.actual_extract_value*(mo.workforce/100))
                    if summ[1]:
                        summ[1]=summ[1]+mo.actual_extract_value*(mo.Combined_discount_rate/100)
                    else:
                        summ[1]=mo.actual_extract_value*(mo.Combined_discount_rate/100)
                    Combined_discount_rate.append(mo.actual_extract_value*(mo.Combined_discount_rate/100))
                    if summ[2]:
                        summ[2]=summ[2]+mo.actual_extract_value*(mo.bank_ratio/100)
                    else:
                        summ[2]=mo.actual_extract_value*(mo.bank_ratio/100)
                    bank_ratio.append(mo.actual_extract_value*(mo.bank_ratio/100))
                    if summ[3]:
                        summ[3]=summ[3]+mo.actual_extract_value*(mo.engineering_stamp/100)
                    else:
                        summ[3]=mo.actual_extract_value*(mo.engineering_stamp/100)
                    engineering_stamp.append(mo.actual_extract_value*(mo.engineering_stamp/100))
                    if summ[4]:
                        summ[4]=summ[4]+mo.actual_extract_value*(mo.others/100)
                    else:
                        summ[4]=mo.actual_extract_value*(mo.others/100)
                    others.append(mo.actual_extract_value*(mo.others/100))
                    if summ[5]:
                        summ[5]=summ[5]+mo.actual_extract_value*(mo.taxes/100)
                    else:
                        summ[5]=mo.actual_extract_value*(mo.taxes/100)
                    taxes.append(mo.actual_extract_value*(mo.taxes/100))
                    if summ[6]:
                        summ[6]=summ[6]+mo.actual_extract_value*(mo.altaminat/100)
                    else:
                        summ[6]=mo.actual_extract_value*(mo.altaminat/100)
                    altaminat.append(mo.actual_extract_value*(mo.altaminat/100))
                    if summ[7]:
                        summ[7]=summ[7]+mo.actual_extract_value*(mo.discount/100)
                    else:
                        summ[7]=mo.actual_extract_value*(mo.discount/100)
                    discount.append(mo.actual_extract_value*(mo.discount/100))
                    if summ[8]:
                        summ[8]=summ[8]+mo.actual_extract_value*(mo.other_deductions_1/100)
                    else:
                        summ[8]=mo.actual_extract_value*(mo.other_deductions_1/100)
                    other_deductions_1.append(mo.actual_extract_value*(mo.other_deductions_1/100))
                    if summ[9]:
                        summ[9]=summ[9]+mo.actual_extract_value*(mo.other_deductions_2/100)
                    else:
                        summ[9]=mo.actual_extract_value*(mo.other_deductions_2/100)
                    other_deductions_2.append(mo.actual_extract_value*(mo.other_deductions_2/100))
                    if summ[10]:
                        summ[10]=summ[10]+mo.actual_extract_value*(mo.commercial_ndustrial_profits_tax/100)
                    else:
                        summ[10]=mo.actual_extract_value*(mo.commercial_ndustrial_profits_tax/100)
                    commercial_ndustrial_profits_tax.append(mo.actual_extract_value*(mo.commercial_ndustrial_profits_tax/100))
                    if summ[11]:
                        summ[11]=summ[11]+mo.actual_extract_value*(mo.value_added_tax/100)
                    else:
                        summ[11]=mo.actual_extract_value*(mo.value_added_tax/100)
                    value_added_tax.append(mo.actual_extract_value*(mo.value_added_tax/100))
                    if summ[12]:
                        summ[12]=summ[12]+mo.actual_extract_value*(mo.stamp_tax_division/100)
                    else:
                        summ[12]=mo.actual_extract_value*(mo.stamp_tax_division/100)
                    stamp_tax_division.append(mo.actual_extract_value*(mo.stamp_tax_division/100))
                    if summ[13]:
                        summ[13]=summ[13]+mo.actual_extract_value*(mo.martyrs_Honor_fund/100)
                    else:
                        summ[13]=mo.actual_extract_value*(mo.martyrs_Honor_fund/100)
                    martyrs_Honor_fund.append(mo.actual_extract_value*(mo.martyrs_Honor_fund/100))
                    if summ[14]:
                        summ[14]=summ[14]+mo.actual_extract_value*(mo.resource_development_tax/100)
                    else:
                        summ[14]=mo.actual_extract_value*(mo.resource_development_tax/100)
                    resource_development_tax.append(mo.actual_extract_value*(mo.resource_development_tax/100))
                    if summ[15]:
                        summ[15]=summ[15]+mo.actual_extract_value*(mo.long_Live_egypt_fund/100)
                    else:
                        summ[15]=mo.actual_extract_value*(mo.long_Live_egypt_fund/100)
                    long_Live_egypt_fund.append(mo.actual_extract_value*(mo.long_Live_egypt_fund/100))
                    if summ[16]:
                        summ[16]=summ[16]+mo.actual_extract_value*(mo.applied_tear/100)
                    else:
                        summ[16]=mo.actual_extract_value*(mo.applied_tear/100)
                    applied_tear.append(mo.actual_extract_value*(mo.applied_tear/100))
                    if summ[17]:
                        summ[17]=summ[17]+mo.actual_extract_value*(mo.union_of_two_sayings/100)
                    else:
                        summ[17]=mo.actual_extract_value*(mo.union_of_two_sayings/100)
                    union_of_two_sayings.append(mo.actual_extract_value*(mo.union_of_two_sayings/100))
        else:
            pro=None
    else:
        projects = Projects.objects.filter(id=pk)
        if projects:
            pro=projects.first()
            for mo in pro.mostakhlas.all():
                    if summ[0]:
                        summ[0]=summ[0]+mo.actual_extract_value*(mo.workforce/100)
                    else:
                        summ[0]=mo.actual_extract_value*(mo.workforce/100)
                    workforce.append(mo.actual_extract_value*(mo.workforce/100))
                    if summ[1]:
                        summ[1]=summ[1]+mo.actual_extract_value*(mo.Combined_discount_rate/100)
                    else:
                        summ[1]=mo.actual_extract_value*(mo.Combined_discount_rate/100)
                    Combined_discount_rate.append(mo.actual_extract_value*(mo.Combined_discount_rate/100))
                    if summ[2]:
                        summ[2]=summ[2]+mo.actual_extract_value*(mo.bank_ratio/100)
                    else:
                        summ[2]=mo.actual_extract_value*(mo.bank_ratio/100)
                    bank_ratio.append(mo.actual_extract_value*(mo.bank_ratio/100))
                    if summ[3]:
                        summ[3]=summ[3]+mo.actual_extract_value*(mo.engineering_stamp/100)
                    else:
                        summ[3]=mo.actual_extract_value*(mo.engineering_stamp/100)
                    engineering_stamp.append(mo.actual_extract_value*(mo.engineering_stamp/100))
                    if summ[4]:
                        summ[4]=summ[4]+mo.actual_extract_value*(mo.others/100)
                    else:
                        summ[4]=mo.actual_extract_value*(mo.others/100)
                    others.append(mo.actual_extract_value*(mo.others/100))
                    if summ[5]:
                        summ[5]=summ[5]+mo.actual_extract_value*(mo.taxes/100)
                    else:
                        summ[5]=mo.actual_extract_value*(mo.taxes/100)
                    taxes.append(mo.actual_extract_value*(mo.taxes/100))
                    if summ[6]:
                        summ[6]=summ[6]+mo.actual_extract_value*(mo.altaminat/100)
                    else:
                        summ[6]=mo.actual_extract_value*(mo.altaminat/100)
                    altaminat.append(mo.actual_extract_value*(mo.altaminat/100))
                    if summ[7]:
                        summ[7]=summ[7]+mo.actual_extract_value*(mo.discount/100)
                    else:
                        summ[7]=mo.actual_extract_value*(mo.discount/100)
                    discount.append(mo.actual_extract_value*(mo.discount/100))
                    if summ[8]:
                        summ[8]=summ[8]+mo.actual_extract_value*(mo.other_deductions_1/100)
                    else:
                        summ[8]=mo.actual_extract_value*(mo.other_deductions_1/100)
                    other_deductions_1.append(mo.actual_extract_value*(mo.other_deductions_1/100))
                    if summ[9]:
                        summ[9]=summ[9]+mo.actual_extract_value*(mo.other_deductions_2/100)
                    else:
                        summ[9]=mo.actual_extract_value*(mo.other_deductions_2/100)
                    other_deductions_2.append(mo.actual_extract_value*(mo.other_deductions_2/100))
                    if summ[10]:
                        summ[10]=summ[10]+mo.actual_extract_value*(mo.commercial_ndustrial_profits_tax/100)
                    else:
                        summ[10]=mo.actual_extract_value*(mo.commercial_ndustrial_profits_tax/100)
                    value_added_tax.append(mo.actual_extract_value*(mo.commercial_ndustrial_profits_tax/100))
                    if summ[11]:
                        summ[11]=summ[11]+mo.actual_extract_value*(mo.value_added_tax/100)
                    else:
                        summ[11]=mo.actual_extract_value*(mo.value_added_tax/100)
                    value_added_tax.append(mo.actual_extract_value*(mo.value_added_tax/100))
                    if summ[12]:
                        summ[12]=summ[12]+mo.actual_extract_value*(mo.stamp_tax_division/100)
                    else:
                        summ[12]=mo.actual_extract_value*(mo.stamp_tax_division/100)
                    stamp_tax_division.append(mo.actual_extract_value*(mo.stamp_tax_division/100))
                    if summ[13]:
                        summ[13]=summ[13]+mo.actual_extract_value*(mo.martyrs_Honor_fund/100)
                    else:
                        summ[13]=mo.actual_extract_value*(mo.martyrs_Honor_fund/100)
                    martyrs_Honor_fund.append(mo.actual_extract_value*(mo.martyrs_Honor_fund/100))
                    if summ[14]:
                        summ[14]=summ[14]+mo.actual_extract_value*(mo.resource_development_tax/100)
                    else:
                        summ[14]=mo.actual_extract_value*(mo.resource_development_tax/100)
                    resource_development_tax.append(mo.actual_extract_value*(mo.resource_development_tax/100))
                    if summ[15]:
                        summ[15]=summ[15]+mo.actual_extract_value*(mo.long_Live_egypt_fund/100)
                    else:
                        summ[15]=mo.actual_extract_value*(mo.long_Live_egypt_fund/100)
                    long_Live_egypt_fund.append(mo.actual_extract_value*(mo.long_Live_egypt_fund/100))
                    if summ[16]:
                        summ[16]=summ[16]+mo.actual_extract_value*(mo.applied_tear/100)
                    else:
                        summ[16]=mo.actual_extract_value*(mo.applied_tear/100)
                    applied_tear.append(mo.actual_extract_value*(mo.applied_tear/100))
                    if summ[17]:
                        summ[17]=summ[17]+mo.actual_extract_value*(mo.union_of_two_sayings/100)
                    else:
                        summ[17]=mo.actual_extract_value*(mo.union_of_two_sayings/100)
                    union_of_two_sayings.append(mo.actual_extract_value*(mo.union_of_two_sayings/100))
        else:
            pro=None
    return render(request, 'reports/almostakhlas.html', context={"pro": pro,"all_p":Projects.objects.all(),
                                                                 "union_of_two_sayings":union_of_two_sayings,
                                                                 "applied_tear":applied_tear,
                                                                 "long_Live_egypt_fund":long_Live_egypt_fund,
                                                                 "resource_development_tax":resource_development_tax,
                                                                 "martyrs_Honor_fund":martyrs_Honor_fund,
                                                                 "stamp_tax_division":stamp_tax_division,
                                                                 "value_added_tax":value_added_tax,
                                                                 "commercial_ndustrial_profits_tax":commercial_ndustrial_profits_tax,
                                                                 "other_deductions_2":other_deductions_2,
                                                                 "other_deductions_1":other_deductions_1,
                                                                 "discount":discount,
                                                                 "altaminat":altaminat,
                                                                 "taxes":taxes,
                                                                 "others":others,
                                                                 "engineering_stamp":engineering_stamp,
                                                                 "bank_ratio":bank_ratio,
                                                                 "Combined_discount_rate":Combined_discount_rate,
                                                                 "workforce":workforce,
                                                                 "summ":summ})
