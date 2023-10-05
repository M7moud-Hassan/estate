from django.shortcuts import render,redirect

from imported.forms import ImportedForm
from imported.models import Imported, PhoneNumber

# Create your views here.

def imported(request):
    clients=Imported.objects.all()
    return render(request,'imported/index.html',context={'clients':clients})

def add_imported(request):
    if request.method == 'POST':
        print(request.POST)
        form = ImportedForm(request.POST)
        if form.is_valid():
            instance = form.save()
            index=0
            while True:
                try:
                    phone=request.POST.getlist(f'group-d[{index}][phone]')[0]
                    if phone:
                        phone = PhoneNumber.objects.create(phone_number=phone)
                        instance.phonesNumber.add(phone)
                    else:
                        break
                    index=index+1
                except:
                    break
            instance.save()
        return redirect('/mtm-group/imported/')
            
    else:
        form = ImportedForm()
    return render(request, 'imported/add.html', context={'form': form})

def edit_imported(request,id):
    client=Imported.objects.filter(id=id).first()
    if client:
        if request.method=='POST':
            form = ImportedForm(request.POST)
            if form.is_valid():
                # instance = form.save()
                client.company_name=form.cleaned_data.get('company_name')
                client.address=form.cleaned_data.get('address')
                client.email=form.cleaned_data.get('email')
                client.website=form.cleaned_data.get('website')
                client.phonesNumber.clear()
                phones = request.POST.getlist('phone') 
                for phone_number in phones:
                    phone = PhoneNumber.objects.create(phone_number=phone_number)
                    client.phonesNumber.add(phone)
                client.save()
                return redirect('/mtm-group/imported/')
        else:
            form=ImportedForm(instance=client)
            return  render(request, 'imported/add.html', context={'form': form,'phones':client.phonesNumber.all()})
def delete_clients(request,id):
    client=Imported.objects.filter(id=id).first()
    if client:
        client.delete()
    return redirect('/mtm-group/imported/')