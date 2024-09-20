from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class HomeView(View):
      def get(self, request, *args, **kwargs):
        return redirect('acervo_pessoal:home_logado') if request.user.is_authenticated else render(request, 'home.html')

class HomePageLogadoView(View):
      def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, 'pag_inicial_logado.html', {'user': user})





