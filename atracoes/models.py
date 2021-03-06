from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    fotos = models.ImageField(upload_to='atracoes', null=True, blank=True)


    def __str__(self):
        return self.nome