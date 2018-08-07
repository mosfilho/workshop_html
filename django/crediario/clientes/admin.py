from django.contrib import admin
from crediario.admin import admin_site
from crediario.clientes.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('cd_chave','no_cliente','no_cidade',)
    list_display_links = ('cd_chave', 'no_cliente',)
    search_fields = ('cd_nomcod','no_cidade',)
    readonly_fields = ('cd_chave',)
    fieldsets = (
        (None, {
            'fields': ('cd_regiao', 'cd_cliente',)
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': ('no_endereco', 'no_bairro','no_cidade',)
        }),
    )
    list_filter = ('sg_loja',)

admin_site.register(Cliente, ClienteAdmin)