import email
from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Marmita

def register_marmita(request):
    return render(request, 'register_marmita.html')

@login_required(login_url='/login/')
def set_marmita(request):
    sabor =request.POST.get('sabor')
    email =request.POST.get('email')
    phone =request.POST.get('phone')
    descricao =request.POST.get('descricao')
    file =request.FILE.get('file')
    user =request.user
    marmita = Marmita.objects.create(sabor=sabor, descricao=descricao)
    return redirect('/')    

@login_required(login_url='/login')
def list_all_marmitas(request):
    marmita = Marmita.objects.filter(active=True)
    return render(request, 'list.html', {'marmita':marmita})  

def list_user_marmitas(request):
    marmita = Marmita.objects.filter(active=True, user=request.user)
    return render(request, 'list.html',{'marmita':marmita})  

def marmita_detail(request, id):
    marmita = Marmita.objects.get(active=True, id=id)
    print(marmita.id)
    return render(request, 'marmita.html',{'marmita':marmita})        

def logout_user(request):
    print(request.user)
    logout(request)  
    return redirect('/login/')  

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário/Senha inválido. Tente novamente.')
        return redirect('/login/')    


   