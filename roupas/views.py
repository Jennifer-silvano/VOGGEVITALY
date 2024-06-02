from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Produto, Categoria, CustomUser , Pedido, ItemPedido, Pagamento, AvaliacaoProduto, Endereco, Carrinho, ItemCarrinho, EnderecoEntrega, CupomDesconto, Wishlist, ItemWishlist, HistoricoCompras, EnderecoCobranca


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'quantidade_estoque', 'categoria', 'marca', 'tamanho', 'cor', 'imagem_url', 'genero']

    def form_valid(self, form):
        form.instance.data_criacao = timezone.now()
        return super().form_valid(form)

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_update.html'
    fields = ['nome', 'descricao', 'preco', 'quantidade_estoque', 'categoria', 'marca', 'tamanho', 'cor', 'imagem_url', 'genero']
