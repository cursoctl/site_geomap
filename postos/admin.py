from django.contrib import admin
from django.utils.html import format_html
from .models import Posto, Imagem, Projeto, Servico, Mapa, FotoMapa

# Registre o modelo FotoMapa diretamente
admin.site.register(FotoMapa)

# Configuração do modelo Imagem
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('photo',)  # Exibe a imagem na lista do admin
    search_fields = ('photo',)  # Permite pesquisar pelo nome da imagem

admin.site.register(Imagem, ImagemAdmin)  # Registre uma única vez

# Configuração do modelo Projeto
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'link', 'get_imagem_thumbnail', 'get_imagem_url')
    search_fields = ('titulo',)

    # Exibe a miniatura da imagem no admin
    def get_imagem_thumbnail(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagem.url)
        return 'No image'
    get_imagem_thumbnail.short_description = 'Thumbnail'

    # Exibe a URL da imagem
    def get_imagem_url(self, obj):
        return obj.imagem.url if obj.imagem else 'No image'
    get_imagem_url.short_description = 'Imagem URL'

admin.site.register(Projeto, ProjetoAdmin)

# Configuração do modelo Mapa
@admin.register(Mapa)
class MapaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem')  # Exibe os campos nome, descricao e imagem
    search_fields = ('nome', 'descricao')  # Permite pesquisar pelos campos nome e descricao

# Configuração do modelo Servico
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')
