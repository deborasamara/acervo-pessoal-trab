from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from ..models.contato import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

class CadastrarContatoView(View):
     def get(self, request, *args, **kwargs):
        contatos = Contato.objects.filter(usuario=request.user).order_by('-id')
        return render(request, 'cadastrar_contato.html', {'contatos': contatos})
    
     def post(self, request, *args, **kwargs):
         nome = request.POST.get('nome')
         email = request.POST.get('email')

         contato = Contato(nome=nome, email=email, usuario=request.user)
         contato.save()
         return redirect(request.META.get('HTTP_REFERER'))