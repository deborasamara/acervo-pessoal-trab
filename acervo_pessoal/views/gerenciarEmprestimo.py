from django.shortcuts import render, redirect
# Create your views here.
from django.views import View
from ..models.livro import *
from ..models.contato import *
from ..models.emprestimo import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

class RegistrarEmprestimoView(View):
    def get(self, request, *args, **kwargs):
        emprestimos = Emprestimo.objects.filter(usuario=request.user).order_by('-id')
        #livros = Livro.objects.filter(usuario=request.user)
        contatos = Contato.objects.filter(usuario=request.user)
        # mostrar livros disponiveis para empréstimo:
        ## pegar todos os ids dos livros que tem emprestimos ativos e retirar dos livros disponiveis
        livros_emprestados_identificadores = Emprestimo.objects.filter(usuario=request.user, status_emprestimo='ativo').values_list('livro_id', flat=True)
        ## fazer uma lista de livros disponiveis retirando os emprestados 
        livros_disponiveis = Livro.objects.filter(usuario=request.user).exclude(id__in=livros_emprestados_identificadores)

        return render(request, 'registrar_emprestimo.html', {'emprestimos': emprestimos, 'livros':livros_disponiveis, 'contatos':contatos})
    
    def post(self, request, *args, **kwargs):
        livro_id = request.POST.get('livro') #pega o id do livro
        contato_id = request.POST.get('contato') 

        #procura por id para poder enviar para a criação do emprestimo
        livro = get_object_or_404(Livro, id=livro_id)
        contato = get_object_or_404(Contato, id=contato_id)

        emprestimo = Emprestimo(
                livro= livro,
                contato= contato,
                data_devolucao= None,
                usuario=request.user,
                status_emprestimo='ativo'
        )
        emprestimo.save()
        return redirect(request.META.get('HTTP_REFERER'), )
    

class RegistrarDevolucaoView(View):
    def get(self, request, *args, **kwargs):
        emprestimos_ativos = Emprestimo.objects.filter(usuario=request.user, status_emprestimo='ativo').order_by('-data_emprestimo')
        livros_emprestados = Livro.objects.filter(emprestimo__usuario=request.user, emprestimo__status_emprestimo='ativo').distinct()
        return render(request, 'registrar_devolucao.html', {'emprestimos_ativos': emprestimos_ativos, 'livros_emprestados': livros_emprestados})

    def post(self, request, *args, **kwargs):
        livro_id = request.POST.get('livro')
        livro = get_object_or_404(Livro, id=livro_id, usuario=request.user) # acha o livro pelo id
        emprestimo = Emprestimo.objects.filter(livro=livro, usuario=request.user, status_emprestimo='ativo').first() # procura o empréstimo desse livro escolhido
        if (emprestimo): # se o emprestimo existir
             emprestimo.status_emprestimo = 'devolvido' # muda o status do emprestimo para devolvido
             emprestimo.data_devolucao = timezone.now() # envia valor de devolvido para o emprestimo
             emprestimo.save() # salva o emprestimo
        
        return redirect(request.META.get('HTTP_REFERER'))
    
class ListarItensView(View):
    def get(self, request, *args, **kwargs):
        ## pegar todos os ids dos livros que tem emprestimos ativos e retirar dos livros disponiveis
        livros_emprestados_identificadores = Emprestimo.objects.filter(usuario=request.user, status_emprestimo='ativo').values_list('livro_id', flat=True)
        ## fazer uma lista de livros disponiveis retirando os emprestados 
        livros_disponiveis = Livro.objects.filter(usuario=request.user).exclude(id__in=livros_emprestados_identificadores) # DISPONIVEIS

        ## pegar todos os ids dos livros que tem emprestimos e adicionar em livros emprestados
        livros_emprestados = Livro.objects.filter(id__in=livros_emprestados_identificadores)# EMPRESTADOS

        return render(request, 'listar_itens.html', {'livros_disponiveis': livros_disponiveis, 'livros_emprestados': livros_emprestados})


