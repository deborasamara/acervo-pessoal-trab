from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from ..models.emprestimo import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout


class CadastroView(View):
     def get(self, request, *args, **kwargs):
        return render(request, 'cadastro.html')
    
     def post(self, request, *args, **kwargs):
         nome = request.POST.get('fname')
         username = request.POST.get('fusername')
         email = request.POST.get('email')
         senha = request.POST.get('password')
        
        # criar novo usuário:
         user = User.objects.create_user(
            username=username,
            email = email,
            first_name = nome,
            password = senha,
         )
         user.save()
         return redirect('acervo_pessoal:login')
         

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        # verificação dos dados para validar o login
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ver se o usuário existe no bd
        user = authenticate(request, username=username, password=password)

        #se o user receber 'none', n tem usuário, se receber outra coisa, as credenciais são inválidas

        if(user != None):
            login(request, user) 
            return redirect('acervo_pessoal:home_logado')  
        
        else:
            return render(request, 'login.html', {'error': 'Houve um erro no seu login, tente novamente. Talvez sua senha esteja errada'})

class MeuPerfilView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, 'meu_perfil.html', {'user':user})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('acervo_pessoal:home')