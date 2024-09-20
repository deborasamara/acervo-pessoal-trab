from django.contrib import admin
from .models.contato import *
from .models.emprestimo import *
from .models.livro import *

# Register your models here.
admin.site.register(Emprestimo)
admin.site.register(Contato)
admin.site.register(Livro)