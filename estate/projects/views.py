import json
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Projects, Ahdaa, Masourfat
from decimal import Decimal
from django.contrib import messages


class DataObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def add_project(request):
    try:
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
                date_end=datetime.strptime(data_object.date7[0], "%d-%m-%Y").date() if data_object.date7[0] else None,
                date_extra_end=datetime.strptime(data_object.date8[0], "%d-%m-%Y").date() if data_object.date8[
                    0] else None,
                price_project=data_object.demo2[0] if data_object.demo2[0] else 0.0,
                gramat_altakheer=data_object.demo1[0] if data_object.demo1[0] else 0.0,
                total_price_end=data_object.demo2[1] if data_object.demo2[1] else 0.0,
                name_mostakhlas=data_object.name_mo[0] if data_object.name_mo[0] else None,
                date_mostakhlas=datetime.strptime(data_object.date_mo[0], "%d-%m-%Y").date() if data_object.date_mo[
                    0] else None,
                price_mostakhlas=data_object.demo2[2] if data_object.demo2[2] else 0.0,
                price_mostakhlas_after=data_object.demo2[3] if data_object.demo2[3] else 0.0,
                altamin=data_object.demo2[4] if data_object.demo2[4] else 0.0,
            )
            index = 0
            while True:
                name = getattr(data_object, 'group-a[' + str(index) + '][untyped-input]', None)
                if name[0]:
                    price = getattr(data_object, 'group-a[' + str(index) + '][demo2]', None)
                    ahdaa = Ahdaa.objects.create(name=name[0], price=price[0] if price[0] else None)
                    project.ahdaa.add(ahdaa)
                    project.save()
                else:
                    break
                index = index + 1
            index = 0
            while True:

                date_mosroufat = getattr(data_object, 'group-a[' + str(index) + '][date10]', None)
                if date_mosroufat[0]:
                    price = getattr(data_object, 'group-a[' + str(index) + '][demo2]', None)
                    des = getattr(data_object, 'group-a[' + str(index) + '][des]', None)
                    moard = getattr(data_object, 'group-a[' + str(index) + '][moard]', None)
                    masourfat = Masourfat.objects.create(price=price[1] if price[1] else None,
                                                         date_masrouf=datetime.strptime(date_mosroufat[0],
                                                                                        "%d-%m-%Y").date() if
                                                         date_mosroufat[0] else None,
                                                         almardeen=moard[0], descriptions=des[0])
                    project.masourfats.add(masourfat)
                    project.save()
                else:
                    break
                index = index + 1
            messages.success(request, "تم حفط المشروع")
            return redirect('/projects/')
    except Exception as e:
        messages.error(request, str(e))
    return render(request, 'projects/add_project.html')


def edit_project(request, id):
    try:
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
                project.date_end = datetime.strptime(data_object.date7[0], "%d-%m-%Y").date() if data_object.date7[
                    0] else None
                project.date_extra_end = datetime.strptime(data_object.date8[0], "%d-%m-%Y").date() if \
                    data_object.date8[
                        0] else None
                project.price_project = data_object.demo2[0] if data_object.demo2[0] else 0.0
                project.gramat_altakheer = data_object.demo1[0] if data_object.demo1[0] else 0.0
                project.total_price_end = data_object.demo2[1] if data_object.demo2[1] else 0.0
                project.name_mostakhlas = data_object.name_mo[0] if data_object.name_mo[0] else None
                project.date_mostakhlas = datetime.strptime(data_object.date_mo[0], "%d-%m-%Y").date() if \
                    data_object.date_mo[0] else None
                project.price_mostakhlas = data_object.demo2[2] if data_object.demo2[2] else 0.0
                project.price_mostakhlas_after = data_object.demo2[3] if data_object.demo2[3] else 0.0
                project.altamin = data_object.demo2[4] if data_object.demo2[4] else 0.0
                project.save()
                project.ahdaa.all().delete()
                project.masourfats.all().delete()

                index = 0
                while True:
                    name = getattr(data_object, 'group-a[' + str(index) + '][untyped-input]', None)
                    if name[0]:
                        price = getattr(data_object, 'group-a[' + str(index) + '][demo2]', None)
                        ahdaa = Ahdaa.objects.create(name=name[0], price=price[0] if price[0] else None)
                        project.ahdaa.add(ahdaa)
                    else:
                        break
                    index += 1

                index = 0
                while True:
                    date_mosroufat = getattr(data_object, 'group-a[' + str(index) + '][date10]', None)
                    if date_mosroufat[0]:
                        price = getattr(data_object, 'group-a[' + str(index) + '][demo2]', None)
                        des = getattr(data_object, 'group-a[' + str(index) + '][des]', None)
                        moard = getattr(data_object, 'group-a[' + str(index) + '][moard]', None)
                        masourfat = Masourfat.objects.create(
                            price=price[1] if price[1] else None,
                            date_masrouf=datetime.strptime(date_mosroufat[0], "%d-%m-%Y").date() if date_mosroufat[
                                0] else None,
                            almardeen=moard[0],
                            descriptions=des[0]
                        )
                        project.masourfats.add(masourfat)
                    else:
                        break
                    index += 1
                project.save()
                messages.success(request, "تم تعديل المشروع")
                return redirect('/projects/')

        else:
            if project:
                return render(request, 'projects/add_project.html', context={'project': project})
    except Exception as e:
        messages.error(request, str(e))
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
        messages.success(request,"تم مسح المشروع")
    return redirect('/projects/')
