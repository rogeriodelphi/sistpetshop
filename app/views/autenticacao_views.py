from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_usuario(request):
    if request.method == "POST":
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('listar_clientes')
            else:
                messages.error(request, 'As credenciais do usuário estão incorretas!')
    else:
        form_login = AuthenticationForm()
    return render(request, 'autenticacao/login.html', {'form_login': form_login})