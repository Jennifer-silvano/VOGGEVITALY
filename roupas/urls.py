from django.urls import path
from django.contrib import admin

from .views import ProdutoListView, ProdutoDetailView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('', admin.site.urls),
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/deletar/', ProdutoDeleteView.as_view(), name='produto_delete'),
]