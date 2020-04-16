from django.db import models


class Tecnologia(models.Model):
    nome = models.CharField('Nome', max_length=20, null=False, blank=False)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    CONTRATACAO_CHOICES = [
        ('CLT', 'Empregado registrado pela CLT'),
        ('TJ', 'Pessoa Jurídica'),
    ]

    titulo = models.CharField('Titulo', max_length=50, blank=False, null=False)
    descricao = models.TextField('Descrição', blank=False, null=False)
    salario = models.FloatField('Salario', blank=False, null=False)
    local = models.CharField('Local', max_length=20, blank=False, null=False)
    quantidade = models.IntegerField('Quantidade', null=False, blank=False)
    contato = models.EmailField('Email', null=False, blank=False)
    tipo_contratacao = models.CharField('Tipo de contratação', null=False, blank=False, max_length=3,
                                        choices=CONTRATACAO_CHOICES)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo
