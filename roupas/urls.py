from django.urls import path
from . import views
from .views import CategoriaListView,CarrinhoView,ProdutoListView

urlpatterns = [
    path('produtos/<str:genero>/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),  # Detalhes do produto
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),  # Criar produto
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),  # Editar produto
    path('produtos/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='produto_delete'),  # Deletar produto
    path('', CategoriaListView.as_view(), name='categoria_list'),
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),
    path('produtos/masculino/<str:categoria_nome>/', views.produtos_por_categoria, name='produtos_masculinos_categoria'),
    path('produtos/feminino/<str:categoria_nome>/', views.produtos_por_categoria, name='produtos_femininos_categoria'),
    path('produtos/<str:genero>/', views.ProdutoListView.as_view(), name='produtos_genero'),
]