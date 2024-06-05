from django.contrib import admin
from .models import Categoria, Marca, Produto, Carrinho, Pedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'categoria', 'marca', 'display_tamanhos', 'cor', 'genero')

    def display_tamanhos(self, obj):
        return ", ".join([tamanho.nome for tamanho in obj.tamanhos.all()])
    
    display_tamanhos.short_description = 'Tamanhos'
@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'calcular_total')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'calcular_total', 'endereco_entrega', 'metodo_pagamento', 'data_pedido')
