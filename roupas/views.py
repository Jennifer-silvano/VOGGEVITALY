# views.py
from django.shortcuts import render, get_object_or_404,HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Produto, Categoria, Carrinho
import json

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produto'
    genero = None

    def get_queryset(self):
        genero = self.kwargs.get('genero')
        return Produto.objects.filter(genero=genero)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genero'] = self.kwargs.get('genero')
        return context
    


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'quantidade_estoque', 'categoria', 'marca', 'tamanhos', 'cor', 'foto_url', 'genero']

    def form_valid(self, form):
        form.instance.data_criacao = timezone.now()
        return super().form_valid(form)

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list.html')

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_update.html'
    fields = ['nome', 'descricao', 'preco', 'quantidade_estoque', 'categoria', 'marca', 'tamanhos', 'cor', 'foto_url', 'genero']

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'

def produtos_por_categoria(request, categoria_nome):
    categoria = get_object_or_404(Categoria, nome=categoria_nome)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'produtos_femininos_categoria.html', {'produtos': produtos, 'categoria': categoria})



class CarrinhoView(ListView):
    model = Carrinho
    template_name = 'carrinho.html'
    context_object_name = 'carrinho'

    def get_queryset(self):
        return Carrinho.objects.filter(usuario=self.request.user)

def adicionar_carrinho(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        produto_id = data.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)
        Carrinho.objects.create(produto=produto, usuario=request.user)
        return HttpResponse(status=200)
    return HttpResponse(status=400)