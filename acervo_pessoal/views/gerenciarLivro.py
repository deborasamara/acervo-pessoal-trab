from django.shortcuts import render, redirect
# Create your views here.
from django.views import View
from ..models.livro import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

class CadastrarLivroView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.filter(usuario=request.user).order_by('-id')
        return render(request, 'cadastrar_livro.html', {'livros': livros})
    
    def post(self, request, *args, **kwargs):
         nome = request.POST.get('nome_livro')
         autor = request.POST.get('autor')
         ano = request.POST.get('ano')
         foto = request.FILES.get('foto_livro')

         livro = Livro(nome=nome, autor=autor, ano=ano, foto=foto, usuario=request.user)
         livro.save()
         return redirect(request.META.get('HTTP_REFERER'))
    
class PesquisarLivroView(View):
     def get(self, request, *args, **kwargs):
          pesquisa = request.GET.get('p', '') # se o usuário não digitar a variável 'p', ele vai só dar enter sem nada, por isso precisa de dois argumentos
          livros_do_acervo = Livro.objects.filter(usuario=request.user, nome__icontains=pesquisa)
          return render(request, 'livros_pesquisados.html', {'livros': livros_do_acervo})
