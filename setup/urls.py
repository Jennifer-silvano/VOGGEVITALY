from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Meu Admin"
admin.site.site_title = "Meu Admin"
admin.site.index_title = "Bem-vindo ao Meu Admin"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('roupas.urls'))

]