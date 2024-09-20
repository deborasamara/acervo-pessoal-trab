from .models import *

def registrar_livro(nome, autor, ano, foto):
    livro = Livro(
        nome = nome,
        autor = autor, 
        ano = ano,
        foto = foto, 
    )
    livro.save()