from django.shortcuts import render,redirect
from .models import Community
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def index(request):
    community= Community.objects.first()
    return render(request, 'users/index.html',{'community':community})

def register(request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            phone=(request.POST['whatsapp'])
            print(phone)
            return redirect('userdash')
              
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form': form})

def userdash(request):
    return HttpResponse("registered")

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                
                if user.role == 'member':
                    return HttpResponse("HI member")
                elif user.role == 'merchant':
                    return HttpResponse("HI merchant")
                else:
                    return HttpResponse("HI admin")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = CustomLoginForm()

    return render(request, 'users/login.html', {'form': form})

def custom_logout(request):
    if request.user.is_authenticated:
        request.session.flush()  

    logout(request)  
    return redirect('login')