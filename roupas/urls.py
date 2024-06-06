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
    path('produtos/masculinos/', views.ProdutoListView.as_view(genero='Masculino'), name='produtos_masculinos'),
    path('produtos/femininos/', views.ProdutoListView.as_view(genero='Feminino'), name='produtos_femininos'),

]