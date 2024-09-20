from django.urls import path
from .views.gerenciarEmprestimo import *
from .views.gerenciarContato import *
from .views.gerenciarLivro import *
from .views.home import *
from .views.outros import *
from django.contrib.auth.views import *

app_name = 'acervo_pessoal'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home_logado/', HomePageLogadoView.as_view(), name='home_logado'), 
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(), name='login'),
    path('meu_perfil/', MeuPerfilView.as_view(), name='perfil'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastrar_livro/', CadastrarLivroView.as_view(), name='cadastrar_livro'),
    path('cadastrar_contato/', CadastrarContatoView.as_view(), name='cadastrar_contato'),
    path('registrar_emprestimo/', RegistrarEmprestimoView.as_view(), name='registrar_emprestimo'),
    path('registrar_devolucao/', RegistrarDevolucaoView.as_view(), name='registrar_devolucao'),
    path('listar_itens/', ListarItensView.as_view(), name='listar_itens'),
    path('pesquisar_livros/', PesquisarLivroView.as_view(), name='pesquisar_livros'),
]