from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'

def index(request):
    # Lógica para a página inicial
    return render(request, 'index.html')
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
