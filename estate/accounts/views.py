from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/mtm-group/projects/')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/mtm-group/projects/')
            else:
                messages.error(request, 'Invalid login credentials')
    else:
        form = LoginForm()
    
    return render(request, 'account/login.html', context={"form": form})
