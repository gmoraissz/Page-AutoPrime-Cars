from django.contrib import admin

from .models import Carro, Contato


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "ano", "preco", "combustivel", "cambio", "destaque", "disponivel")
    list_filter = ("marca", "combustivel", "cambio", "destaque", "disponivel")
    search_fields = ("marca", "modelo", "versao")
    list_editable = ("destaque", "disponivel")


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "carro", "lido", "criado_em")
    list_filter = ("lido", "criado_em")
    search_fields = ("nome", "email", "telefone")
    list_editable = ("lido",)
