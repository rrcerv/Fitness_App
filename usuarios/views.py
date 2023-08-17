from django.shortcuts import render
from .models import Usuario
import re
from django.shortcuts import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from django.shortcuts import HttpResponse
import matplotlib.pyplot as plt
from pathlib import Path
import os


def signup(request):
    status = request.GET.get('status')
    if request.session.get('usuario'):
        return redirect('/home/fitness_app/')
    else:
        return render(request, 'signup.html', {'status': status} )
    
def validate_signup(request):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()
        nome = request.POST.get('nome').strip()

        if (re.fullmatch(regex, email) == None):
            return redirect('/auth/cadastrar/?status=0')
        
        if (len(senha)< 8):
            return redirect ('/auth/cadastrar/?status=1')
        
        if (Usuario.objects.filter(email=email)):
            return redirect ('/auth/cadastrar/?status=2') 
        
        else:
            senha = generate_password_hash(senha, 'pbkdf2:sha256', 8)
            new_user = Usuario(email=email, senha=senha, nome=nome)
            new_user.save()
            return redirect('/auth/login/')

def login(request):
    status=request.GET.get('status')
    if request.session.get('usuario'):
        return redirect('/home/fitness_app/')
    else:
        return render(request, 'login.html', {'status': status})

def validate_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(Usuario.objects.filter(email=email)) > 0:
            current_user = Usuario.objects.get(email=email)
            if check_password_hash(current_user.senha, senha):
                request.session['usuario'] = current_user.id
                return redirect('/home/fitness_app/')
            else:
                return redirect('/auth/login/?status=0')
            
            #if check_password_hash()
        else:
            return redirect('/auth/login/?status=1')

def sair(request):
    request.session.flush()
    return redirect('/auth/login')