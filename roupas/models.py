from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    genero_choices = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Unissex', 'Unissex'),
    ]
    genero = models.CharField(max_length=10, choices=genero_choices)
    foto_url = models.URLField(max_length=200, blank=True) 

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tamanho(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    foto_url = models.URLField()
    cor = models.CharField(max_length=50)
    genero_choices = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Unissex', 'Unissex'),
    ]
    genero = models.CharField(max_length=10, choices=genero_choices)
    

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    

    def calcular_total(self):
        total = 0
        for produto in self.produtos.all():
            total += produto.preco
        return total
    def __str__(self):
        return f'Carrinho de {self.usuario.username}'
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    endereco_entrega = models.TextField()
    metodo_pagamento = models.CharField(max_length=100)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def calcular_total(self):
        total = 0
        for produto in self.produtos.all():
            total += produto.preco
        return total

    def __str__(self):
        return f"Pedido #{self.pk} - {self.usuario.username}"
