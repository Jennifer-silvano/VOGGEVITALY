from django.contrib import admin
from .models import Categoria, Marca, Produto, Carrinho, Pedido,Tamanho
from django.utils.html import format_html

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero',  'mostrar_foto')

    def mostrar_foto(self, obj):
        if obj.foto_url:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.foto_url)
        return "Sem Foto"
    mostrar_foto.short_description = 'Foto'

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'categoria', 'marca', 'cor', 'genero','foto_url')

    def display_tamanhos(self, obj):
        return ", ".join([tamanho.nome for tamanho in obj.tamanhos.all()])
    
    display_tamanhos.short_description = 'Tamanhos'
@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'calcular_total', )

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'calcular_total', 'endereco_entrega', 'metodo_pagamento', 'data_pedido')
