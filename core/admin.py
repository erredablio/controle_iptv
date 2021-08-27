from django.contrib import admin
from .models import Cliente, Compra, Licenca, Produto, Venda

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'celular']

admin.site.register(Cliente, ClienteAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

admin.site.register(Produto, ProdutoAdmin)

class CompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'produto', 'prazo', 'data_compra', 'quantidade', 'preco_compra']

admin.site.register(Compra, CompraAdmin)

class LicencaAdmin(admin.ModelAdmin):
    list_display = ['id', 'compra', 'cartao', 'codigo']

admin.site.register(Licenca, LicencaAdmin)

class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'licenca', 'cliente', 'data_venda', 'preco_venda']

admin.site.register(Venda, VendaAdmin)