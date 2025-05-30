from django.shortcuts import render,redirect
from .models import Community
from .forms import RegisterForm
from django.http import HttpResponse

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
    return HttpResponse("HI")
