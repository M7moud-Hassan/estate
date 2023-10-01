import json
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect

from engineers.models import Engineers
from .models import AdditionalPeriods, Projects, Ahdaa, Masourfat, Mostakhlas
from decimal import Decimal
from django.contrib import messages
from imported.models import Imported


class DataObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def add_project(request):
        if request.method == 'POST':
            data_object = DataObject(**request.POST)
            project = Projects.objects.create(
                name=data_object.name_project[0],
                date_session=datetime.strptime(data_object.date1[0], "%d-%m-%Y").date() if data_object.date1[
                    0] else None,
                date_finance=datetime.strptime(data_object.date2[0], "%d-%m-%Y").date() if data_object.date2[
                    0] else None,
                date_notification_Altrsih=datetime.strptime(data_object.date3[0], "%d-%m-%Y").date() if
                data_object.date3[
                    0] else None,
                date_sadad_khatab_alkhsmat=datetime.strptime(data_object.date4[0], "%d-%m-%Y").date() if
                data_object.date4[
                    0] else None,
                date_asnad=datetime.strptime(data_object.date5[0], "%d-%m-%Y").date() if data_object.date5[0] else None,
                date_work=datetime.strptime(data_object.date6[0], "%d-%m-%Y").date() if data_object.date6[0] else None,
                date_end=datetime.strptime(data_object.date7[1], "%d-%m-%Y").date() if data_object.date7[0] else None,
                # date_extra_end=data_object.date8[0],
                duration_project=int(data_object.date7[0]) if data_object.date7[0] else 0,
                price_project=data_object.demo2[1] if data_object.demo2[1] else 0.0,
                insurance_value=data_object.demo2[0] if data_object.demo2[0] else 0.0,
                gramat_altakheer=data_object.demo1[0] if data_object.demo1[0] else 0.0,
                total_price_end=data_object.demo2[2] if data_object.demo2[2] else 0.0,
                report=data_object.report[0]
                )
            index = 0
            while True:

                price = getattr(data_object, 'group-a[' + str(index) + '][demo2]', None)

                if price and  int(price[0])>0:
                    eng = getattr(data_object, 'group-a[' + str(index) + '][engineer]', None)
                    # eng = getattr(data_object,  'group-a[' + str(index) + '][engineer]', None)

                    ahdaa = Ahdaa.objects.create(price=price[0] if price[0] else 0,
                                                 engineer_id=Engineers.objects.filter(id=int(eng[0])).first() if eng[0] else None)

                    project.ahdaa.add(ahdaa)
                    project.save()
                else:
                    break
                index = index + 1
                #durations
            index = 0
            while True:
                price = getattr(data_object, 'group-d[' + str(index) + '][demo2]', None)
                if  price and price[0] and  int(price[0])>0 :
                    date_Period=getattr(data_object, 'group-d[' + str(index) + '][dated1]', None)
                    reason=getattr(data_object, 'group-d[' + str(index) + '][reason]', None)
                    terminationBeforeTheIncrease=getattr(data_object, 'group-d[' + str(index) + '][dated2]', None)
                    terminationAfterTheIncrease=getattr(data_object, 'group-d[' + str(index) + '][dated3]', None)
                    durations = AdditionalPeriods.objects.create(price_increase=price[0] if price[0] else 0,
                                                 date_Period=datetime.strptime(date_Period[0],
                                                                                        "%d-%m-%Y").date() if
                                                         date_Period[0] else None,
                                                         reason=reason[0] if
                                                         reason[0] else None,
                                                         terminationBeforeTheIncrease=datetime.strptime(terminationBeforeTheIncrease[0],
                                                                                        "%d-%m-%Y").date() if
                                                         terminationBeforeTheIncrease[0] else None,
                                                         terminationAfterTheIncrease=datetime.strptime(terminationAfterTheIncrease[0],
                                                                                        "%d-%m-%Y").date() if
                                                         terminationAfterTheIncrease[0] else None,
                                                         )

                    project.durations.add(durations)
                    project.save()
                else:
                    break
                index = index + 1
                ###################################################333
            index = 0
            while True:

                date_mosroufat = getattr(data_object, 'group-a[' + str(index) + '][date10]', None)
                if date_mosroufat and date_mosroufat[0]:
                    eng = getattr(data_object, 'group-a[' + str(index) + '][engineer_]', None)
                    price = getattr(data_object, 'group-a[' + str(index) + '][demo2]', None)
                    des = getattr(data_object, 'group-a[' + str(index) + '][des]', None)
                    moard = getattr(data_object, 'group-a[' + str(index) + '][imported_]', None)
                    masourfat = Masourfat.objects.create(price=price[1] if price[1] else None,
                                                         date_masrouf=datetime.strptime(date_mosroufat[0],
                                                                                        "%d-%m-%Y").date() if
                                                         date_mosroufat[0] else None,
                                                         imported=Imported.objects.filter(id=int(moard[0])).first(), descriptions=des[0],
                                                         bain_masrouf=Engineers.objects.filter(id=int(eng[0])).first() if eng[0] else None)
                    project.masourfats.add(masourfat)
                    project.save()
                else:
                    break
                index = index + 1

            index=0
            while True:
                price_mostakhlas_after = getattr(data_object, 'group-c[' + str(index) + '][demo2]', None)
                if price_mostakhlas_after and price_mostakhlas_after[0]:
                    engineer_id = getattr(data_object, 'group-c[' + str(index) + '][engineer]', None)
                    date_mostakhlas=getattr(data_object, 'group-c[' + str(index) + '][date_mo]', None)
                    percentage=getattr(data_object, 'group-c[' + str(index) + '][demo1]', None)
                    price_mostakhlas_after=getattr(data_object, 'group-c[' + str(index) + '][demo2]', None)
                    mostakjlas=Mostakhlas.objects.create(engineer_id=Engineers.objects.filter(id=int(engineer_id[0])).first(),date_mostakhlas=
                    datetime.strptime(date_mostakhlas[0],
                                      "%d-%m-%Y").date() if
                    date_mostakhlas[0] else None
                    ,
                                                 workforce=percentage[1]  if percentage[1] else 0.0,Combined_discount_rate=percentage[2]  if percentage[2] else 0.0,
                                                 bank_ratio=percentage[3]  if percentage[3] else 0.0,engineering_stamp=percentage[4]  if percentage[4] else 0.0,
                                                 others=percentage[5]  if percentage[5] else 0.0,taxes=percentage[6]  if percentage[6] else 0.0,altaminat=percentage[0]  if percentage[0] else 0.0,
                                                 price_mostakhlas_after=price_mostakhlas_after[1] if price_mostakhlas_after[1] else 0.0,
                                                actual_extract_value=price_mostakhlas_after[0] if price_mostakhlas_after[0] else 0.0,
                                                         discount=price_mostakhlas_after[2] if price_mostakhlas_after[2] else 0.0,
                                                         other_deductions_1=percentage[7]  if percentage[7] else 0.0,
                                                         other_deductions_2=percentage[8]  if percentage[8] else 0.0,
                                                         commercial_ndustrial_profits_tax=percentage[9]  if percentage[9] else 0.0,
                                                         value_added_tax=percentage[10]  if percentage[10] else 0.0,
                                                         stamp_tax_division=percentage[11]  if percentage[11] else 0.0,
                                                         martyrs_Honor_fund=percentage[12]  if percentage[12] else 0.0,
                                                         resource_development_tax=percentage[13]  if percentage[13] else 0.0,
                                                         long_Live_egypt_fund=percentage[14]  if percentage[14] else 0.0,
                                                         applied_tear=percentage[15]  if percentage[15] else 0.0,
                                                         union_of_two_sayings=percentage[16]  if percentage[16] else 0.0,
                                                         notes=getattr(data_object, 'group-c[' + str(index) + '][notes][0]', None)
                                                         )
                    project.mostakhlas.add(mostakjlas)
                    project.save()
                else:
                    break
                index = index + 1
            messages.success(request, "تم حفط المشروع")
            return redirect('/projects/')
    # except Exception as e:
    #     messages.error(request, str(e))
        return render(request, 'projects/add_project.html',context={'engineers':Engineers.objects.all(),
                                                                    'importeds':Imported.objects.all()})


def edit_project(request, id):
        project = Projects.objects.filter(id=id).first()

        if request.method == 'POST':
            data_object = DataObject(**request.POST)
            if project:
                project.name = data_object.name_project[0]
                project.date_session = datetime.strptime(data_object.date1[0], "%d-%m-%Y").date() if data_object.date1[
                    0] else None
                project.date_finance = datetime.strptime(data_object.date2[0], "%d-%m-%Y").date() if data_object.date2[
                    0] else None
                project.date_notification_Altrsih = datetime.strptime(data_object.date3[0], "%d-%m-%Y").date() if \
                    data_object.date3[0] else None
                project.date_sadad_khatab_alkhsmat = datetime.strptime(data_object.date4[0], "%d-%m-%Y").date() if \
                    data_object.date4[0] else None
                project.date_asnad = datetime.strptime(data_object.date5[0], "%d-%m-%Y").date() if data_object.date5[
                    0] else None
                project.date_work = datetime.strptime(data_object.date6[0], "%d-%m-%Y").date() if data_object.date6[
                    0] else None
                project.date_end = datetime.strptime(data_object.date7[1], "%d-%m-%Y").date() if data_object.date7[
                    0] else None
                project.date_extra_end = project.date_extra_end + int(data_object.date8[0]) if \
                    data_object.date8[
                        0] else None
                project.report=data_object.report[0]
                project.price_project = data_object.demo2[0] if data_object.demo2[0] else 0.0
                project.gramat_altakheer = data_object.demo1[0] if data_object.demo1[0] else 0.0
                project.total_price_end = data_object.demo2[1] if data_object.demo2[1] else 0.0
                project.save()
                project.ahdaa.all().delete()
                project.masourfats.all().delete()
                project.mostakhlas.all().delete()
                project.durations.all().delete()

                index = 0
                while True:
                    eng = getattr(data_object, 'group-a[' + str(index) + '][engineer]', None)
                    if eng and eng[0]:
                        price = getattr(data_object, 'group-a[' + str(index) + '][demo2]', None)
                        # eng = getattr(data_object,  'group-a[' + str(index) + '][engineer]', None)

                        ahdaa = Ahdaa.objects.create(price=price[0] if price[0] else 0,
                                                     engineer_id=Engineers.objects.filter(id=int(eng[0])).first() if
                                                     eng[0] else None)
                        project.ahdaa.add(ahdaa)
                    else:
                        break
                    index += 1

                index = 0
                while True:
                    date_mosroufat = getattr(data_object, 'group-a[' + str(index) + '][date10]', None)
                    if date_mosroufat and date_mosroufat[0]:
                        price = getattr(data_object, 'group-a[' + str(index) + '][demo2]', None)
                        eng = getattr(data_object, 'group-a[' + str(index) + '][engineer_]', None),
                        des = getattr(data_object, 'group-a[' + str(index) + '][des]', None)
                        moard = getattr(data_object, 'group-a[' + str(index) + '][moard]', None)
                        
                        masourfat = Masourfat.objects.create(
                            price=price[1] if price[1] else None,
                            date_masrouf=datetime.strptime(date_mosroufat[0], "%d-%m-%Y").date() if date_mosroufat[
                                0] else None,
                            almardeen=moard[0],
                            descriptions=des[0],

                            bain_masrouf=Engineers.objects.filter(id=int(eng[0][0])).first() if eng[0] else None
                        )
                        project.masourfats.add(masourfat)
                    else:
                        break
                    index += 1
                project.save()

                index = 0
                while True:
                    price_mostakhlas_after = getattr(data_object, 'group-c[' + str(index) + '][demo2]', None)
                    if price_mostakhlas_after and price_mostakhlas_after[0]:
                        engineer_id = getattr(data_object, 'group-c[' + str(index) + '][engineer]', None)
                        date_mostakhlas = getattr(data_object, 'group-c[' + str(index) + '][date_mo]', None)
                        percentage = getattr(data_object, 'group-c[' + str(index) + '][demo1]', None)
                        price_mostakhlas_after = getattr(data_object, 'group-c[' + str(index) + '][demo2]', None)
                        mostakjlas = Mostakhlas.objects.create(
                            engineer_id=Engineers.objects.filter(id=int(engineer_id[0])).first(), date_mostakhlas=
                            datetime.strptime(date_mostakhlas[0],
                                              "%d-%m-%Y").date() if
                        date_mostakhlas[0] else None
                                                               ,
                                                                  workforce=percentage[1]  if percentage[1] else 0.0,Combined_discount_rate=percentage[2]  if percentage[2] else 0.0,
                                                 bank_ratio=percentage[3]  if percentage[3] else 0.0,engineering_stamp=percentage[4]  if percentage[4] else 0.0,
                                                 others=percentage[5]  if percentage[5] else 0.0,taxes=percentage[6]  if percentage[6] else 0.0,altaminat=percentage[0]  if percentage[0] else 0.0,
                                                 price_mostakhlas_after=price_mostakhlas_after[1] if price_mostakhlas_after[1] else 0.0,
                                                actual_extract_value=price_mostakhlas_after[0] if price_mostakhlas_after[0] else 0.0,
                                                         discount=price_mostakhlas_after[2] if price_mostakhlas_after[2] else 0.0,
                                                         other_deductions_1=percentage[7]  if percentage[7] else 0.0,
                                                         other_deductions_2=percentage[8]  if percentage[8] else 0.0,
                                                         commercial_ndustrial_profits_tax=percentage[9]  if percentage[9] else 0.0,
                                                         value_added_tax=percentage[10]  if percentage[10] else 0.0,
                                                         stamp_tax_division=percentage[11]  if percentage[11] else 0.0,
                                                         martyrs_Honor_fund=percentage[12]  if percentage[12] else 0.0,
                                                         resource_development_tax=percentage[13]  if percentage[13] else 0.0,
                                                         long_Live_egypt_fund=percentage[14]  if percentage[14] else 0.0,
                                                         applied_tear=percentage[15]  if percentage[15] else 0.0,
                                                         union_of_two_sayings=percentage[16]  if percentage[16] else 0.0,
                                                         notes=getattr(data_object, 'group-c[' + str(index) + '][notes][0]', None)
                                                         )
                        project.mostakhlas.add(mostakjlas)
                        project.save()
                    else:
                        break
                    index = index + 1
                messages.success(request, "تم تعديل المشروع")
                return redirect('/projects/')

        else:
            if project:
                return render(request, 'projects/add_project.html', context={'project': project,'engineers':Engineers.objects.all(),
                                                                             'importeds':Imported.objects.all()})
    # except Exception as e:
    #     messages.error(request, str(e))
        return redirect('/projects/')


def update_ahdaa(request):
    try:
        data = json.loads(request.body)
        for d in data:
            if d['name'] or d['price']:
                ah = Ahdaa.objects.filter(id=int(d['id'])).first()
                if ah:
                    ah.name = d['name']
                    ah.price = d['price']
                ah.save()
        return JsonResponse({'status': 'success', 'message': 'Data updated successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def update_masrouf(request):
    try:
        data = json.loads(request.body)
        print(data)
        for d in data:
            if d['date_masrouf'] or d['price'] or d['almardeen'] or d['descriptions']:
                ah = Masourfat.objects.filter(id=int(d['id'])).first()
                if ah:
                    if d['date_masrouf']:
                        date_masrouf_date = datetime.strptime(d['date_masrouf'], "%d-%m-%Y").date()
                    else:
                        date_masrouf_date = None
                    ah.date_masrouf = date_masrouf_date
                    ah.price = Decimal(d['price'])
                    ah.almardeen = d['almardeen']
                    ah.descriptions = ['descriptions']
                ah.save()
        return JsonResponse({'status': 'success', 'message': 'Data updated successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def delete_project(request, id):
    project = Projects.objects.filter(id=id).first()
    if project:
        project.delete()
        messages.success(request, "تم مسح المشروع")
    return redirect('/projects/')


def form(request):
   return  render(request,'components/forms/form-advanced.html')