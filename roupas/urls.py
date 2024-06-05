from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),  # Lista de produtos
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),  # Detalhes do produto
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),  # Criar produto
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),  # Editar produto
    path('produtos/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='produto_delete'),  # Deletar produto
]
