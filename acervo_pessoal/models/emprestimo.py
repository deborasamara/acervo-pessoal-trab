from django.db import models 
from acervo_pessoal.models.livro import Livro
from acervo_pessoal.models.contato import Contato
from django.contrib.auth.models import User
from django.utils import timezone

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status_emprestimo = models.CharField(max_length=10, choices= [ ('ativo', 'Ativo'),
        ('devolvido', 'Devolvido')], default='ativo')
    
    def __str__(self):
        return "Livro "+ str(self.livro) + " emprestado para "+ str(self.contato) + " em " + str(self.data_emprestimo) + " status: "+ str(self.status_emprestimo)
    
""" def registrar_devolucao(self):
        self.status_emprestimo = 'devolvido'
        self.data_devolucao = timezone.now()
        self.save() # salva mesmo no banco de dados
"""