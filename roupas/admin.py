from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
    Produto, Categoria, Cliente, Pedido, ItemPedido, Pagamento, 
    AvaliacaoProduto, Endereco, Carrinho, ItemCarrinho, CupomDesconto, 
    Wishlist, ItemWishlist, HistoricoCompras, Marca, EnderecoEntrega, EnderecoCobranca, CustomUser
)

# Defina a classe inline para Cliente
class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = 'Clientes'


# Defina a classe admin personalizada para CustomUser
class CustomUserAdmin(BaseUserAdmin):
    inlines = (ClienteInline,)


# Registre o CustomUser com a classe admin personalizada
admin.site.register(CustomUser, CustomUserAdmin)

# Registre os modelos restantes com suas classes admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'quantidade_estoque']
    list_filter = ('categoria', 'marca', 'genero')
    search_fields = ('nome', 'descricao')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ('nome',)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(EnderecoEntrega)
class EnderecoEntregaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'endereco', 'cidade', 'estado', 'cep']
    search_fields = ['cliente__username', 'endereco', 'cidade', 'estado', 'cep']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'get_email', 'telefone', 'endereco', 'cidade', 'estado', 'cep']
    search_fields =['user__username', 'telefone', 'cidade', 'estado']
    list_filter = ('data_nascimento', 'cidade', 'estado') 

    @admin.display(ordering='user__username', description='Username')
    def get_username(self, obj):
        return obj.user.username

    @admin.display(ordering='user__email', description='Email')
    def get_email(self, obj):
        return obj.user.email

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_pedido', 'status']

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'produto', 'quantidade', 'preco_unitario']

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'tipo_pagamento', 'status_pagamento', 'data_pagamento', 'valor_pago']

@admin.register(AvaliacaoProduto)
class AvaliacaoProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'cliente', 'nota']

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'endereco', 'cidade', 'estado', 'cep']

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_criacao']

@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ['carrinho', 'produto', 'quantidade', 'preco_unitario']

@admin.register(CupomDesconto)
class CupomDescontoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'valor_desconto']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_criacao']

@admin.register(ItemWishlist)
class ItemWishlistAdmin(admin.ModelAdmin):
    list_display = ['wishlist', 'produto']

@admin.register(HistoricoCompras)
class HistoricoComprasAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'produto', 'quantidade', 'data_compra']

class GeneroListFilter(admin.SimpleListFilter):
    title = 'Gênero'
    parameter_name = 'genero'

    def lookups(self, request, model_admin):
        return (
            ('F', 'Feminino'),
            ('M', 'Masculino'),
            ('U', 'Unissex'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(genero=self.value())
        return queryset
    
@admin.register(EnderecoCobranca)
class EnderecoCobrancaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'endereco', 'cidade', 'estado', 'cep']
    search_fields = ['cliente__user__username', 'endereco', 'cidade', 'estado']
    list_filter = ('cidade', 'estado')

    def cliente(self, obj):
        return obj.cliente.user.username
